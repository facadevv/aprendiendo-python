#Given an integer n, return a string array answer (1-indexed) where:

#    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#    answer[i] == "Fizz" if i is divisible by 3.
#    answer[i] == "Buzz" if i is divisible by 5.
#    answer[i] == i (as a string) if none of the above conditions are true.

#Exemple
#Input: n = 15
#Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

def FizzBuzz():
    try:
        answer=int(input("Please enter a number between 1 and 100:"))
    except:
        print("")
        print("It has to be a number")
        print("---->Start again<----")
        FizzBuzztry()
    else:
        if answer > 0 and answer < 101:
            print("")
            print("There you go:")
            number=list((range(1,answer+1)))
            for value in number:
                result_3=value / 3 
                result_5=value / 5
                if result_3 == int(result_3) or result_5 == int(result_5):
                    if result_3 == int(result_3):
                        number[value-1]=str("Fizz")
                    elif result_5 == int(result_5):
                        number[value-1]=str("Buzz")
                    if result_3 == int(result_3) and result_5 == int(result_5):
                        number[value-1]=str("FizzBuzz")
                else:
                    number[value-1]=str(value)
            print(number)
        elif answer > 100:
            print("")
            print("Come on it´s not that hard ;)")
            print("-------->Start again<--------")
            FizzBuzztry()

def FizzBuzztry():
    try:
        answer=int(input("Ok... REMEMBER, enter a number between 1 and 100:"))
    except:
            print("")
            print("You really don´t like following rules, right?")
            print("----------------->Game Over<-----------------")
    else:
        if answer > 0 and answer < 101:
            print("")
            print("There you go:")
            number=list((range(1,answer+1)))
            for value in number:
                result_3=value / 3 
                result_5=value / 5
                if result_3 == int(result_3) or result_5 == int(result_5):
                    if result_3 == int(result_3):
                        number[value-1]=str("Fizz")
                    elif result_5 == int(result_5):
                        number[value-1]=str("Buzz")
                    if result_3 == int(result_3) and result_5 == int(result_5):
                        number[value-1]=str("FizzBuzz")
                else:
                    number[value-1]=str(value)
            print(number)
        else:
                print("")
                print("You really don´t like following rules, right?")
                print("----------------->Game Over<-----------------")
FizzBuzz()
