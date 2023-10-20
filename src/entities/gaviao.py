from interfaces import IAves

class Gaviao(IAves):
    
    def retorna_som(self):
        return "Grrrr"
    
    def retorna_voar(self):
        return True
    
    def retorna_alimento(self):
        return "Outras Aves"