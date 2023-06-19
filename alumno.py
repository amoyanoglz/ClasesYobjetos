from user import User
class Alumno(User):

    def __init__(self, nombre, turno, correo):
        super().__init__(nombre, correo)
        self.turno = turno
        self.nota = 0

    def __str__(self):
        buffer = []
        buffer.append(f"Alumno: {self.nombre.ljust(8)}\n")
        buffer.append(f" Turno: {self.turno}\n")
        buffer.append(f"  Nota: {self.getNota()}")

        return "".join(buffer)

    def setNota(self, nota):
        self.nota = nota

    
    def getNota(self):
        return round(self.nota, 2)

    def convocar_examen(self, turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"{self.correo}")
            print(f"    Estimado/a {self.nombre}, su nota media ha sido un {self.nota} ha sivo vd convocado al blablabla")

