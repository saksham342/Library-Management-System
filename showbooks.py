import readbook
import os

bookslist = readbook.viewbooks()
def printbooks():
    print("\nThe books in your library are:\n")
    topics = f'''
    {"Book ID":>0}{"Book Name":>35}{"Author Name":>30}{"Publication name":>35}{"Published Date":>30}{"Quantity":>20}
'''
    print(topics)
    
    for i in range (len(bookslist)):
        for j in range (len(bookslist[i])):
            a = bookslist[i][j]
            print("{:<30}".format("|    "+a),end="")
        print("\n")

