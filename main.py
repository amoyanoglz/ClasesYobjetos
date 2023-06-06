from alumno import Alumno
from aula import Aula

def convocar_todos():
    for turno in turnos:
        print(f"TURNO: {turno}")
        mi_aula.convocar_examen(turno)
        print("")

mi_aula = Aula()

turnos = ["A", "B", "C"]

mi_aula.add(Alumno("Pepito", turnos[0], "pepito@a.com"))
mi_aula.add(Alumno("Lucia", turnos[0], "lucia@a.com"))
mi_aula.add(Alumno("Martita", turnos[1], "martita@b.com"))
mi_aula.add(Alumno("Gloria", turnos[1], "gloria@b.com"))
mi_aula.add(Alumno("Juanito", turnos[2], "juanito@c.com"))
mi_aula.add(Alumno("Jorgito", turnos[2], "jorgito@c.com"))
mi_aula.add(Alumno("Jaimito", turnos[2], "jaimito@c.com"))
mi_aula.puntuar()

print()
print("CONVOCADOS:")
convocar_todos()

print("CONVOCADOS A:")
mi_aula.convocar_examen(turnos[0])
