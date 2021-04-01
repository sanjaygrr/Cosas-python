import random
import collections
PALOS = ['espada', 'corazon','rombo', 'trebol']
VALORES = ['A','2','3','4','5','6','7','8','9','10','j','q','k']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))

    return barajas


def obtener_mano(barajas, tamaño_mano):
    mano = random.sample(barajas, tamaño_mano)
    return mano

def main(tamaño_mano, intentos):
    barajas = crear_baraja()
    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamaño_mano)
        manos.append(mano)
    
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        print(counter)
        for val in counter.values():
            if val == 2:
                pares += 1
                break
        probabilidad_par = pares / intentos
        print(f'La probabilidad de obtener un par en una mano de {tamaño_mano} barajas es {probabilidad_par}')
if __name__ == "__main__":
    tamaño_mano = int(input('de cuantas barajas será a mano?: '))
    intentos = int(input('cuantos intentos para calcular la probabilidad?: '))
    main(tamaño_mano, intentos)
    barajas = crear_baraja()
    mano = obtener_mano(barajas, 5)

    # print(barajas)