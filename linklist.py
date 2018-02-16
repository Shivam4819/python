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

    def addnode_start(self,data):
        if self.start is None:
            print("list is empty")
        else:
            new_node = Nodes(data)
            new_node.next = self.start
            self.start = new_node

    def add_in_middle(self,data):
        new_node = Nodes(data)
        a = int(input("enter place after which you want to enter:-"))
        temp = self.start
        count = 0
        while count < a:
            temp1 = temp
            temp = temp.next
            count = count+1
        new_node.next = temp
        temp1.next = new_node

    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def search(self):
        nums = int(input("enter the data to be searched:-"))
        temp = self.start
        while temp.data is not nums:
            temp = temp.next
        if temp.data is nums:
            print("data found:- ",temp.data)
        else :
            print("data not present")

    def delete_element(self):
        nums = int(input("Enter the data to be deleted:-"))
        temp = self.start
        if self.start.data is nums:
            self.start = temp.next
            temp.next=None
            del temp
        else:
            while temp.data is not nums:
                temp1 = temp
                temp = temp.next
            temp1.next = temp.next
            temp.next = None
            del temp


l = Linklist()
choice=1
print("menu")
print("1)add node")
print("2)display")
print("3)add in middle")
print("4)delete element")
print("5)search")
print("6)exit")

while choice!=6:
    choice=int(input("enter choice-"))
    if choice==1:
        new_data=int(input("enter the data-"))
        l.addnode(new_data)
    elif choice==2:
        l.display()
    elif choice==3:
        new_data = int(input("enter the data-"))
        l.add_in_middle(new_data)
    elif choice == 4:
        l.delete_element()
    elif choice == 5:
        l.search()
    else:
        print("wrong buddy")