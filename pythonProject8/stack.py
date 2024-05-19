class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:", stack.items)
    print("Size of stack:", stack.size())
    print("Peek:", stack.peek())

    popped_item = stack.pop()
    print("Popped item:", popped_item)
    print("Stack after pop:", stack.items)
    print("Size of stack after pop:", stack.size())
