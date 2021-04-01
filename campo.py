
class Campo:

    def __init__(self):
        self.coordendas_borrachos = {}

    def añadir_borracho(self, borracho, coordenada):
        self.coordendas_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_borrachos[borracho]
        nueva_coordenada = coordenada_actua.mover(delta_x,delta_y)

        self.coordendas_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self,borracho):
        return self.coordendas_borrachos[borracho]