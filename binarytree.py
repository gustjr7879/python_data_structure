'''
(task 1) BinNode interface를 구현하세요.
(task 2) BinNode를 상속하여 INode를 구현하세요. INode는 값, 왼쪽 자식 포인터, 오른쪽 자식 포인터를 가집니다.
(task 3) 구현한 BinNode와 INode를 이용하여 본인이 좋아하는 10자 이상의 영어 단어 혹은 구의 글자들로 tree를 구성하세요. tree의 모양은 너무 단조롭지만 않으면 아무렇게나 구성해도 좋습니다. 단, root에서부터 inorder traversal 을 수행하였을 때, 문구가 올바르게 출력되도록 구성하세요.
(task 4) preorder, inorder, postorder traversal을 수행하는 함수를 구현하고, 함수를 수행한 결과를 확인하세요.
(task 5) BinNode를 상속하여 LNode를 구현하세요. LNode는 양쪽 자식이 모두 없는 Leaf node만을 위한 구현입니다.
(task 6) task 3에서 구현한 tree에서 leaf node를 기존 INode에서 LNode로 교체하고, task 5를 수행하여 기존 결과와 동일함을 확인하세요.

위 task를 모두 수행하고, 각 task의 코드와 결과를 정리하여 "result.pdf" 파일로 제출하세요.
또한, 구현한 모든 코드를 압축하여 "result.zip" 파일로 제출하세요.
'''

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