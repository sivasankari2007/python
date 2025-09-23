class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
bst = BST()
root = None
for key in [50, 30, 70, 20, 40, 60, 80]:
    root = bst.insert(root, key)
print("Inorder traversal of the BST:")
bst.inorder(root)
print()
key = 40
found = bst.search(root, key)
print(f"Search {key}: {'Found' if found else 'Not Found'}")
root = bst.delete(root, 30)
print("Inorder traversal after deleting 30:")
bst.inorder(root)
print()
total_nodes = bst.countNodes(root)
print(f"Total nodes in BST: {total_nodes}")
