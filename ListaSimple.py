class ListaSimple:
    def __init__(self):
        self.inicio = None
        
    def agregar_al_final(self, data):
        if self.inicio == None:
            self.inicio = data
        else: 
            actual = self.inicio

            while actual.siguiente != None:
                actual = actual.siguiente 
            actual.siguiente = data
    
    def mostrar(self):
        actual = self.inicio
        while actual != None:
            actual.imprimir()
            actual = actual.siguiente 
        print("-"*30)
        
    def buscar_por_nombre(self, nombre):
        actual = self.inicio
        while actual != None:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente 
        return None
        