class ReverseStack:
    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return len(self.item)==0

def reverse(text):
    s = ReverseStack()
    for c in text:
        s.push(c)
    revText = ""
    while not s.isEmpty():
        revText += s.pop()
    print(revText)

print(reverse("shubham"))