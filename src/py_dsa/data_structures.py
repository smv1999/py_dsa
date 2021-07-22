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

    def reverse_list(self):
        """Reverses the list"""
        if self.is_empty():
            return None
        else:
            current = self.head
            prev = None
            while current != None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev


class TreeNode:
    """Method that creates a Tree Node"""

    def __init__(self, data):
        """Initialize the node"""
        self.data = data
        self.left = None
        self.right = None


class Tree:
    """Methods that perform various operations on Binary Tree using Tree Node"""

    def __init__(self):
        """Initialize the tree"""
        self.root = None

    def is_empty(self):
        """Check if the tree is empty"""
        return self.root == None

    def add(self, data):
        """Add an item to the binary tree"""
        if self.is_empty():
            self.root = TreeNode(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(data)
                        break
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(data)
                        break
                else:
                    break

    def height(self):
        """Return the height of the tree"""
        if self.is_empty():
            return 0
        else:
            return self.__height_node(self.root)

    def __height_node(self, node):
        """Return the height of the node"""
        if node == None:
            return 0
        else:
            return max(self.__height_node(node.left), self.__height_node(node.right)) + 1

    def search(self, data):
        """Search for an item in the tree"""
        if self.is_empty():
            return False
        else:
            current = self.root
            while current != None:
                if data < current.data:
                    current = current.left
                elif data > current.data:
                    current = current.right
                else:
                    return True
            return False

    def remove(self, data):
        """Delete an item from the binary tree"""
        if self.is_empty():
            return
        else:
            self.__remove_node(self.root, data)

    def __remove_node(self, node, data):
        """Delete the node"""
        if node == None:
            return
        else:
            if data < node.data:

                node.left = self.__remove_node(node.left, data)
            elif data > node.data:
                node.right = self.__remove_node(node.right, data)
            else:
                if node.left == None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right == None:
                    temp = node.left
                    node = None
                    return temp
                temp = self.__min_value_node(node.right)
                node.data = temp.data
                node.right = self.__remove_node(node.right, temp.data)
            return node

    def invert_tree(self):
        """Invert the tree"""
        if self.is_empty():
            return None
        else:
            self.__invert_tree(self.root)

    def __invert_tree(self, node):
        """Invert the tree"""
        if node == None:
            return
        else:
            node.left, node.right = node.right, node.left
            self.__invert_tree(node.left)
            self.__invert_tree(node.right)

    def __min_value_node(self, node):
        """Return the minimum value node"""
        while node.left != None:
            node = node.left
        return node

    def print_tree(self, traversal='inorder'):
        """Prints the tree in in-order by default.
           Takes an optional argument traversal to print in preorder or postorder 
        """
        if self.is_empty():
            print("Tree is empty")
        else:
            current = self.root
            self.__print_node(current, traversal)

    def __print_node(self, node, traversal):
        """Print the node"""
        if node == None:
            return
        else:
            if traversal == 'inorder':
                self.__inorder_traversal(self.root)
            elif traversal == 'preorder':
                self.__preorder_traversal(self.root)
            else:
                self.__postorder_traversal(self.root)

    def __inorder_traversal(self, node):
        """Inorder traversal of the tree"""
        if node == None:
            return
        else:
            self.__inorder_traversal(node.left)
            print(node.data)
            self.__inorder_traversal(node.right)

    def __preorder_traversal(self, node):
        """Preorder traversal"""
        if node == None:
            return
        else:
            print(node.data)
            self.__preorder_traversal(node.left)
            self.__preorder_traversal(node.right)

    def __postorder_traversal(self, node):
        """Postorder traversal"""
        if node == None:
            return
        else:
            self.__postorder_traversal(node.left)
            self.__postorder_traversal(node.right)
            print(node.data)


class Graph:
    """Methods that perform various operations on Graph"""

    def __init__(self):
        """Initialize the graph"""
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge to the graph"""
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

    def remove_vertex(self, vertex):
        """Remove a vertex from the graph"""
        if vertex in self.graph:
            del self.graph[vertex]
            for key in self.graph:
                if vertex in self.graph[key]:
                    self.graph[key].remove(vertex)

    def remove_edge(self, vertex1, vertex2):
        """Remove an edge from the graph"""
        if vertex1 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)

    def print_graph(self):
        """Print the graph"""
        for key in self.graph:
            print(key, ":", self.graph[key])

    def breadth_first_search(self, start):
        """Breadth first search"""
        visited = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(self.graph[vertex])
        return visited

    def depth_first_search(self, node, visited=[]):
        """Depth first search"""
        if node not in visited:
            visited.append(node)
            for i in self.graph[node]:
                self.depth_first_search(i, visited)
        return visited
