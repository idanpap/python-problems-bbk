# 1.
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            top_node = self.top
            self.top = self.top.next
            top_node.next = None
            return top_node.data

    def peek(self):
        return self.top.data

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

# 2.


class Stack:
    def __init__(self):
        self.top = []

    def push(self, x):
        if x == '(' or x == '[' or x == '{' or x == '<':
            self.top.append(x)
        else:
            if self.peek() == '(':
                if x == ')':
                    self.pop()
            elif self.peek() == '[':
                if x == ']':
                    self.pop()
            elif self.peek() == '{':
                if x == '}':
                    self.pop()
            elif self.peek() == '<':
                if x == '>':
                    self.pop()
            else:
                return False

    def pop(self):
        return self.top.pop()

    def peek(self):
        return self.top[len(self.top)-1]

    def is_empty(self):
        if self.top == []:
            return True
        else:
            return False


X = str(input())
stack01 = Stack()
for x in X:
    stack01.push(x)
print(stack01.is_empty())
