
import os


def menu():
    while True: 
        print("MENU PRINCIPAL")
        print("1. Cargar Archivo")
        print("2. Mostrar elementos")
        print("3. Buscar elemento por ID y generar imagen")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
           print("Cargar Archivo")
        elif opcion == "2":
            print("Mostrar elementos")
        elif opcion == "3":
            print("Buscar elemento por ID y generar imagen")
        elif opcion == "4":
            print("Mostrar datos del estudiante")
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