
#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.

#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [3,4,5]
#Explanation: The middle node of the list is node 3.

#Example 2:
#Input: head = [1,2,3,4,5,6]
#Output: [4,5,6]
#Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

class node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head=None

    def insert(self, data):
        new_node=node(data)
        if(self.head):
            current=self.head
            while (current.next):
                current=current.next
            current.next=new_node
        else:
            self.head=new_node

    def printLL(self):
        current=self.head
        while (current):
            print(current.data)
            current=current.next

LL=linked_list()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
