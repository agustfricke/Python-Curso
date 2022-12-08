persona = {
    'nombre': 'Agustin',
    'edad': 22
}
# print(persona)
# print(type(persona))

# Acceder al valor
# print(persona['edad'])

# Son ordenados || Pueden cambiar || No permite duplicados

# a = {
#     'nombre': 'Agustin',
#     'nombre': 'Juan'
# }
# print(a)


# len()

# persona = {
#     'nombre': 'Agustin',
#     'edad': 22, 
#     'es_admin': True,
#     'precio': 59.99
# }

# print(persona)


# dict

# persona = dict(nombre = 'Agustin', edad = 22)
# print(persona)
# print(type(persona))


# Obtener las llaves

persona = {
    'nombre': 'Agustin',
    'edad': 22, 
    'es_admin': True,
    'precio': 59.99
}

# print(persona.keys())

# # values()

# print(persona.values())

# # items()

# print(persona.items())


persona = {
    'nombre': 'Agustin',
    'edad': 22, 
    'es_admin': True,
    'precio': 59.99
}

# if 'sdsdsd' in persona:
#     print('Si esta!')
# else:
#     print('No esta!')

# cambiar items

persona = {
    'nombre': 'Agustin',
    'edad': 22, 
    'es_admin': True,
    'precio': 59.99
}

# persona['edad'] = 45
# print(persona)

# # update()
# persona.update({'es_admin': False})
# print(persona)


# 

persona = {
    'nombre': 'Agustin',
    'edad': 22, 
    'es_admin': True,
    'precio': 59.99
}

# persona['Nacionalidad'] = 'Argentina'
# # print(persona)

# # Eliminar

# persona.pop('es_admin')
# # print(persona)

# del persona['precio']
# print(persona)


# # clear()

# persona.clear()
# print(persona)


persona = {
    'nombre': 'Agustin',
    'edad': 22, 
    'es_admin': True,
    'precio': 59.99
}

# # Loop llaves
# for p in persona:
#     print(p)

# # Loop de valores
# for p in persona.values():
#     print(p)

# # Loop todos los items
# for a, b in persona.items():
#     print(a, b)


# Copiar diccionarios

# persona = {
#     'nombre': 'Agustin',
#     'edad': 22, 
#     'es_admin': True,
#     'precio': 59.99
# }

# copia = persona.copy()
# print(copia)
# print(persona)

# copia = dict(persona)
# print(copia)
# print(persona)

# Diccionarios anidados:

users = {
 'user1' : {
   'user_name' : 'Random',
   'email' : 'random@random.com'
 },
 'user2' : {
   'user_name' : 'Usuario',
   'email' : 'usuario@gmail.com'
 },
 'user3' : {
   'user_name' : 'admin',
   'email' : 'admin@admin.com'
 }
}
print(users)
