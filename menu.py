# Menu con los puntos señalados en la actividad

from binaryTree import BinaryTree
from matplotlibGraph import BinaryTreePlot

tree = BinaryTree()

def addElements():
    while True:
        try:
            num = int(input("Ingrese un numero (o 'n' para salir): "))

            tree.insert(num)
        except ValueError:
            resp = input("¿Desea salir? (s/n): ").strip().lower()

            if resp == "s":
                break
            elif resp == "n":
                addElements()
                break
            else:
                print("Opción inválida. Intente de nuevo.")

def showOrders():
    print("\nRecorridos\n")
    print(f"In-order: {tree.in_order()}")
    print(f"Pre-order: {tree.pre_order()}")
    print(f"Post-order: {tree.post_order()}")

    treePlot = BinaryTreePlot()
    treePlot.root = tree.root
    treePlot.plot_tree()

def showElementsWithChildren():
    print("\nResultados\n")
    print(f"Elementos o Nodos con 2 hijos: {tree.node_with_two_kids()}")
    print(f"Elementos con 1 hijo par: {tree.node_with_one_even_child()}")
    print(f"Suma de hijos de cada nodo: {tree.sum_children()}")

def searchElement():
    num = int(input("Ingrese el elemento o nodo a buscar: "))

    result = tree.search(num)

    if isinstance(result, list):
        print(f"Elemento o nodo {num} encontrado!")
        print(f"Recorrido: {result}")
    else:
        print(result)

def menu():
    while True:
        print("\n// Actividad Evaluativa (Estructuras tipo arbol) //\n")

        print("Opciones\n")
        print("1. Añadir elementos")
        print("2. Ver recorridos (in-order, pre-order y post-order)")
        print("3. Mostrar elementos con (2 Hijos, 1 Hijo par y Suma de hijos)")
        print("4. Buscar elemento")

        print("\n5. Salir")

        opcion = int(input("\nElige una opcion: "))

        if opcion == 1:
            addElements()
        elif opcion == 2:
            showOrders()
        elif opcion == 3:
            showElementsWithChildren()
        elif opcion == 4:
            searchElement()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()