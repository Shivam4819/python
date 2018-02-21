
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
    def swap_node(self):
        count = 1
        temp = self.start
        temp1 = self.start
        num1 = int(input("enter first node to be swapped"))
        num2 = int(input("enter second node to be swapped"))
        while (count < num1 - 1):
            temp = temp.next
            count +=1
        count = 1
        while (count < num2 - 1):
            temp1 = temp1.next
            count +=1
        a=[]
        a[0] = temp.next
        a[1] = temp.next.next
        a[2] = temp1.next
        a[3] = temp1.next.next
        temp.next.next = a[3]
        temp1.next.next = a[1]
        temp.next = a[2]
        temp1.next = a[0]

    def swapNodes(self ):

        x=int(input("enter the first node:-"))
        y=int(input("enter the second node:-"))
        if x == y:
            return
        temp1 = self.start
        temp=None
        while temp1.data != x:
            temp = temp1
            temp1 = temp1.next

        temp3 = self.start
        temp2 = None
        while temp3.data != y:
            temp2 = temp3
            temp3 = temp3.next
        if temp != None:
            temp.next = temp3
        else:
            self.start = temp3
        if temp2 != None:
            temp2.next = temp1
        else:
            self.start = temp1
        temp5 = temp1.next
        temp1.next = temp3.next
        temp3.next = temp5


l = Linklist()
count=int(input("enter the total no of node"))
for i in range(count):
    new_data = int(input("enter the data-"))
    l.addnode(new_data)
l.display()
l.swapNodes()
l.display()

