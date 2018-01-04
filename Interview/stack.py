class Stack():

    def __init__(self):
        self.items = []
        self.top = -1

    def isEmpty(self):
        return self.items == 0

    def size(self):
        return len(self.items)

    def push(self, value):
        self.top+=1
        self.items.append(value)

    def pop(self):
        old_top = self.top
        self.top-=1
        return self.items[old_top]


if __name__ == '__main__':
    stack = Stack()
    stack.push('Michael')
    stack.push('hello there')
    stack.push('2345r6t df')
    stack.push('blah blah')
    print stack.size()
    print stack.pop()
    print stack.pop()
    print stack.pop()