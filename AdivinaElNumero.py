import random

def run():
    numero_aleatorio = random.randint(1, 500)
    numero_elegido = int(input('Elige un número entre el 1 y el 500: '))
    pass

    while numero_aleatorio != numero_elegido:
        if(numero_aleatorio > numero_elegido):
            print('busca un numero más grande!!')
        else: 
            print('busca un numero más pequeño po!!')
        numero_elegido = int(input('ingresa otro numero: '))

    print('GANASTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
if __name__== '__main__':
    run()