def viewbooks():
    bookdata=[]
    with open ("stock.txt", 'r') as books:
        for line in books:
            lines=((line.strip()).split(","))
            bookdata.append(lines)
    return bookdata
    

