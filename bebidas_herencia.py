class Bebida:

    VOLUMEN_MULTIPLICADOR = 33.814
    MEDIDA = "oz"
    DECIMALES = 2

    def __init__(self, nombre, precio, volumen):
        self.nombre = nombre
        self.precio = precio
        self._volumen = volumen
        print(f"nueva bebida: {self.nombre}")

    def __str__(self):
        return f"{self.nombre} {self.precio}€ {self.volumen()} {self.MEDIDA}"
    
    def volumen(self):
        return round(self._volumen * self.VOLUMEN_MULTIPLICADOR, self.DECIMALES)

class BebidaAlcoholica(Bebida):
    
    def __init__(self, nombre, precio, volumen, graduacion):
        super().__init__(nombre, precio, volumen)
        self.graduacion = graduacion
        self.cantidad_alcohol = self.volumen() * self.graduacion

    def __str__(self):
        return Bebida.__str__(self) + " (alcoholica)"

class BebidaAltaGraduacion(BebidaAlcoholica):
    
    VOLUMEN_MULTIPLICADOR = 1000
    MEDIDA = "ml"
    DECIMALES = 0

    def __init__(self, nombre, precio, volumen, graduacion):
        super().__init__(nombre, precio, volumen, graduacion)

    def __str__(self):
        return super().__str__() + " (alta graduacion) " +\
                "alcohol: " + str(self.cantidad_alcohol) + self.MEDIDA
    

    def getMedida(self):
        return self.MEDIDA

bebidas = [
    Bebida("Coca Cola", 1.5, 0.33),
    Bebida("Agua", 0.80, 0.5),
    BebidaAlcoholica("Cerveza", 2.5, 0.33, 0.055),
    BebidaAltaGraduacion("Vodka", 5, 0.05, 0.4)
]

print("Bebidas:")
for bebida in bebidas:
    print(f" - {bebida}")


print(f"LA MEDIDA DE LA ALTA GRADUACION ES: {bebidas[3].getMedida()}")
