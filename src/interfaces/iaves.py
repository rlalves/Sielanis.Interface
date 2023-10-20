from abc import ABC, abstractclassmethod

class IAves(ABC):

    @abstractclassmethod
    def retorna_som(self):
        pass

    def retorna_voar(self):
        pass

    def retorna_alimento(self):
        pass