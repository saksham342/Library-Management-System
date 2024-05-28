import os
import random
import showbooks
import readbook

def book_management_operation():
    
    def addbook():
        booklist = readbook.viewbooks()
        random_number=random.randint(1,999999)
        bookid_generated=f'{random_number:06}'
        addcheck = input("Do you want to add new book or existing book: (n/N or e/E)")
        
        if addcheck in {'e','E'}:
            showbooks.printbooks()
            while True:
                id = input("Enter book id which you want to add: ")
                idfound=False
                for i in range (len(booklist)):
                    if booklist[i][0]==id:
                        idfound=True
                        print(f"The book name is: {booklist[i][1]}")
                        quantity = input("Enter the quantity of book to add: ")
                        booklist[i][5] = int(booklist[i][5])+int(quantity)
                        
                        with open ("stock.txt", "w") as stock:
                            for i in range (len(booklist)):
                                for j in range (len(booklist[i])):
                                    if j!=5:
                                        stock.write(str(booklist[i][j])+",")
                                    else:
                                        stock.write(str(booklist[i][j]))
                                stock.write("\n")
                if idfound==False:
                    print("The book with that book id is not found in our database. ")
                else:
                    break
            

        elif addcheck in {'n','N'}:
            name = input("Please enter the name of the book: ")
            author = input("Please enter the author of the book: ")
            publication = input("Please enter the publication name: ")
            published_year = input("Please input the published year: ")
            published_month = input("Please input the published month: ")
            published_day = input("Please input the published day: ")
            new_quantity = input("Please enter the quantity of the book: ")
            published_date = f"{published_year}:{published_month}:{published_day}"
            print(published_date)
            print(f"Your book detains are:\n name: {name} | author: {author} | publication: {publication} | published date: {published_date}")
            confirm_add = input("Do you sure want to add the books of above details: (y/Y  or  n/N)")
            if confirm_add in {'y', 'Y'}:
                booklist.append([bookid_generated,name,author,publication,published_date])
                with open ("stock.txt", "w") as stock:
                    for i in range (len(booklist)):
                        for j in range (len(booklist[i])):
                            if j!=5:
                                stock.write(str(booklist[i][j])+",")
                            else:
                                stock.write(str(booklist[i][j]))
                        stock.write("\n")
                            
                
                    # stock.write("\n"+str((bookid_generated)+", "+name+", "+author+", "+publication+", "+published_date))

            elif confirm_add in {'n', 'N'}:
                print("Book adding cancelled")

    def removebook():
        showbooks.printbooks()
        def remove_book_by_id(book_id):
            with open('stock.txt', 'r') as file:
                lines = file.readlines()

            # Find the index of the line containing the specified book ID
            index_to_remove = None
            for i, line in enumerate(lines):
                if book_id in line:
                    index_to_remove = i
                    break

            # If the book ID is found, remove the corresponding line
            if index_to_remove is not None:
                del lines[index_to_remove]

                # Write the modified lines back to the file
                with open('stock.txt', 'w') as file:
                    file.writelines(lines)
                print(f"Book with ID {book_id} has been removed.")
            else:
                print(f"Book with ID {book_id} not found in the file.")


        user_input = input("Enter the book ID to remove: ")

        remove_book_by_id(user_input)

    def showbook():
        showbooks.printbooks()

    while True:

        options = f'''
    ................................................
    """"""""""""""""""""""""""""""""""""""""""""""""
            Please Select option for operation
    ------------------------------------------------

    Your options are:
    1. Add book to library
    2. Remove book from library
    3. View all book details
    4. Back to main menu
    """"""""""""""""""""""""""""""""""""""""""""""""      
Choose one of the four options: 
'''
        print(options)
        management_option=input("")
        if management_option == "1":
            addbook()
        elif management_option=="2":
            removebook()
        elif management_option=="3":
           showbook()
        elif management_option=="4":
            break
  
