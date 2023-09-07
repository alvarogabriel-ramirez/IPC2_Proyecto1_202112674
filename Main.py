import xml.etree.ElementTree as ET

import os
from Senal import Senal
from Dato import Item
from ListaSenal import ListaSenal
import os

senales = ListaSenal()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

def carga_datos(ruta):

    if not os.path.isfile(ruta):
        print("El archivo no existe")
        return

    if not ruta.endswith(".xml"):
        print("El archivo debe ser .xml")
        return
    tree = ET.parse(ruta)
    root = tree.getroot()
    
    for senal in root.findall('senal'):
        nombre = senal.get('nombre')
        tiempo = int(senal.get('t'))
        amplitud = int(senal.get('A'))
        senal_nueva = Senal(nombre,tiempo,amplitud)

    # for dato in senal.findall('dato'):
    #     t = int(dato.get('t'))
    #     A = int(dato.get('A'))
    #     text = dato.text
        
    #     if int(text) > 0:
    #         text = "1"
    #     else:
    #         text = "0"
    #     dato_nuevo = Item(t, A, text)
    #     senal_nueva.items.insertar(dato_nuevo)
    #     senales.insertarOrdenadoNombre(senal_nueva)

        for dato in senal.findall('dato'):
            t = int(dato.get('t'))
            A = int(dato.get('A'))
            text = dato.text
            dato_nuevo = Item(t,A,text)
            senal_nueva.items.insertar(dato_nuevo)
        
        senales.insertar(senal_nueva)
        
    print("** Datos cargados correctamente **")

def graficar(senal):
    dot_string = 'digraph G {\n'
    dot_string += senal.to_dot()
    dot_string += "}\n"
    with open("matriz.dot", "w") as archivo:
        archivo.write(dot_string)
    os.system("dot -Tpng matriz.dot -o matriz.png")
    print("¡Gráfica generada!")


def menu():
    while True: 
        print("MENU PRINCIPAL")
        print("_"*60)
        print("1. Cargar Archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Inicializar Sistema")    
        print("7. Salida")

        opcion = input("Ingrese una opción: ")
        if   opcion == "1":
            clear()
            print("_"*60 )
            print("Cargar Archivo")
            print("-"*60 )
            global ruta 
            ruta = input("> Ingrese la ruta del archivo:")
            carga_datos(ruta)
            #senales.mostrar()
        
        elif opcion == "2":
            clear()
            print("_"*60 )
            print("Procesar archivo")
            print("-"*60 )

        elif opcion == "3":
            clear()
            print("_"*60 )
            print("Escribir archivo salida")
            senales.escribirXML()
            print("-"*60 )

        elif opcion == "4":
            clear()
            print("_"*60 + "\n")
            print("Mostrar datos del estudiante")
            print("-> Alvaro Gabriel Ramirez Alvarez")
            print("-> 202112674")
            print("-> Introducción a la Programación y Computación 2 A")
            print("-> Ingeniería en Ciencias y Sistemas")
            print("-> 6to Semestre")
            print("-"*60)

        elif opcion == "5":
            clear()
            print("_"*60 )
            print("Generar gráfica")
            print("-"*60 )
            senales.mostrar()
            nombre = input("> Ingrese el nombre de la señal:")
            Senal = senales.buscar_por_nombre(nombre)
            if Senal:
                graficar(Senal)
            else:
                print(f"La Señal {nombre} no existe")

        elif opcion == "6":
            clear()
            print(" ¡ INICIALIZADO CORRECTAMENTE !")
            senales.inicializar()

        elif opcion == "7":
            break
        else:
            print("*** Opción inválida ***")
        input("Presione ENTER para continuar...")
        clear()

if __name__ == '__main__':
    menu()