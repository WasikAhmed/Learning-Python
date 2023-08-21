# Class Stack
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            self.stack.pop()
    
    def show(self):
        # self.stack.reverse()
        # print(self.stack)
        print(self.stack[::-1])
    
    def search(self, element):
        return element in self.stack

if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    for i in range(0, 21, 2):
        stack.push(i)
    stack.show()
    stack.pop()
    stack.show()
    print(stack.search(20))
    print(stack.search(18))