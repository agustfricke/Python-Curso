def texto():
    # Cuerpo de la funcion
    print('Hola Python')

# llamar a al funcion
# texto()

# Argumentos
def miNombre(nombre):
    print('Mi nombre es ' + nombre)

# miNombre('Belen')

# 2 Argumentos
def nombreCompleto(nombre, apellido):
    print('Mi nombre completo es ' + nombre + apellido)

# nombreCompleto('Agustin ', 'Fricke')


# Argementos *args
# def estudio (*args):
#     print('Estoy estudiando ' + args[2])

# estudio('React', 'Django', 'Python')


# Argumentos **kwargs
# def estudio(**kwargs):
#     print('Estoy estudiando ' + kwargs['Frontend'])

# estudio(Backend='Django', Frontend='React')

# Argumentos con palabra clave
# def estudio(a, b, c):
#     print('Estoy estudio ' + c)

# estudio(a = 'Python', b = 'React', c = 'Django')

# Predeterminado
# def pais(pais = 'Argentina'):
#     print('Soy de ' + pais)

# pais('Brasil')
# pais()


# Pasar lista como argemnto
# def misFrutas(frutas):
#     for fruta in frutas:
#         print(fruta)

# frutas = ['banana', 'kiwi', 'pera']
# misFrutas(frutas)


# Return
# def unaFuncion(x):
#     return 5 * x

# print(unaFuncion(1))
# print(unaFuncion(2))
# print(unaFuncion(10))

def unaFuncion():
    pass
