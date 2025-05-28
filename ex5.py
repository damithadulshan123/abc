class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)  # Actually print the data
            printval = printval.next
    
    def insert_at_beginning(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

# Create the linked list
ll = LinkedList()
ll.head = Node("toyota")
l2 = Node("bmw")
l3 = Node("audi")
l4 = Node("lamborghini")

# Link the nodes
ll.head.next = l2
l2.next = l3
l3.next = l4

# Insert a new node at the beginning
ll.insert_at_beginning("ford")

# Print the linked list
ll.listprint()
