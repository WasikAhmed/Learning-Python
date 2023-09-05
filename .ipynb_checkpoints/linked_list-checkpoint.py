
# Node Class
class Node:
    def __init__(self, data):
        self.data = data # Assigning data
        self.next = None # Initializing next as null

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__' :
    # creating an empty list
    list = LinkedList()

    list.head = Node(69)
    second_node = Node(20)
    third_node = Node(100)

    list.head.next = second_node
    second_node.next = third_node

    list.print_list()