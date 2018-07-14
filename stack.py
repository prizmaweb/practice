class Node:
    def __init__(self,val):
        self.value=val
        self.next=None


class Stack:
    def __init__(self):
        self.top=None

    def push(self,node):
        node.next=self.top
        self.top=node

    def pop(self):
        curr=self.top
        if curr == None:
            raise StopIteration()
        self.top=self.top.next
        return curr
        
if __name__ == "__main__":
    s= Stack()
    a=Node(5)
    b=Node(10)
    c=Node(14)
    s.push(a)
    s.push(b)
    s.push(c)
    x=s.pop()
    yx=s.pop()
    print x.value
