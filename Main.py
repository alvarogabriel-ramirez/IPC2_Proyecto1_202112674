import xml.etree.ElementTree as ET

import os
from Senal import Senal
from Dato import Item
from ListaSimple import ListaSimple
import os

senales = ListaSimple()

def carga_datos(ruta):

    if not os.path.isfile(ruta):
        print("El archivo no existe")
        return

    if not ruta.endswith(".xml"):
        print("El archivo debe ser .xml")
        return
    
    #elementos.inicializar()
    tree = ET.parse(ruta)
    root = tree.getroot()
    for senal in root.findall('senal'):
        nombre = senal.get('nombre')
        tiempo = int(senal.get('t'))
        amplitud = int(senal.get('A'))
        senal_nueva = Senal(nombre,tiempo,amplitud)
        
        for dato in senal.findall('dato'):
            t = int(dato.get('t'))
            A = int(dato.get('A'))
            text = dato.text
            dato_nuevo = Item(t,A,text)
            senal_nueva.items.agregar_al_final(dato_nuevo)
        
        senales.agregar_al_final(senal_nueva)
        #elementos.insertarOrdenadoPorId(senal_nueva)
        
    print("** Datos cargados correctamente **")

def graficar(elemento):
    dot_string = 'digraph G {\n'
    dot_string += elemento.to_dot()
    dot_string += "}\n"
    with open("matriz.dot", "w") as archivo:
        archivo.write(dot_string)
    os.system("dot -Tpng matriz.dot -o matriz.png")
    print("¡Gráfica generada!")


def menu():
    while True: 
        print("MENU PRINCIPAL")
        print("1. Cargar Archivo")
        print("2. Mostrar elementos")
        print("3. Generar imagen")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            print("Cargar Archivo")
            ruta = input("Ingrese la ruta del archivo: ")
            carga_datos(ruta)
        elif opcion == "2":
            print("Mostrar elementos")
            senales.mostrar()
        elif opcion == "3":
            print("Generar imagen")
            senales.mostrar()
            nombre = input("Ingrese el nombre del elemento: ")
            elemento = senales.buscar_por_nombre(nombre)
            if elemento:
                graficar(elemento)
            else:
                print(f"El elemento con ID {nombre} no existe")
        elif opcion == "4":
            print("Mostrar datos del estudiante")
            print("-> Alvaro Gabriel Ramirez Alvarez")
            print("-> 202112674")
            print("-> Introducción a la Programación y Computación 2 A")
            print("-> Ingeniería en Ciencias y Sistemas")
            print("-> 6to Semestre")

        elif opcion == "5":
            print("Generar gráfica")
        elif opcion == "6":
            break
        else:
            print("Opción inválida")
        input("Presione ENTER para continuar...")
        os.system('cls')

    
if __name__ == '__main__':
    menu()