from typing import List


class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop(len(self.data) - 1)

    def top(self):
        return self.data[len(self.data) - 1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'[{", ".join(self.data[::-1])}]'


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))
print(stack.pop())
print(stack.top())
stack.push("cucumber")
print(str(stack))
print(stack.is_empty())
print(stack.is_empty())