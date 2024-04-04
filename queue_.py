class Queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.queue = [0 for _ in range(self.size)]
    
    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled.')
    
    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty.')
    # 判断队空
    def is_empty(self):
        return self.front == self.rear
    # 判断队满
    def is_filled(self):
        return self.front == (self.rear + 1) % self.size

queue1 = Queue(5)
for i in range(4): # size = 5, 只能装4个数
    queue1.push(i)
queue1.pop()
queue1.push(5)
queue1.push(6)