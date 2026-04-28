class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)

    if (head == None):
        head = newNode
    else:
        newNode.next = head
        head = newNode


def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)

    if (head == None):
        head = newNode
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = newNode


def insertNodeAfterGivenNode(data, node):
    global head
    newNode = Node(data)

    if (head == None):
        head = newNode
    else:
        current = head
        prev = None

        while (prev == None or prev.data != node):
            prev = current
            current = current.next

            if (current == None):
                print('The node does not exist')
                return

        newNode.next = current
        prev.next = newNode


def traverseLinkedList():
    current = head
    while (current):
        print(current.data, end=" -> ")
        current = current.next
    print("None")


#Main Program
node1 = Node('Buksan mo by Willie Revillame')
print(node1.data)
print()

head = node1

insertNodeAtTheBeginning('Ale by The Bloomfields')
insertNodeAtTheBeginning('Mundo by IV of Spades')
insertNodeAtTheBeginning('Dati by Sam Concepcion')

traverseLinkedList()
print()

insertNodeAtTheEnd('Kahit Ayaw Mo Na by This Band')
insertNodeAtTheEnd('Paraluman by Adie')

traverseLinkedList()
print()

insertNodeAfterGivenNode('Ikaw at Ako by Moira', 'Ale by The Bloomfields')
insertNodeAfterGivenNode('Ere by Eraserheads', 'Mundo by IV of Spades')
traverseLinkedList()
