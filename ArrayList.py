#ArrayList 생성자 

class ArrayList():
    def __init__(self,defaultsize,listsize,data):
        self.defaultsize = defaultsize
        self.listsize = listsize
        self.data = data
    def clear(self):
        self.listsize = 0
        
        if self.listsize == 0:
            self.data = []
        print(self.data)
    def update(self,pos,value):
        self.pos = pos
        self.value = value
        self.data[pos] = value
        print(self.data)
    def getValue(self,pos):
        print(self.data[pos])
    def length(self):
        print(self.listsize)
    def append(self,value):
        self.value = value
        self.listsize += 1
        self.data.append(value)
        print(self.data)
    def insert(self,pos,value):
        self.pos = pos
        self.value = value
        self.data.append(0)
        for i in range(pos+1,self.listsize):
            self.data[i+1] = self.data[i]
            self.data[i] = self.data[i-1]     
        self.listsize +=1
        self.data[pos] = value
        print(self.data)
    def remove(self,pos):
        self.pos = pos
        for i in range(pos,self.listsize-1):
            self.data[i] = self.data[i+1]
        del self.data[self.listsize-1]
        self.listsize -= 1
        if self.listsize == 0:
            self.data = []
        print(self.data)
a = ArrayList(10,0,[])
a.append(1)
a.append(2)
a.clear()
a.append(1)
a.append(2)
a.append(3)
a.update(0,3)
a.getValue(0)
a.length()
a.insert(1,4)
a.remove(0)