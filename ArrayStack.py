#list 의 제한된 형태 리스트의 한쪽 끝에서만 insert/delete
#last in first out
#Notation : PUSH POP TOP

#구현해볼 것 clear, push pop topvalue len 

import numpy as np

class Stack:
    def __init__(self,data):
        self.arr = np.array(data)
        return
    def push(self,value):
        self.arr = np.append(self.arr,value)
        return
    def len(self):
        self.size = len(self.arr)
        return self.size
    def pop(self):
        self.arr = self.arr[0:self.size-1]
        return
    def print_stack(self):
        print(self.arr)
    def clear(self):
        self.arr = np.array([])
    def top_value(self):
        value = self.arr[-1]
        return value
a = Stack(0) # 스택 생성 및 초기값 설정
a.push(1) # 1추가
a.push(2) # 2추가
a.push(3) # 3추가
a.print_stack() #확인
print(a.len()) # 사이즈 확인
a.pop() # pop진행
a.print_stack() # 확인
print(a.top_value()) # topvalue확인
a.clear() # clear
a.print_stack() # 아무것도 없음을 확인