print("########################################")
print("MYPY PHONE BOOK")
print("########################################")

#Prompt the user to choose an option
def print_menu():
    print('1 : Add New Entry')
    print('2 : Delete Entry')
    print('3 : Update Entry')
    print('4 : Lookup Number')
    print('5 : QUIT')

numbers = {}
option = 0
print_menu()
while option != 5:
    option = int(input("Choose  number between 1 and 5: "))

    #To update an entry
    if option == 3:
        y=input("Enter name whose number needs update:")
        for x in numbers.keys():
            if x==y:
                numbers[x]= int(input("Enter a new number:"))
                print("Name: ", x, "\tNumber:", numbers[x])
                print()

    #To add new entry
    elif option == 1:
        print("Add a Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        if phone in numbers.values():
            print(" This Phone number already exists")
        else:
            numbers[name] = phone

    # To Delete an existing entry
    elif option == 2:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")

    # To lookup up for an entry
    elif option == 4:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")

    #when the user decides to quit
    elif option != 5:
        print_menu()