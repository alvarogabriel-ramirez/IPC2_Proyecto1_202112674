from Nodo import Nodo
from ListaSenal import ListaSenal


class Senal(Nodo):
    def __init__(self, nombre, tiempo, amplitud):
        super().__init__()
        self.nombre = nombre
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.items = ListaSenal()

    def imprimir(self):
        print(
            f'SENAL --- Nombre: {self.nombre}, t: {self.tiempo} , A: {self.amplitud}')
        print("-"*60)
        self.items.mostrar()

    def to_dot(self):
        nodo_nombre = f'senal_{self.nombre}'
        cadena = f'"{nodo_nombre}" [label="{self.nombre}", shape=ellipse, color=red];\n'
        nodo_tiempo = f"{nodo_nombre}_tiempo"
        nodo_amplitud = f"{nodo_nombre}_amplitud"
        cadena += f'"{nodo_tiempo}" [label="Tiempo: {self.tiempo}", shape=ellipse, color=lightblue];\n'
        cadena += f'"{nodo_amplitud}" [label="Amplitud: {self.amplitud}", shape=ellipse, color=lightblue];\n'
        cadena += f'"{nodo_nombre}" -> "{nodo_tiempo}";\n'
        cadena += f'"{nodo_nombre}" -> "{nodo_amplitud}";\n'

        nodo_items = f"{nodo_nombre}_items"
        cadena += f'"{nodo_items}" [label="Datos", shape=ellipse, color=green];\n'
        cadena += f'"{nodo_nombre}" -> "{nodo_items}";\n'

        for c in range(1, self.amplitud + 1):
            prev_item = nodo_items
            for r in range(1, self.tiempo + 1):
                item = self.get_item(r, c)
                item_nodo_nombre = f"{nodo_nombre}_item_{r}_{c}"
                cadena += f'"{item_nodo_nombre}" [label="{item.text if item else "-"}", shape=ellipse];\n'

                if r == 1:
                    cadena += f'"{nodo_items}" -> "{item_nodo_nombre}";\n'

                else:
                    cadena += f'"{prev_item}" -> "{item_nodo_nombre}";\n'

                prev_item = item_nodo_nombre
        return cadena

    def to_xml(self):
        cadena = f'<senal nombre="{self.nombre}" amplitud="{self.amplitud}">\n'
        actual = self.items.inicio
        while actual:
            cadena += f'\t<item row="{actual.t}" col="{actual.A}">{actual.text}</item>\n'
            actual = actual.siguiente
        cadena += "</senal>\n"
        return cadena

    def get_item(self, t, A):
        actual = self.items.inicio
        while actual:
            if actual.t == t and actual.A == A:
                return actual
            actual = actual.siguiente
        return None

        
    