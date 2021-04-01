import random
def generar_contraseña():
    largo = int(input('¿Cuántos caracateres necesitas?: '))
    mayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','X','Y','Z']
    minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','x','y','z']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    cosas = ["<",">",".,","","!","#","$","%","&","/","(",")"]
    caracteres = mayus + minus + numeros + cosas
    
    contrasena = []

    for i in range(largo):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contraseña()
    print(f'tu nueva contraseña es {contrasena}')
    pass

if __name__ == '__main__':
    run()