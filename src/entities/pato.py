from interfaces import IAves

class Pato(IAves):
    
    def retorna_som(self):
        return "Quack"
    
    def retorna_voar(self):
        return True
    
    def retorna_alimento(self):
        return "Peixes"