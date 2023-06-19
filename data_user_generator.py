class DataUserGenerator:

    def __init__(self, cantidad_usuarios):
        self.next_user = 0
        self.usuarios = [
            {"nombre": "Pepito", "correo": "pepito@isdabea.st", "turno": "A"},
            {"nombre": "Ayoub Dalene", "correo": "pepito1@isdabea.st", "turno": "A"},
            {"nombre": "Løkenfeltet Hordaland", "correo": "pepito2@isdabea.st", "turno": "A"},
        ]

    def generar_usuario(self):

        if self.next_user >= len(self.usuarios):
            raise Exception(
                f"No hay más usuarios. se ha solicitado el usuario " +\
                    f"{self.next_user + 1}/{len(self.usuarios)} " +\
                    f"(indice {self.next_user}))")

        user = self.usuarios[self.next_user]
        self.next_user += 1

        return user
