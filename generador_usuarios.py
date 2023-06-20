import requests


class GeneradorDeUsuarios:
    def __init__(self, total_usuarios, limite_de_peticion=5000, debug_level=0):
        self.limite_de_peticion = limite_de_peticion
        self.debug_level = debug_level
        self.total_usuarios = total_usuarios
        self.usuarios_solicitados = 0
        self.usuarios_generados = 0
        self.indice_siguiente_usuario = 0
        self.usuarios = []
        self.solicitar_usuarios()

    def generar_usuario(self):
        if self.debe_solicitar_mas():
            self.solicitar_usuarios()

        usuario = self.obtener_usuario_de_buffer()
        self.usuarios_generados += 1
        return usuario

    def obtener_usuario_de_buffer(self):
        if self.indice_siguiente_usuario >= len(self.usuarios):
            raise Exception(
                f"No hay más usuarios. Se solicitó el usuario "
                + f"{self.indice_siguiente_usuario + 1}/{len(self.usuarios)} "
                + f"(indice {self.indice_siguiente_usuario})"
            )
        usuario = self.usuarios[self.indice_siguiente_usuario]
        self.indice_siguiente_usuario += 1

        if self.debug_level > 1:
            print(self.buffer_stattus())

        return usuario

    def buffer_stattus(self):
        return {
            "total_usuarios": self.total_usuarios,
            "usuarios_solicitados": self.usuarios_solicitados,
            "indice_siguiente_usuario": self.indice_siguiente_usuario,
            "usuarios_en_buffer": len(self.usuarios),
        }

    def solicitar_usuarios(self):
        # limpiar buffer si es necesario
        if self.indice_siguiente_usuario >= len(self.usuarios):
            self.usuarios = []
            self.indice_siguiente_usuario = 0

        cantidad_solicitud = min(
            self.total_usuarios - self.usuarios_solicitados,
            self.limite_de_peticion,
        )

        self.usuarios_solicitados += cantidad_solicitud

        if self.debug_level or cantidad_solicitud > 25:
            print(f"Solicitando {cantidad_solicitud} usuarios")
        uri = f"https://randomuser.me/api/?results={cantidad_solicitud}"
        respuesta = requests.get(uri)
        self.usuarios += self.procesar_respuesta(respuesta)

    def procesar_respuesta(self, respuesta):
        usuarios_recibidos = []
        randomuser = respuesta.json()

        if isinstance(randomuser, dict) and "error" in randomuser:
            raise Exception(f"Error en la solicitud: {randomuser['error']}")

        for persona in randomuser["results"]:
            nombre_completo = persona["name"]["first"] + " " + persona["name"]["last"]
            usuarios_recibidos.append(
                {"nombre_completo": nombre_completo, "correo": persona["email"]}
            )

        if self.debug_level:
            print(f"Recuperados {len(usuarios_recibidos)} usuarios")

        return usuarios_recibidos

    def debe_solicitar_mas(self):
        buffer_sobrepasado = self.indice_siguiente_usuario >= len(self.usuarios)
        faltan_usuarios = self.usuarios_solicitados < self.total_usuarios

        return buffer_sobrepasado and faltan_usuarios

    def usuarios_restantes(self):
        return self.total_usuarios - self.usuarios_generados


if __name__ == "__main__":
    from random import randint

    IMPRIME_CADA_LOTE = 2

    total_usuarios = randint(50, 200)
    limite_de_peticion = randint(4, 25)

    print(f"Generando {total_usuarios} usuarios ...\n")
    generador = GeneradorDeUsuarios(total_usuarios, limite_de_peticion, debug_level=1)

    contador = 0
    for i in range(total_usuarios):
        usuario = generador.generar_usuario()
        if contador < IMPRIME_CADA_LOTE:
            print(usuario)
        elif contador == IMPRIME_CADA_LOTE + 1 and generador.usuarios_restantes() > 0:
            print(f"{generador.usuarios_restantes()} usuarios más ...")
        else:
            pass
        contador += 1
        if contador >= limite_de_peticion:
            contador = 0
