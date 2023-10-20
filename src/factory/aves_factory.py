from entities import Gaviao
from entities import Pato

class Aves_Factory():

    def fabrica(self, tipo_ave: int):
        # receive tipo_ave and return the correct instance of Ave
        if tipo_ave == 1:
            return Gaviao()
        elif tipo_ave == 2:
            return Pato()
        else:
            raise ValueError("Tipo de ave inválido")