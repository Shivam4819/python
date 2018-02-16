class Nodes:
    def __init__(self, data1):
        self.data = data1
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Nodes(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def popped(self):
     temp = self.top
     print(self.top.data)
     self.top=temp.next
     temp.next=None
     del temp

l = stack()
choice=1
print("menu")
print("1)push")
print("2)display")
print("3)pop")
print("4)exit")
while choice!=4:
    choice=int(input("enter choice-"))
    if choice==1:
        new_data=int(input("enter the data-"))
        l.addnode(new_data)
    elif choice==2:
        l.display()
    elif choice==3:
        l.delete_element()
    else:
        print("wrong buddy")