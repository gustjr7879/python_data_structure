#queues -> last in first out 맨끝으로만 들어가고 처음에서만 뺀다 -> 일반적인 생활에서의 줄 !
#Notation : Enqueue(add) Dequeue(-) Front(맨앞의 값) Rear(맨뒤의 값)

#linkedqueue를 구현해보기

class Node:
    def __init__(self,value = None, pointer = None):
        self.value = value
        self.pointer = None
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def Enqueue(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count +=1
    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -=1
            return value
        else:
            print('비어있음')
    def size(self):
        return self.count
    def front(self):
        return self.head.value
    def rear(self):
        return self.tail.value
    def print_queue(self):
        node = self.head
        while node:
            print(node.value,end=' ')
            node = node.pointer
        print()
a = LinkedQueue() #큐 생성
a.Enqueue(1) # 1,2 추가
a.Enqueue(2)
a.print_queue() # 확인
print(a.size()) # 사이즈 확인
a.Enqueue(3) # 3추가
a.print_queue() # 확인
a.dequeue() # 값 제거 
a.print_queue() # 확인
a.Enqueue(4) # 4 추가
a.print_queue() # 확인
print(a.size()) # 사이즈 확인
print(a.front()) # front값 확인
print(a.rear()) #rear값 확인

