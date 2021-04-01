

def morral(capacidad_morral, pesos_elementos, valores_elementos, n):

    if n == 0 or capacidad_morral == 0:
        return 0

    if pesos_elementos[n-1] > capacidad_morral:
        return morral(capacidad_morral, pesos_elementos, valores_elementos, n-1)
        
    return max(valores_elementos[n-1] + morral(capacidad_morral - pesos_elementos[n-1], pesos_elementos, valores_elementos, n-1),
                morral(capacidad_morral, pesos_elementos, valores_elementos, n-1))


if __name__ == '__main__':
    valores_elementos = [60, 100, 120]
    pesos_elementos = [10,20,30]
    capacidad_morral = int(input('Cual es el tamaño de su morral?'))
    n = len(valores_elementos)

    resultado = morral(capacidad_morral, pesos_elementos, valores_elementos, n)
    print(resultado)