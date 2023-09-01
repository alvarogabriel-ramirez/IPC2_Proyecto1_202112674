from Nodo import Nodo

class Item(Nodo):
    def __init__(self, t, A, text):
        super().__init__()
        self.t = t
        self.A = A
        self.text = text
        
    
    def imprimir(self):
        print(f'     t : {self.t}, A: {self.A}, Text: {self.text}')