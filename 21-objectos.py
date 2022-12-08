# class Persona:
#     nombre = 'Juan'
#     apellido = 'Dou'

# print(Persona.nombre, Persona.apellido)

# p1 = Persona()
# print(p1.nombre)
# print(p1.apellido)

# __init__()

# class Persona:
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido

# # Obj numero 1
# p1 = Persona('Juan', 'Dou')
# print(p1.nombre, p1.apellido)

# # Obj numero 2
# p2 = Persona('Agustin', 'Fricke')
# print(p2.nombre, p2.apellido)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Mi nombre es {self.nombre} y tengo {self.edad} años'

p1 = Persona('Agustin', 22)
# print(p1)

# p1.edad = 50
# p1.nombre = 'Pepe'
# del p1.nombre
# del p1
# print(p1)


p2 = Persona('Juan', 32)
print(p2)

class Persona:
    pass