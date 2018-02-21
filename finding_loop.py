
class Nodes:
    def __init__(self, data1):
        self.data = data1
        self.next = None


class Linklist:
    def __init__(self):
        self.start = None

    def addnode(self, data):
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

    def check_loop(self):
        r=set()
        temp=self.start
        while temp:
            if temp in r:
                return True
            else:
                r.add(temp)
            temp=temp.next


l = Linklist()
count=int(input("enter the total no of node"))
for i in range(count):
    new_data = int(input("enter the data-"))
    l.addnode(new_data)
l.display()

l.start.next.next.next.next.next=l.start.next
if l.check_loop():
    print("loop found")
else:
    print("not found")