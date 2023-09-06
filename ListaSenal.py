class ListaSenal():    
    def __init__(self):
        self.inicio = None
        self.fin = None
        
    def mostrar(self):
        actual = self.inicio
        while actual != None:
            actual.imprimir()
            actual = actual.siguiente 
    
    def mostrar_inverso(self):
        actual = self.fin
        while actual != None:
            actual.imprimir()
            actual = actual.anterior

    def inicializar(self):
        self.inicio = None
        self.fin = None
        
    def insertar(self, data):
        if self.inicio == None:
            self.inicio = data
        else: 
            actual = self.inicio

            while actual.siguiente != None:
                actual = actual.siguiente 
            actual.siguiente = data

            
    def insertarOrdenadoNombre(self, objeto):
        if self.inicio == None:
            self.inicio = objeto
            self.fin = objeto
        else:
            if objeto.nombre < self.inicio.nombre:
                self.insertarInicio(objeto)
            elif objeto.nombre > self.fin.nombre:
                self.insertarFin(objeto)
            else:
                aux = self.inicio
                while aux != None:
                    if objeto.nombre < aux.nombre:
                        objeto.siguiente = aux
                        objeto.anterior = aux.anterior
                        aux.anterior.siguiente = objeto
                        aux.anterior = objeto
                        break
                    aux = aux.siguiente
                    
    
    
    def buscar_por_nombre(self, nombre):
        actual = self.inicio
        while actual != None:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente 
        return None
    
    
    def escribirXML(self):
        cadena = '<?xml version="1.0" encoding="UTF-8"?>\n'
        cadena += '<senales>\n'
        actual = self.inicio
        while actual:
            aux = actual.to_xml()
            cadena += aux
            actual = actual.siguiente
        cadena += '</senales>\n'
        with open("nuevaSenales.xml", "w") as archivo:
            archivo.write(cadena)
        print("¡Archivo XML generado!")