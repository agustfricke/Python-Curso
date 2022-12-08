# frutas = ('pera', 'banana', 'melon')
# print(frutas)
# print(type(frutas))

# Son ordenadas || No pueden cambiar || Permiten duplicados

# Como determinar la longitud

# frutas = ('pera', 'banana', 'melon')
# print(len(frutas))

# 1 solo item

# a = ('pera',)
# print(a)
# print(type(a))

# Tipos de datos en las tuplas

# a = ('pera', 78, 98.0, True)
# print(type(a))


# Crear una tupla con tuple()

# a = tuple(('banana', 45))
# print(a)
# print(type(a))


# Acceder al numero de index

# a = ('pera', 98, True)
# # print(a[1])
# # print(a[-1])

# print(a[-2:-1])

# a = ('pera', 'banana', True, 78, 90, False)

# if 'sdsdsd' in a:
#     print('Si existe')
# else:
#     print('No existe')


# De tupla a lista 
# a = ('pera', 'banana', True, 78, 90, False)
# lista = list(a)
# print(type(lista))
# print(lista)

# lista.append('kiwi')
# print(lista)

# a = tuple(lista)
# print(a)
# print(type(a))


# Agregar una tupla a una tupla

# a = ('pera', 'banana', True, 78, 90, False)
# nuevoItem = ('kiwi',)
# a += nuevoItem
# print(a)


# Eliminar

# a = ('pera', 'banana', True, 78, 90, False)
# print(a)

# lista = list(a)
# lista.remove('banana')
# a = tuple(lista)
# print(a)


# a = ('pera', 'banana', True, 78, 90, False)
# del a 
# print(a)


# Desempacar tuplas

# tupla1 = ('pera', 'kiwi', 'naranja')
# print(tupla1)
# fruta1, fruta2, fruta3 = tupla1
# print(fruta1)
# print(fruta2)
# print(fruta3)

# *

# frutas = ('pera', 'banana', 'sandia', 'melon')
# fruta1, *fruta2 = frutas
# print(fruta1)
# print(fruta2)

# Bucles for

frutas = ('pera', 'banana', 'sandia', 'melon')
# for fruta in frutas:
#     print(fruta)

# for fruta in range(len(frutas)):
#     print(frutas[fruta])

# while
frutas = ('pera', 'banana', 'sandia', 'melon')

# x = 0

# while x < len(frutas):
#     print(frutas[x])
#     x = x + 1


# Unir tuplas

frutas = ('pera', 'banana', 'sandia', 'melon')

tuplaX2 = frutas * 2
print(tuplaX2)