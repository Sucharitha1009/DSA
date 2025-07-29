class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None   
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def dab(self):
        if not self.head:
            print("can't perform delete in any empty list")
        print(f"Deleted:{self.head.data}")
        self.head=self.head.next
        if self.head:
            self.head.prev=None
    def display(self):
        temp=self.head
        print("Doubly Linked List:")
        while temp:
            print(temp.data,end="<-->")
            temp=temp.next
        print("None")
        
dll=DoublyLinkedList()
n=int(input("enter no of elements to insert at end:"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iae(val)
dll.display()
d=int(input("\n how many times do you want to perform delete operation:"))
for _ in range(d):
    dll.dab()
    dll.display()
