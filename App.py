First_Name = input("please enter your first name: ")
last_Name = input("please enter your last name: ")
print("Hello"+ " "+First_Name +" "+ last_Name)
Age_group= 2024-int(input("please enter your age: "))
if Age_group<=2008 :
    check_item = input("Are you a newcomer student?(Yes/No) ")
    if check_item == 'Yes':
        print("Welcome to the NHL_Stenden University")
    else:
        print("How can I help you?")
    exit()
else:
    print("Hello to new generation")
