

def input_expected_answer():
    try:
        choice = int(input('Enter your choice´s number: '))
        return choice
    except ValueError:
        print('Please enter a valid integer.')

def sales_manager():
    print('What do you want?\n 1.- Create a new sales file\n 2.- Add sale\n 3.- Consult sales manager\n 4.- Exit')
    
    while True:
        choice = input_expected_answer()
        
        if choice in (1, 2, 3, 4):
            print('Processing your request...')
            
            if choice == 1:
                print("sales_file = open('Files/sales_file.txt', 'w+')")
                print("sales_file)")   
            if choice == 2:
                print("add_sale()")
                
            if choice == 3:
                print("consult()")
                
            elif choice == 4:
                print('Leaving the program...')
                break
        else:
            print('You must enter a valid option (1, 2, 3, or 4).')

    print("continue")

sales_manager()
