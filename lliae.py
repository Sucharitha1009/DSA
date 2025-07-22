#Linked List insertion at ending
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(f"{data} inserted at end / will be first node")
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
        print(f"{data} inserted at last")
    def display(self):
        current=self.head
        if not current:
            print("LinkedList Empty")
            return 
        while current:
            print(current.data,end="---")
            current=current.next
        print("None")
        
ll=LinkedList()
while True:
    print("\n LinkedList- Insert At Begin...")
    print("1.Insert")
    print("2.Display")
    print("3.Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        print("Exit the operation ....")
        break
    else:
        print("Enter Only ...1/2/3")
        
