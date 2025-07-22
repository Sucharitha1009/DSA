''' search operation where element in the node is present or not'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
    def search(self,key):
        pos=1
        current=self.head
        while current:
            if current.data==key:
                print(f"{key} found in the linked list")
                return True
            current=current.next
            pos+=1
        print(f"{key} not found in the linked list")
        return False
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
    print("3.Search")
    print("4.Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        val=int(input("enter the value to search:"))
        ll.search(val)
    elif choice=='4':
        print("Exit the operation ....")
        break
    else:
        print("Enter Only ...1/2/3")
        
