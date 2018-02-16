class Nodes:
    def __init__(self, data1):
        self.data = data1
        self.next = None


class quque:
    def __init__(self):
        self.start = None

    def enque(self, data):
        new_node = Nodes(data)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            temp.next = new_node


    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def deque(self):
        temp = self.start
        print(self.start.data)
        self.start=temp.next
        temp.next=None
        del temp

l = quque()
choice=1
print("menu")
print("1)enque")
print("2)display")
print("3)deque")
print("4)exit")
while choice!=4:
    choice=int(input("enter choice-"))
    if choice==1:
        new_data=int(input("enter the data-"))
        l.enque(new_data)
    elif choice==2:
        l.display()
    elif choice==3:
        l.deque()
    else:
        print("wrong buddy")