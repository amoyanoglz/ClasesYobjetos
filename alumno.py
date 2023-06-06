class Alumno:
    def __init__(self, nombre, turno, correo):
        self.nombre = nombre
        self.correo = correo
        self.turno = turno
        self.nota = 0

    def setNota(self, nota):
        self.nota = nota

    def describe(self):
        print(f"Alumno: {self.nombre.ljust(8)}", end = " - ")
        print(f"Turno:  {self.turno}", end = " - ")
        print(f"Nota:   {self.nota}")

    def convocar_examen(self, turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"{self.correo}")
            print(f"    Estimado/a {self.nombre}, su nota media ha sido un {self.nota} ha sivo vd convocado al blablabla")

