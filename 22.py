#today we will reverse a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def begin(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        else:
            new.next=self.head
            self.head =new
            
    def Show(self):
        current=self.head
        count=0
        while(current):
            print(current.data)
            count+=1
            current=current.next

    def reverse(self):
        prev=None
        current=self.head
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
        
ll = Linkedlist()
ll.begin(4)
ll.begin(3)
ll.begin(2)
ll.begin(1)
ll.Show()
print("reversed")
ll.reverse()
ll.Show()
