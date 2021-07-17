class Stack:
    """Methods that perform various stack operations"""

    def __init__(self):
        """Initialize the stack"""
        self.stack = []

    def is_empty(self):
        """Check if the stack is empty"""
        return self.stack == []

    def push(self, item):
        """Push an item onto the stack"""
        self.stack.append(item)

    def pop(self):
        """Pop the last item off the stack and return it"""
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def peek(self):
        """Return the last element of the list"""
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        """Return the size of the list"""
        return len(self.stack)


class Queue:
    """Methods that perform various Queue operations"""

    def __init__(self):
        """Initialize the queue"""
        self.queue = []

    def is_empty(self):
        """Check if the queue is empty"""
        return self.queue == []

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the first element of the list"""
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        """Return the size of the list"""
        return len(self.queue)


class Node:
    """Method that creates a node"""

    def __init__(self, data):
        """Initialize the node"""
        self.data = data
        self.next = None


class LinkedList:
    """Methods that perform various operations on Linked List using Node class"""

    def __init__(self):
        """Initialize the list"""
        self.head = None

    def is_empty(self):
        """Check if the list is empty"""
        return self.head == None

    def add_first(self, data):
        """Add an item to the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        """Add an item to the end of the list"""
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def add_in_between(self, data, prev_node, next_node):
        """Add an item to the middle of the list"""
        new_node = Node(data)
        new_node.next = next_node
        prev_node.next = new_node

    def remove_first(self):
        """Remove and return the first element of the list"""
        if self.is_empty():
            return None
        else:
            self.head = self.head.next

    def remove_last(self):
        """Remove and return the last element of the list"""
        if self.is_empty():
            return None
        else:
            current = self.head
            prev = None
            while current.next != None:
                prev = current
                current = current.next
            prev.next = None

    def remove_in_between(self, prev_node, next_node):
        """Remove and return the middle element of the list"""
        if self.is_empty():
            return None
        else:
            prev_node.next = next_node

    def print_list(self):
        """Print the list"""
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next
