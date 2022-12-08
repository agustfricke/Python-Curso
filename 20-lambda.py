# lambda argumentos :  expresion

x = lambda a : a + 10
# print(x(5))

def miFuncion(n):
    return lambda a : a * n

X2 = miFuncion(2)
print(X2(50))