#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.
#Example 1:                     #Input: head = [1,2,3,4,5]
                                #Output: [3,4,5]

#Example 2:                     #Input: head = [1,2,3,4,5,6]
                                #Output: [4,5,6]
#Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
class node:
    def __init__(self, data):                
        self.data=data                                      
        self.next=None
class linked_list:
    def __init__(self):
        self.head = None
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def insert(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def print_middle_of_the_linked_list(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None and fast_ptr.next.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next     
        if self.length() % 2 == 0 and slow_ptr and slow_ptr.next:
            slow_ptr = slow_ptr.next
        while slow_ptr:
            print(slow_ptr.data)
            slow_ptr = slow_ptr.next
    def inputt(self):
        print("Este programa imprimirá desde el nodo medio de una lista enlazada.")
        while True:
            answer = input("Por favor, ingresa un número, o, presiona f para terminar:")
            if answer == "f" or answer== "F":
                break
            else:
                self.insert(answer)

LL = linked_list()
LL.inputt()
LL.print_middle_of_the_linked_list()
