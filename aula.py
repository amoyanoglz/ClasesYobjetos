import random

class Aula:
    def __init__(self):
        self.alumnos = []
    
    def add(self, alumno):
        self.alumnos.append(alumno)
    
    def listar(self):
        for alumno in self.alumnos:
            alumno.describe()
    
    def convocar_examen(self, turno):
        for alumno in self.alumnos:
            alumno.convocar_examen(turno)

    def puntuar(self):
        for alumno in self.alumnos:
            alumno.setNota(random.randint(3, 10))
            if alumno.turno == "A":
                alumno.setNota(0)
            alumno.describe()

