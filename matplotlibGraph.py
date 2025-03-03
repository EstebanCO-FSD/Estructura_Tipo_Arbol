# Gráfico de la estructura tipo árbol

import matplotlib.pyplot as plt
from binaryTree import BinaryTree

# Función para graficar el árbol
def plot_tree(tree):
    if not tree.root:
        print("El árbol está vacío.")
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_axis_off()

    # Llamamos a la función recursiva para dibujar el árbol
    _plot_recursive(ax, tree.root, 0, 0, 100, 50)

    plt.draw()
    plt.pause(0.001)
    plt.show()

# Función recursiva para dibujar nodos y conexiones
def _plot_recursive(ax, node, x, y, x_offset, y_offset):
    if node is None:
        return

    # Dibujar nodo
    ax.text(x, y, str(node.data), fontsize=12, ha='center', va='center',
            bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='circle'))

    # Conectar con hijo izquierdo
    if node.left:
        ax.plot([x, x - x_offset], [y - 5, y - y_offset], 'k-')
        _plot_recursive(ax, node.left, x - x_offset, y - y_offset, x_offset / 1.5, y_offset)

    # Conectar con hijo derecho
    if node.right:
        ax.plot([x, x + x_offset], [y - 5, y - y_offset], 'k-')
        _plot_recursive(ax, node.right, x + x_offset, y - y_offset, x_offset / 1.5, y_offset)