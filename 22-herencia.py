class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombreCompleto(self):
        print(self.nombre, self.apellido)

# p1 = Persona('Agustin', 'Fricke')
# p1.nombreCompleto()

class Estudiante(Persona):
    def __init__(self, nombre, apellido, año):
        super().__init__(nombre, apellido)
        self.año = año
    def bienvendio(self):
        print('Bienvenido', self.nombre, self.apellido, 'a la clase ', self.año)

e1 = Estudiante('Juan', 'Perez', 2024)
e1.bienvendio()

