#today we will create a linked list and add elements 

class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
    
class LinkedList():
    def __init__(self):
        self.head=None

    def InBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next=self.head
            self.head = new_node
        
    def AIndex(self,data,index):
        new_node = Node(data)
        current_node = self.head
        position=0
        if position==index:
            self.InBegin(data)
        else:
            while(current_node!=None and position+1!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                new_node.next=current_node.next
                current_node.next=new_node
            else:
                print("not exist")
    
    def AtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node=self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next=new_node
    
        
    def show(self):
        current_node=self.head
        count=0
        while(current_node):
            print(f"data {count}: {current_node.data}")
            count+=1
            current_node=current_node.next



#add elements
n1=LinkedList()
n1.InBegin(10)

n1.InBegin(20)
n1.InBegin(30)

n1.AIndex(25,1)

n1.show()