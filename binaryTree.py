# Estructura tipo árbol

from node import Node

class BinaryTree:
    root = None

def insert(tree, data):
    if tree.root is None:
        tree.root = Node()
        tree.root.data = data
    else:
        _insert_recursive(tree.root, data)


def _insert_recursive(node, data):
    if data < node.data:
        if node.left is None:
            node.left = Node()
            node.left.data = data
        else:
            _insert_recursive(node.left, data)
    else:
        if node.right is None:
            node.right = Node()
            node.right.data = data
        else:
            _insert_recursive(node.right, data)


def search(tree, data):
    route = []
    node = _search_recursive(tree.root, data, route)

    return route if node else "El elemento buscado no existe"


def _search_recursive(node, data, route):
    if node is None:
        return None

    route.append(node.data)

    if node.data == data:
        return node

    if data < node.data:
        return _search_recursive(node.left, data, route)

    return _search_recursive(node.right, data, route)


def in_order(tree):
    result = []
    _in_order_recursive(tree.root, result)
    return result


def _in_order_recursive(node, result):
    if node is not None:
        _in_order_recursive(node.left, result)
        result.append(node.data)
        _in_order_recursive(node.right, result)


def pre_order(tree):
    result = []
    _pre_order_recursive(tree.root, result)
    return result


def _pre_order_recursive(node, result):
    if node is not None:
        result.append(node.data)
        _pre_order_recursive(node.left, result)
        _pre_order_recursive(node.right, result)


def post_order(tree):
    result = []
    _post_order_recursive(tree.root, result)
    return result


def _post_order_recursive(node, result):
    if node is not None:
        _post_order_recursive(node.left, result)
        _post_order_recursive(node.right, result)
        result.append(node.data)


def node_with_two_kids(tree):
    result = []
    _node_with_two_kids_recursive(tree.root, result)
    return result


def _node_with_two_kids_recursive(node, result):
    if node is not None:
        if node.left and node.right:
            result.append(node.data)

        _node_with_two_kids_recursive(node.left, result)
        _node_with_two_kids_recursive(node.right, result)


def node_with_one_even_child(tree):
    result = []
    _node_with_one_even_child_recursive(tree.root, result)
    return result


def _node_with_one_even_child_recursive(node, result):
    if node is not None:
        if (node.left and node.left.data % 2 == 0) or (node.right and node.right.data % 2 == 0):
            result.append(node.data)

        _node_with_one_even_child_recursive(node.left, result)
        _node_with_one_even_child_recursive(node.right, result)


def sum_children(tree):
    result = []
    _sum_children_recursive(tree.root, result)
    return result


def _sum_children_recursive(node, result):
    if node is not None:
        result.append((node.left.data if node.left else 0) + (node.right.data if node.right else 0))
        _sum_children_recursive(node.left, result)
        _sum_children_recursive(node.right, result)