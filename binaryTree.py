# Estructura tipo arbol

from node import Node

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        route = []
        node = self._search_recursive(self.root, data, route)

        return route if node else "El elemento buscado no existe"
    
    def _search_recursive(self, node, data, route):
        if node is None:
            return None
    
        route.append(node.data)

        if node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data, route)
        
        return self._search_recursive(node.right, data, route)

    def in_order(self):
        result = []
        self._in_order_recursive(self.root, result)

        return result
    
    def _in_order_recursive(self, node, result):
        if node is not None:
            self._in_order_recursive(node.left, result)
            result.append(node.data)
            self._in_order_recursive(node.right, result)

    def pre_order(self):
        result = []
        self._pre_order_recursive(self.root, result)

        return result
    
    def _pre_order_recursive(self, node, result):
        if node is not None:
            result.append(node.data)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def post_order(self):
        result = []
        self._post_order_recursive(self.root, result)

        return result
    
    def _post_order_recursive(self, node, result):
        if node is not None:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.data)
    
    def node_with_two_kids(self):
        result = []
        self._node_with_two_kids_recursive(self.root, result)

        return result
    
    def _node_with_two_kids_recursive(self, node, result):
        if node is not None:
            if node.left and node.right:
                result.append(node.data)

            self._node_with_two_kids_recursive(node.left, result)
            self._node_with_two_kids_recursive(node.right, result)

    def node_with_one_even_child(self):
        result = []
        self._node_with_one_even_child_recursive(self.root, result)

        return result
    
    def _node_with_one_even_child_recursive(self, node, result):
        if node is not None:
            if (node.left and node.left.data % 2 == 0) or (node.right and node.right.data % 2 == 0):
                result.append(node.data)

            self._node_with_one_even_child_recursive(node.left, result)
            self._node_with_one_even_child_recursive(node.right, result)

    def sum_children(self):
        result = []
        self._sum_children_recursive(self.root, result)

        return result
    
    def _sum_children_recursive(self, node, result):
        if node is not None:
            result.append((node.left.data if node.left else 0) + (node.right.data if node.right else 0))
            
            self._sum_children_recursive(node.left, result)
            self._sum_children_recursive(node.right, result)