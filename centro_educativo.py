from alumno import Alumno
from aula import Aula
from profesor import Profesor
from data_user_generator import DataUserGenerator


class CentroEducativo:
    def __init__(self, alumnos=1, profesores=1, aulas=1):
        self.data_user_generator = DataUserGenerator(10)
        self.aulas = []
        self.alumnos = []
        self.profesores = []

        self.cantidad = {"aulas": aulas, "alumnos": alumnos, "profesores": profesores}

        self.generar_aulas()
        self.generar_profesores()
        self.generar_alumnos()
        self.asignar_profesores()
        self.asignar_alumnos()

    def generar_aulas(self):
        for i in range(self.cantidad["aulas"]):
            self.aulas.append(Aula())

    def generar_profesores(self):
        self.profesores = [
            Profesor("Juanito Balerrama", 0, 10),
            Profesor("Manolito Pomporretas", 0, 10),
            Profesor("Teres Rabal", 0, 10),
        ]

    def generar_alumnos(self):
        for i in range(self.cantidad["alumnos"]):
            usuario = self.data_user_generator.generar_usuario()
            self.alumnos.append(Alumno(usuario["nombre"], usuario["correo"], "A"))

    def asignar_profesores(self):
        contador = 0
        while contador < len(self.profesores):
            self.aulas[contador % (len(self.aulas) - 1)].set_profesor(
                self.profesores[contador]
            )
            contador += 1

    def asignar_alumnos(self):
        contador = 0
        while contador < len(self.alumnos):
            self.aulas[contador % (len(self.aulas) - 1)].add(self.alumnos[contador])
            contador += 1

    def listar(self):
        contador = 0
        for aula in self.aulas:
            print(f"AULA {contador} ----------------------------- ")
            try:
                aula.listar()
            except Exception as e:
                print(e)

            print("\n" * 3)
            contador += 1

    def puntuar(self):
        print("- LISTADO DE AULAS Y ALUMNOS:")
        contador = 0
        for aula in self.aulas:
            print(f"AULA {contador} ----------------------------- ")
            try:
                aula.puntuar()
            except Exception as e:
                print(e)

            print("\n" * 3)
            contador += 1

    def convocar(self, turno="A"):
        print("- CONVOCACIONES:")
        contador = 0
        for aula in self.aulas:
            print(f"AULA {contador} ----------------------------- ")
            try:
                aula.convocar_examen(turno)
            except Exception as e:
                print(e)

        print("\n" * 3)
        contador += 1
