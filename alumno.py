from user import User


class Alumno(User):

    DECIMALES_NOTA = 2

    def __init__(self, nombre, correo, turno = "A"):
        super().__init__(nombre, correo)
        self.turno = turno
        self.nota = 0

    def __str__(self):
        buffer = []
        buffer.append(f"Alumno: {self.nombre.ljust(24)}\n")
        buffer.append(f" Turno: {self.turno}\n")
        buffer.append(f"  Nota: {self.getNota()}")

        return "".join(buffer)

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return round(self.nota, self.DECIMALES_NOTA)

    def convocar_examen(self, turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"{self.correo}")
            print(
                f"    Estimado/a {self.nombre}, "
                + f"su nota media ha sido un {self.getNota()} "
                + f"ha sivo vd convocado al blablabla"
            )
