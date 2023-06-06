import random

class Aula:
    def __init__(self):
        self.alumnos = []
        self.profesor = None
    
    def add(self, alumno):
        self.alumnos.append(alumno)
    
    def listar(self):
        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.describe()
    
    def convocar_examen(self, turno):
        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.convocar_examen(turno)

    def puntuar(self):
        for alumno in self.alumnos:
            alumno.setNota(self.profesor.generar_nota())
            alumno.describe()
    
    def set_profesor(self, profesor):
        self.profesor = profesor

