import showbooks
import os
import book_management
import user_management
def firstdisplay():
    main = f"""
    ................................................
    """"""""""""""""""""""""""""""""""""""""""""""""
             Library Management software
    ------------------------------------------------

    Your options are:
    1. Book Management
    2. User Management 
    3. Transaction functions
    4. Exit program
    """"""""""""""""""""""""""""""""""""""""""""""""      
Choose one of the four options: 
"""
    while True:
        print(main)
        option = input("")
        if option == "1":
            book_management.book_management_operation()
        elif option == "2":
            user_management.user_management_operation()
        elif option == "3":
            break
            pass
        elif option == "4":
            exit()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please select option from 1 - 4 only. ")

firstdisplay()