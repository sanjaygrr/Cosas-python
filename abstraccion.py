class  Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'llenando el tanque con agua{temperatura}')

    def _añadir_jabon(self):
        print('añadiendo jabon')
   
    def _lavar(self):
        print('lavando la ropa')
    
    def _centrifugar(self):
        print('centrifugando la ropa')

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()