class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node("Bakit ba ikaw ang siyang iniisip ko")
print(node1.data)


head = node1


def insertNodeAtTheBeginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head


head = insertNodeAtTheBeginning(head, "Ako'y alipin mo kahit hindi batid")
head = insertNodeAtTheBeginning(head, "Araw-gabi nasa isip ka")


def traverseLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


def insertNodeAtTheEnd(head, data):
    new_node = Node(data)
    
    if head is None:
        return new_node
    
    temp = head
    while temp.next is not None:
        temp = temp.next
    
    temp.next = new_node
    return head


head = insertNodeAtTheEnd(head, "Di ko mapigilan ang damdamin ko")
head = insertNodeAtTheEnd(head, "Sana'y mapansin mo ang puso ko")

print("\nAfter inserting at the end:")
traverseLinkedList(head)


def insertNodeAtGivenNode(head, prev_value, data):
    temp = head
    
    while temp is not None:
        if temp.data == prev_value:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            return head
        temp = temp.next
    
    print("Previous node not found")
    return head


head = insertNodeAtGivenNode(head, "Ako'y alipin mo kahit hindi batid", "Pag-ibig ko'y tunay at wagas")
head = insertNodeAtGivenNode(head, "Araw-gabi nasa isip ka", "Ikaw lamang ang laman ng puso")