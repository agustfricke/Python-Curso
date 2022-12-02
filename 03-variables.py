# variableiables 

nombre = 'Agustin'
edad = 22

nombre = 'Agustin'
edad = 22
print(nombre)
print(edad)

nombre = 'Juan'
edad = 'treinta'

nombre = 'Agustin'
edad = 22
print(type(nombre))
print(type(edad))

nombre = 'Agustin'
apellido = 'Fricke'

nombre = 'Pithon'
Nombre = 'Pithon'

mivariable = 'Python'
mi_variable = 'Python'
_mi_variable = 'Python'
mivariable = 'Python'
Mivariable = 'Python'
mivariable2 = 'Python'

# 2mivariable = 'Python'
# mi-variable = 'Python'
# mi variable = 'Python'

# miVariable = 'Python'
# MiVariable = 'Python'
# mi_variable = 'Python'

# a, b, c = 'pera', 'melon', 'naranja'
# print(a)
# print(b)
# print(c)


# a, b, c = 'Python'
# print(a)
# print(b)
# print(c)


frutas = ['manzana', 'pera', 'melon']
a, b, c = frutas
print(a)
print(b)
print(c)


a = 'Me'
b = 'gusta'
c = 'Python'
print(a, b, c)

a = 'Me'
b = 'gusta'
c = 'Python'
print(a + b + c)

a = 'Me '
b = 'gusta '
c = 'Python'
print(a + b + c)

a = 5
b = 5 
print(a + b)
10

a = 3
b = 'Python'
print(b, a)

# Declaramos la variable
nombre = 'Python'

# Declaramos la funcion
def miFuncion():
    # Usamos la variable dentro de la funcion
    print('Me gusta ' + nombre)

# Llamamos a la funcion
miFuncion()


# Declaramos la variable global
nombre = 'Python'

# Declaramos la funcion
def miFuncion():
    # Declaramos variable local
    nombre = 'JavaScript'
    # Impimios por consola la variable local
    print('Me gusta ' + nombre)

# Llamamos a la funcion
miFuncion()

# Imprimimos por consola la varibale global 
print('Me gusta ' + nombre)



# Declaramos la funcion
def miFuncion():
    # Hacmos la variable global
    global nombre
    # Declaramos la variable
    nombre = 'Python'
    # Usamos la variable dentro de la funcion
    print('Me gusta ' + nombre)

# Llamamos a la funcion
miFuncion()

# Usamos la variable fuera de la funcion
print('Me gusta ' + nombre)