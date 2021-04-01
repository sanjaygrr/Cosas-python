
print('BIENVENIDO')
print('Este programa le permitirá sacar su valor acomulado de manera individual como empresarial')
personas = int(input('¿cuantas personas dese agregar?'))
total_empresarial = 0
agregar = 's'
while agregar == "s":
    for i in range(0,personas):
        print('Persona', i+1)
        P = int(input('ingrese el valor de deposito mensual: '))
        n = int(input('ingrese cantidad de depositos mensuales: '))
        x = float((input('ingrese Tasa de interés mensual: ')))
        A = float(P*((((1+x)**n)-1)/x))
        total_empresarial += A

        print(f'el Total Empresarial es {total_empresarial}')
        agregar = input('¿desea hacer alguna otra operaion?')
input()