
#Given an integer num, return the number of steps to reduce it to zero.
#In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

                   #Exemple: Input: num = 14
                          #Output: 6
                        #Explanation: 
        #Step 1) 14 is even; divide by 2 and obtain 7. 
        #Step 2) 7 is odd; subtract 1 and obtain 6.
        #Step 3) 6 is even; divide by 2 and obtain 3. 
        #Step 4) 3 is odd; subtract 1 and obtain 2. 
        #Step 5) 2 is even; divide by 2 and obtain 1. 
        #Step 6) 1 is odd; subtract 1 and obtain 0.

def Steps_to_Zero():

    answer=int(input("Please enter a number: "))
    answer_init=answer
    counter=0
    while answer != 0:
        counter+=1
        if answer % 2 == 0:
            answer=answer/2            
        else:
            answer=answer-1
    print(f"The number of steps to zero from {answer_init} is: {counter}")

Steps_to_Zero()