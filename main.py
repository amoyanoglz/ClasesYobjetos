from alumno import Alumno
from aula import Aula
from profesor import Profesor

mi_aula = Aula()
mi_profe = Profesor("Juanito Balerrama", 0, 10)

mi_aula.set_profesor(mi_profe)
mi_aula.add(Alumno("Pepito", "A", "pepito@a.com"))
mi_aula.add(Alumno("Lucia", "A", "lucia@a.com"))
mi_aula.add(Alumno("Martita", "A", "martita@b.com"))
mi_aula.add(Alumno("Gloria", "A", "gloria@b.com"))
mi_aula.add(Alumno("Juanito", "A", "juanito@c.com"))
mi_aula.add(Alumno("Jorgito", "A", "jorgito@c.com"))
mi_aula.add(Alumno("Jaimito", "A", "jaimito@c.com"))

mi_aula.puntuar()
mi_aula.listar()
print()
print("CONVOCADOS:")
mi_aula.convocar_examen("A")
