from random import uniform

from alumno import Alumno
from aula import Aula
from profesor import Profesor
from generador_usuarios import GeneradorDeUsuarios


class CentroEducativo:
    def __init__(self, alumnos=1, profesores=1, aulas=1):
        total_usuarios = alumnos + profesores
        self.aulas = []
        self.alumnos = []
        self.profesores = []
        self.data_user_generator = GeneradorDeUsuarios(total_usuarios)

        self.generar_aulas(aulas)
        self.generar_profesores(profesores)
        self.generar_alumnos(alumnos)
        self.asignar_profesores()
        self.asignar_alumnos()

    def generar_aulas(self, aulas):
        for i in range(aulas):
            self.aulas.append(Aula())

    def generar_profesores(self, profesores):
        for i in range(profesores):
            usuario = self.data_user_generator.generar_usuario()
            profesor = Profesor(
                usuario["nombre_completo"],
                round(uniform(0, 4), 2),
                round(uniform(6, 10), 2),
            )

            self.profesores.append(profesor)

    def generar_alumnos(self, alumnos):
        for i in range(alumnos):
            usuario = self.data_user_generator.generar_usuario()
            self.alumnos.append(
                Alumno(usuario["nombre_completo"], usuario["correo"])
            )

    def asignar_profesores(self):
        for i, profesor in enumerate(self.profesores):
            aula = self.aulas[i % len(self.aulas)]
            aula.set_profesor(profesor)

    def asignar_alumnos(self):
        for i, alumno in enumerate(self.alumnos):
            self.aulas[i % len(self.aulas)].add(alumno)

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

            print("\n" * 1)
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
