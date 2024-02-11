# balancing a tree
def main():
    tree = Tree()
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for element in elements:
        tree.insert(element)
    tree.print_tree()
    print("Longest Path")
    print(tree.longest_path())
    if tree.is_balanced():
        print("Tree is balanced")
    else:
        print("Tree is not balanced")

    tree.balance()

    print("Balanced Tree")
    tree.print_tree()
    print("Longest Path")
    print(tree.longest_path())
    if tree.is_balanced():
        print("Tree is balanced")
    else:
        print("Tree is not balanced")

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def in_order(self, elements):
        if self.left:
            self.left.in_order(elements)
        elements.append(self.data)
        if self.right:
            self.right.in_order(elements)

    def print_node(self):
        if self.left:
            self.left.print_node()
        print(self.data)
        if self.right:
            self.right.print_node()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def print_tree(self):
        if self.root is not None:
            self.root.print_node()


    def balance(self):
        elements = self.in_order()
        self.root = self.build_tree(elements)

    def in_order(self):
        elements = []
        self.root.in_order(elements)
        return elements

    def build_tree(self, elements):
        if not elements:
            return None
        mid = len(elements) // 2
        root = Node(elements[mid])
        root.left = self.build_tree(elements[:mid])
        root.right = self.build_tree(elements[mid+1:])
        return root


    def longest_path(self):
        return self._longest_path(self.root)

    def _longest_path(self, node):
        if node is None:
            return 0
        return 1 + max(self._longest_path(node.left), self._longest_path(node.right))


    def is_balanced(self):
        return self._is_balanced(self.root)


    def _is_balanced(self, node):
        if node is None:
            return True
        left = self._longest_path(node.left)
        right = self._longest_path(node.right)
        return abs(left - right) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right)


if __name__ == "__main__":
    main()