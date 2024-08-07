Tema 33

Testati functia proceseaza mockuind functia transforma
def transforma(obiect):
    if isinstance(obiect, str):
        return obiect.upper()
    elif isinstance(obiect, (int, float, complex)):
        return obiect ** 2
    else:
        return obiect
def proceseaza(lista):
    if not isinstance(lista, list):
        raise TypeError('Parametrul trebuie sa fie lista')
    return [transforma(elem) for elem in lista]
    
Modificati testele de la exercitiul precedent (de la curs) astfel incat sa foloseasca cel putin metoda .setUp() pentru a defini lista de elemente pentru toate testele.
