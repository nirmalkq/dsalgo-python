#Single node of singly linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

#insert method for linked list
    def insert(self,data):
        newNode = Node(data)
        if(self.head):
            current =self.head
            while(current.next):
                current =current.next
            current.next=newNode
        else:
            self.head =newNode

# Print method for linkedlist
    def printLinkedList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

# Creating a single node
ll = LinkedList()
# ll.head = Node(3)
# print(ll.head.data)
# first = Node(3)
# print(first.data)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.printLinkedList()
