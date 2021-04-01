import random
import math
def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)

    acomulador = 0
    for x in X:
        acomulador += (x - mu)**2

    return acomulador /len(X)
def desviacion_estandar(X):
    return math.sqrt(varianza(X)) 
if __name__ == "__main__":
    X = [random.randint(0,100) for i in range(40)]

    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Arreglo de X: {X}')
    print(f'media = {mu}')
    print(f'Varianza= {Var}')
    print(f'desviacion estandar = {sigma}')