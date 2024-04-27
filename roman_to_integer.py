#Given a roman numeral, convert it to an integer.
#Example:                                       Input: s = "MCMXCIV"
#                                               Output: 1994
#                                               Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
                                                                                                                                                #
class node:
    def __init__ (self, letter):
        self.letter=letter
        self.next=None
class linked_list:
    def __init__ (self):
        self.head=None   
    def insert(self,letter):
        new_node=node(letter)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def RomanToDecimal(self):
        roman_letters={"I","V","X","L","C","D","M"}
        answer=input("Please, enter a Roman number: ")
        if answer== answer.lower():
            print("-------------------------------------------------------------")
            print("|Roman numbers are ritten with CAPITAL LETTERS, try again ;)|")
            print("-------------------------------------------------------------")
            for char in answer:
                if char not in roman_letters:
                    print("             ---------------------------------")
                    print("             |AND...That´s not a Roman number|")
                    print("             ---------------------------------")
                    break
        elif answer== answer.upper():
            for char in answer:
                if char not in roman_letters:
                    print("-----------------------------------------")
                    print("|That´s not a Roman number, try again ;)|")
                    print("-----------------------------------------")
                    break
        for char in answer:
            self.insert(char)
        current=self.head   
        values=list()
        sum=0
        while current:
            if current:
                current_letter=current.letter
                if current and current.next:
                    next_letter=current.next.letter
                else:
                    next_letter=None
            if current_letter=="I":
                
                if current_letter=="I" and next_letter=="V":
                    values.append(4)
                    current=current.next.next
                elif current_letter=="I" and next_letter=="X":
                    values.append(9)
                    current=current.next.next
                else:
                    values.append(1)
                    current=current.next
            if current_letter=="V":
                values.append(5)
                current=current.next
            if current_letter=="X":
                if current_letter=="X" and next_letter=="L":
                    values.append(40)
                    current=current.next.next
                elif current_letter=="X" and next_letter=="C":
                    values.append(90)
                    current=current.next.next
                else:
                    values.append(10)
                    current=current.next
            if current_letter=="L":
                values.append(50)
                current=current.next            
            if current_letter=="C":
                if current_letter=="C" and next_letter=="D":
                    values.append(400)
                    current=current.next.next
                elif current_letter=="C" and next_letter=="M":
                    values.append(900)
                    current=current.next.next
                else:
                    values.append(100)
                    current=current.next            
            if current_letter=="D":
                values.append(500)
                current=current.next            
            if current_letter=="M":
                values.append(1000)
                current=current.next
        for e in values:
            sum+=e
        print(sum)
LL=linked_list()
LL.RomanToDecimal()

