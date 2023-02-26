'''#CREATING NODE DECLARATION AND DEFINITION
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp  = first node
            while temp:
                print(temp.data,"->",end=" ")
                #tempdata means first node's data
                temp=temp.next #establishing link
obj=singlelinkedlist()
#node creation - initialization
n=Node(10)  #so n.data in node class will be 10
obj.head=n  #assigning first node as head
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display() '''


'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data, "->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("w")
obj.head=n
n1=Node("i")
n.next=n1
n2=Node("n")
n1.next=n2
n3=Node("n")
n2.next=n3
n4=Node("e")
n3.next=n4
n5=Node("r")
n4.next=n5
obj.display() '''

'''#inserting at beginning
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("befire inserting 100")
obj.display()
print(" ")
print("after inserting 100")
obj.insert_beginning(100)
obj.display()
print(" ")
print("after inserting 555")
obj.insert_beginning(555)
obj.display() '''

'''#inserting at end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp  = first node
            while temp:
                print(temp.data,"->",end=" ")
                #tempdata means first node's data
                temp=temp.next #establishing link
obj=singlelinkedlist()
#node creation - initialization
n=Node(10)  #so n.data in node class will be 10
obj.head=n  #assigning first node as head
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.insert_end(1111)
obj.display()  '''

'''#inserting at given position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
            #np.data=data         not required
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp  = first node
            while temp:
                print(temp.data,"->",end=" ")
                #tempdata means first node's data
                temp=temp.next #establishing link
obj=singlelinkedlist()
n=Node(10)  
obj.head=n  
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.insert_position(3,100)
obj.display() '''

#single linked list creation using user input
class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def append(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
a_llist = LinkedList()
n = int(input('how many elements would you like to enter'))
for i in range(n):
    data = int(input('enter data item'))
    a_llist.append(data)
print('the linked list:',end = ' ')
a_llist.display()
            
        
