
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.count = 0
        self.top = None

    def pushStack(self,val):
        node = Node(val)
        if self.count == 0:
            self.top = node
        else:
            temp = self.top
            node.next = temp
            self.top = node

        self.count += 1

    def popStack(self):
        if self.count == 0:
            print("Under flow!")
        else:
            temp = self.top
            self.top = temp.next
            del(temp)
            self.count -= 1

    def stackTop(self):
        if self.top is None:
            return -1
        else:
            return self.top.val

    def display(self):
        temp = self.top
        while temp is not None:
            print (temp.val,end=" ")
            temp = temp.next


s = Stack()
s.pushStack(1)
s.pushStack(2)
k = int(input())
s.pushStack(k)
s.display()
print()
if s.stackTop() == -1:
    print("Stack is empty!")
else:
    print(s.stackTop())

print()
