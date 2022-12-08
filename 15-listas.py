# frutas = ['pera', 'banana', 'naranja', 'pera']
# print(frutas)
# print(type(frutas))

# Son ordenadas || Pueden cambiar || Permiten valores duplicados 

# Logingitud de una lista

# frutas = ['pera', 'banana', 'naranja', 'pera']
# print(len(frutas))


# Tipos de datos dentro de las listas

# a = ['pera', 'banana', True, 56, 98.09]

# print(a)
# print(type(a))


# Crear una lista con list()

# frutas = list(('pera', 'kiwi', 'banana'))
# print(frutas)
# print(type(frutas))


# Acceder a los items

# a = ['pera', 34.67, True, 'Python']

# # print(a[2])

# # print(a[-3])

# print(a[1:3])
# print(a[:3])
# print(a[1:])
# print(a[-4:-2])


# in

# frutas = ['pera', 'banana', 'kiwi']

# if 'dffdf' in frutas:
#     print('Si pera esta en frutas')
# else:
#     print('No esta en frutas')


# cambiar los items

# frutas = ['pera', 'banana', 'kiwi']

# # frutas[1] = 'naranja'

# # print(frutas)

# frutas[1:3] = ['coco', 'naranja']
# print(frutas)


# frutas [1:3] = ['coco']
# print(frutas)


# insertar elementos en una lista

# frutas = [12, True, 'Holad']
# frutas.insert(2, 'pera')
# print(frutas)

# Agregar elementos a una lista

# frutas = ['pera', 'naranja', 'kiwi']
# frutas.append('manzana')
# print(frutas)


# Extender una lista

# a = ['pera', 'naranja', 'kiwi']
# b = ['pera', 'naranja', 'kiwi', 67, True]

# a.extend(b)
# print(a)


# Eliminar items

# a = ['pera', 'naranja', 'kiwi']
# a.remove('kiwi')
# print(a)

# a.pop()
# print(a)

# del a[1]
# print(a)

# a.clear()
# print(a)

# del a
# print(a)




# Bucles for con listas

# a = ['pera', 'naranja', 'kiwi']

# for fruta in a:
#     print(fruta)


# for fruta in range(len(a)):
#     print(fruta)


# Bucles while con las listas

# frutas = ['pera', 'naranja', 'kiwi']

# x = 0

# while x < len(frutas):
#     print(frutas[x])

#     x = x + 1


# Comprension de una lista

# frutas = ['pera', 'manzana', 'kiwi']

# nuevaLista = []

# nuevaLista = [fruta for fruta in frutas if fruta != 'pera']
# print(nuevaLista)

# nuevaLista = [x for x in frutas if 'a' in x]
# print(nuevaLista)



# for fruta in frutas:
#     if 'a' in fruta:
#         nuevaLista.append(fruta)

# print(nuevaLista)
# print(frutas)


# Ordenar las listas

# a = ['d', 'b', 'a', 'c']
# b = [4, 2, 1, 3]
# a.sort()
# a.reverse()
# print(a)
# b.sort(reverse = True)
# print(b)
    

# Copiar listas copy()

# lista1 = ['pera', 'Python', 98]
# lista2 = list(lista1)
# print(lista2)



# lista2 = lista1.copy()

# print(lista2)


# Unir listas

lista1 = ['pera', 'melón', 'naranja']
lista2 = ['sandía', 'manzana', 'kiwi']

lista1.extend(lista2)
print(lista1)



# lista3 = lista1 + lista2
# print(lista3)

# for x in lista2:
#     lista1.append(x)

# print(lista1)






