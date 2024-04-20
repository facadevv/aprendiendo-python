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
        print("You really don´t like folliwing rules, right? ;)")
        print("---------------->Start again<-------------------")
        try:
            answer=int(input("Please enter a number between 1 and 100:"))
        except:
            print("Really??")
            print("--->Game Over<---")
        else:
            if answer > 0 and answer < 101:
                print("Thanks!")
                number=list((range(1,answer+1)))
                for value in number:
                    result_3=value / 3 
                    result_5=value / 5
                    if result_3 == int(result_3):
                        number[value-1]=str("Fizz")
                    elif result_5 == int(result_5):
                        number[value-1]=str("Buzz")
                    else:
                        number[value-1]=str(value)
                print(number)
            else:
                print("You really don´t like folliwing rules, right? ;)")
                print("--->Game Over<---")
    else:
        if answer > 0 and answer < 101:
            print("Thanks!")
            number=list((range(1,answer+1)))
            for value in number:
                result_3=value / 3 
                result_5=value / 5
                if result_3 == int(result_3):
                    number[value-1]=str("Fizz")
                elif result_5 == int(result_5):
                    number[value-1]=str("Buzz")
                else:
                    number[value-1]=str(value)
            print(number)
        if answer > 101:
            print("You really don´t like folliwing rules, right? ;)")
            print("---------------->Start again<-------------------")
            try:
                answer=int(input("Please enter a number between 1 and 100:"))
            except:
                print("Really??")
                print("--->Game Over<---")
            else:
                if answer > 0 and answer < 101:
                    print("Thanks!")
                    number=list((range(1,answer+1)))
                    for value in number:
                        result_3=value / 3 
                        result_5=value / 5
                        if result_3 == int(result_3):
                            number[value-1]=str("Fizz")
                        elif result_5 == int(result_5):
                            number[value-1]=str("Buzz")
                        else:
                            number[value-1]=str(value)
                    print(number)
                elif answer > 101:
                    print("Really??")
                    print("--->Game Over<---")
FizzBuzz()

