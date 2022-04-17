'''
ArrayList와 LinkedList를 구현하여 제출하세요.

1) ListIterator를 포함하여 Doubly Linked List를 구현하세요. (DList.java)

2) Array를 사용하여 Stack을 구현하세요. (ArrayStack.java 파일로 제출)

3) Link를 사용하여 Queue를 구현하세요. (LinkedQueue.java 파일로 제출)

(Bonus: 점수반영안됨) Circular Queue를 구현해보세요. 

각각의 구현을 코드를 작성하여 (예: TestAll.java), 본인이 작성한 자료구조가 올바르게 작동하는지 테스트 해보세요. 테스트 코드와 테스트 결과를 result.pdf파일로 간단히 정리하여 제출하세요.

'''
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        return
class DoubleLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    
    def add(self, data):
        new = Node(data)
        new.prev = self.tail
        self.tail.next = new
        self.tail = new
    def delete(self, data):
        if self.head == '':
            return False
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        node = self.head
        while node.next:
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next
                node.next.prev = node
                del temp
                return True
            node = node.next
        return False
    def display(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def get_len(self):
        node = self.head
        count = 0
        while node:
            node = node.next
            count += 1
        print(count)
        return count
    def insert(self, n, data): #n = 위치
        if n == 0: 
            self.add(data)
            return True
        elif n == self.get_len()-1:
            self.add(data)
            return True
        else:
            node = self.head.next
            count = 1
            while node.next and count < n:
                count += 1
                node = node.next
            if count < n:
                return False
            new = Node(data)
            new.next = node.next
            node.next.prev = new
            node.next = new
            new.prev = node
            return True
a = DoubleLinkedList(1)
a.add(2) #add
a.add(3) #add
a.display() #iterator
a.delete(2) #delete
a.display() #iterator
b = a.get_len() #갯수 출력
a.insert(1,4) #insert 1위치 4데이터
a.display() #iterator