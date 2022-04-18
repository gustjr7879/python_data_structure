

class BinNode():
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
class INode(BinNode):
    def __init__(self,data):
        super().__init__(data)
class LNode(BinNode):
    def __init__(self,data):
        super().__init__(data)
class BinaraySearchTree():
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root = self.insert_value(self.root,data)
        return self.root is not None
    def insert_value(self,node,data):
        if node is None:
            node = LNode(data) #Binnode -> Inode or LNode
        else:
            if len(data) <= len(node.data):
                node.left = self.insert_value(node.left,data)
            else:
                node.right = self.insert_value(node.right,data)
        return node
    def find(self,key):
        return self.find_value(self.root,key)
    def find_value(self,root,key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.find_value(root.left,key)
        elif key > root.data:
            return self.find_value(root.right,key)
    def inordertraversal(self):
        def _inordertraversal(root):
            if root is None:
                pass
            else:
                _inordertraversal(root.left)
                print(root.data)
                _inordertraversal(root.right)
        _inordertraversal(self.root)
    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None :
                pass
            else: 
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)
    def preorder_traversal(self):
        def _preorder_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _preorder_traversal(root.left)
                _preorder_traversal(root.right)
        _preorder_traversal(self.root)

array = ['a','aa','bananaC','apple','orange','joy__','hyunskki','qkrgustjr','parkhyunseok','iphone','macbook','graphneuralnetwork']
bst = BinaraySearchTree()
for i in array:
    bst.insert(i)
print(bst.find('bananaC'))
print(bst.find('banana'))
print('-----inorder-----')
bst.inordertraversal()
print('-----preorder-----')
bst.preorder_traversal()
print('-----postorder-----')
bst.post_order_traversal()
