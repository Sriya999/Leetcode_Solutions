class MyQueue:

    def __init__(self):
        self.s1=[]#two stacks
        self.s2=[]

    def push(self, x: int) -> None:
        #copy s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        #insert data
        self.s1.append(x)
        #copy back s2 to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
