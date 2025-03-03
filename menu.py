# Menú con los puntos señalados en la actividad

from binaryTree import BinaryTree
from matplotlibGraph import plot_tree
from binaryTree import (
    insert, search, in_order, pre_order, post_order,
    node_with_two_kids, node_with_one_even_child, sum_children
)

tree = BinaryTree()

def addElements():
    while True:
        try:
            num = int(input("Ingrese un número (o 'n' para salir): "))
            insert(tree, num)
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
    print(f"In-order: {in_order(tree)}")
    print(f"Pre-order: {pre_order(tree)}")
    print(f"Post-order: {post_order(tree)}")

    plot_tree(tree)

def showElementsWithChildren():
    print("\nResultados\n")
    print(f"Elementos o Nodos con 2 hijos: {node_with_two_kids(tree)}")
    print(f"Elementos con 1 hijo par: {node_with_one_even_child(tree)}")
    print(f"Suma de hijos de cada nodo: {sum_children(tree)}")

def searchElement():
    num = int(input("Ingrese el elemento o nodo a buscar: "))
    result = search(tree, num)

    if isinstance(result, list):
        print(f"Elemento o nodo {num} encontrado!")
        print(f"Recorrido: {result}")
    else:
        print(result)

def menu():
    while True:
        print("\n// Actividad Evaluativa (Estructuras tipo árbol) //\n")
        print("Opciones\n")
        print("1. Añadir elementos")
        print("2. Ver recorridos (in-order, pre-order y post-order)")
        print("3. Mostrar elementos con (2 Hijos, 1 Hijo par y Suma de hijos)")
        print("4. Buscar elemento")
        print("\n5. Salir")

        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("Opción inválida. Intente de nuevo.")
            continue

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