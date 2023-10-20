from factory import aves_factory

f = aves_factory.Aves_Factory()

ave = f.fabrica(1)
print(ave.retorna_som())
print(ave.retorna_voar())
print(ave.retorna_alimento())
    
ave = f.fabrica(2)
print(ave.retorna_som())
print(ave.retorna_voar())
print(ave.retorna_alimento())