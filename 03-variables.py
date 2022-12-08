# Variables

# edad = 32.32

# nombre = 'Belen'
# nOMBRE = 'JUAN'

# print(nombre)
# print(nOMBRE)
# print(edad)

# Nombres Permitidos:

mivariable = 'Python'
mi_variable = 'Python'
_mi_variable = 'Python'
mivariable = 'Python'
Mivariable = 'Python'
mivariable2 = 'Python'

# Nombre no Permitidos:

# 2mivariable = 'Python'
# mi-variable = 'Python'
# mi variable = 'Python'

# Deben comenzar por una letra o guión bajo
# Deben contener sólo caracteres alfanuméricos y guiones bajos(A-z, 0-9 y _)
# No pueden comenzar con un número(0-9)
# Presta atención a las mayusculas y minusculas(Edad es una variables diferente a edad)


# Camel case:
miVariablePrimera = 4

# Pascal case:
MiVariable = 78

# Sanke case:
mi_variable = 89


# Muchos valores a muchas variables
# a, b, c = 'pera', 'banana', 'melon'


# Un valor a muchas variables
# a = b = c = 'Python'
# print(a)
# print(b)
# print(c)

# Desempacar coleccion de datos unpacking

# frutas = ['pera', 'banana', 'melon']
# # print(frutas)
# a, b, c = frutas
# # print(a)
# # print(b)
# # print(c)
# print(a, b, c)

# Concatenar
# a = 'Me '
# b = 'gusta '
# c = 'Python'

# x = 15
# y = 3


# print(c, y)

# Varibales globales global

nombre = 'Python'

def miFuncion():

    global nombre
    nombre = 'JavaScript'
    print('Me gusta ' + nombre)

miFuncion()

print(nombre)