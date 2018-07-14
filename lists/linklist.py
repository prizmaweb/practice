class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
        self.length=0

    def append(self, val):
        curr=self.head
        self.length +=1
        if curr ==None:
            self.head=Node(val)
            return
        while curr != None:
            prev=curr
            curr=curr.next
        prev.next=Node(val) 
        prev.next.next=None
            
    def insertAt(self,index,val):
        if (self.length < index):
            raise IndexError()
        curr=self.head
        counter=0
        while counter < index :
            counter+=1
            curr=curr.next
        nextval=curr.next 
        curr.next=Node(val)
        curr.next.next=nextval
        self.length +=1
         
if __name__ == "__main__":
    l= LinkList()
    l.append(4)
    l.append(3)
    l.append(2)
    l.insertAt(0,100)
    l.insertAt(1,101)
    l.insertAt(5,101)
    curr=l.head
    for i in range(l.length):
        print str(curr.value)
        curr=curr.next
 
