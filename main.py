
from PasswordGenerator import generateWeak,generateMedium,generateStrong

from DataBaseHandler import add_password,delete_password,show_database,search_appAndpassword

from colorama import Fore,Back,Style,init
init(convert=True)
from termcolor import colored

while True:
    print(colored('$'*30,'yellow'))
    print()
    print(colored("WELCOME TO PASSWORD MANAGER",'green'))
    print()
    print(colored('$'*30,'yellow'))
    print()
    print()
    print("what would you like to do ?")
    print("1.Generate password")
    print("2.Show Generated Password")
    print("3.Delete Generated password")
    print("4.Exit")
   
    
    user_input = input(">>>")
    if user_input == "1":
        print("For what application would you like to  use your password?")
        application = input(">>>")
        print()

        print("How strong should the password be:?")
        print("1. Weak = 5-5 chars , pure letters")
        print("2. Medium = 7-12 chars, letters and numbers")
        print("3. Strong = 15-20 chars, letters,numbers and symbols")
        pw_strength = input (">>>")

        if pw_strength == "1":
            password = generateWeak()
        elif pw_strength == "2":
            password = generateMedium()
        elif pw_strength == "3":
            password == generateStrong()
        add_password(application,password)

        print(colored("^"*25,'green'))
        print(colored(f'Saved Password for {application}!','green'))
        print(colored("^"*25,'green'))
    elif user_input == "2":
        show_database()
    elif user_input =="3":
        print()
        print("Are you sure you want to delete it?")
        print()
        print("press Y if yes, press N  to cancel")
        print()
        print()
    elif user_input == "Y":
        while True:
            print()
            print("Enter the application and the password you want to delete")
            print()
            print()
            print()
            app_to_delete = input("Application:")
            pw_to_delete = input("Password:")
            print()
            print()
            if  search_appAndpassword(app_to_delete,pw_to_delete):
                delete_password(app_to_delete,pw_to_delete)
                print(colored("-"*50,'green'))
                print(colored("password deleted",'green'))
                print(colored("-"*50,'green'))
                print()
                break
            else:
                print(colored("-"*50,'red'))
                print()
                print(colored("Account not exists",'red'))  
                print()     
                print(colored("-"*50,'red'))  
                break
         
    elif user_input == "N":
        print()
        print("Cancelled")
        print()
        print()
                  

    elif user_input == "4":
        print()
        print()
        print()
        print()
        print(colored('%'*35,'yellow'))
        print(colored("Thank You for using the program!",'green'))
        print(colored('%'*35,'yellow'))
        break


