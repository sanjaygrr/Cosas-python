import random
import math
from estadisticas import desviacion_estandar, media
def aventar_punto(numero_de_puntos):
    dentro_circulo = 0

    for _ in range(numero_de_puntos):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])

        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            dentro_circulo += 1
    return (4*dentro_circulo) / numero_de_puntos

def estimacion(numero_de_puntos, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_punto(numero_de_puntos)
        estimados.append(estimacion_pi)
    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)

    print(f'est = {round(media_estimados, 5)}, sigma = {round(sigma, 5)}, puntos = {numero_de_puntos}')
    return (media_estimados,sigma)
def estimar_pi(precision, numero_de_intentos):
    numero_de_puntos = 1000
    sigma = precision

    while sigma >= precision/1.96 :
        media, sigma = estimacion(numero_de_puntos, numero_de_intentos )
        numero_de_puntos *= 2
    return media

if __name__ == "__main__":
    estimar_pi(0.01, 1000)