import random

def user_management_operation():
    def read_users():
        userdata=[]
        with open ("user.txt", 'r') as users:
            for line in users:
                lines=((line.strip()).split(","))
                userdata.append(lines)
        return userdata
    def print_user_details():
        userlist = read_users()
        title = f'''
................................................
    """"""""""""""""""""""""""""""""""""""""""""""""
           User Details are prited below
    ------------------------------------------------
'''     
        print(title)
        topics = f'''
    {"Library user ID":>0}{"User Name":>25}{"Grade":>24}{"Faculty":>35}{"Contact No.":>33}{"Student ID":>28}
'''     
        print(topics)
        for i in range (len(userlist)):
            for j in range (len(userlist[i])):
                a = userlist[i][j]
                print("{:<30}".format("|    "+a),end="")
            print("\n")

    def addUser():
        random_number=random.randint(1,99999)
        libraryId_generated=f'{random_number:05}'
        username = input("Enter the full name of the user: ")
        grade = input("Enter the grade of student from 1 to 12: ")
        faculty = input("Enter the faculty of student: ")
        contact = input("Enter the contact number of student: ")
        studentId = input("Enter the college ID / student ID of the student: ")
        userlist = read_users()
        userlist.append([libraryId_generated,username,grade,faculty,contact,studentId])
        with open ("user.txt", "w") as user:
            for i in range (len(userlist)):
                for j in range (len(userlist[i])):
                    if j!=5:
                        user.write(str(userlist[i][j])+",")
                    else:
                        user.write(str(userlist[i][j]))
                user.write("\n")
    def removeUser():
        def remove_user_by_id(toRemoveID):
            with open('user.txt', 'r') as file:
                lines = file.readlines()

                # Find the index of the line containing the specified book ID
            index_to_remove = None
            for i, line in enumerate(lines):
                if toRemoveID in line:
                    index_to_remove = i
                    break
                

            # If the book ID is found, remove the corresponding line
            if index_to_remove is not None:
                del lines[index_to_remove]

                # Write the modified lines back to the file
                with open('user.txt', 'w') as file:
                    file.writelines(lines)
                print(f"User with Library ID {toRemoveID} has been removed.")
            else:
                print(f"Book with Library ID {toRemoveID} not found in the file.")
        print_user_details()
        toRemoveID = input("Enter the Library Id of student which user you want to remove: ")
        remove_user_by_id(toRemoveID)

    def updateUser():
        def update_user_by_id(id_to_update):
            with open('user.txt', 'r') as file:
                lines = file.readlines()

                # Find the index of the line containing the specified book ID
            index_to_update = None
            for i, line in enumerate(lines):
                if id_to_update in line:
                    index_to_update = i
                    break
            print(index_to_update)
            if index_to_update is not None:
                updated_name = input("Enter the updated name of the user (Enter to skip): ")
                updated_grade = input("Enter the updated grade of student from 1 to 12 (Enter to skip): ")
                updated_faculty = input("Enter the updated faculty of student (Enter to skip): ")
                updated_contact = input("Enter the updated contact number of student (Enter to skip): ")
                updated_studentId = input("Enter the updated college ID / student ID of the student (Enter to skip): ")
                userdata = read_users()
                with open('user.txt', 'w') as file_to_update:
                    
                    if len(updated_name.strip())>0:
                        userdata[index_to_update][1]=updated_name

                    if len(updated_grade.strip())>0:
                        userdata[index_to_update][2]=updated_grade

                    if len(updated_faculty.strip())>0:
                        userdata[index_to_update][3]=updated_faculty

                    if len(updated_contact.strip())>0:
                        userdata[index_to_update][4]=updated_contact                        

                    if len(updated_studentId.strip())>0:
                        userdata[index_to_update][5]=updated_studentId                        
                    
                    for i in range (len(userdata)):
                        for j in range (len(userdata[i])):
                            if j!=5:
                                file_to_update.write(str(userdata[i][j])+",")
                            else:
                                file_to_update.write(str(userdata[i][j]))
                        file_to_update.write("\n")
        print_user_details()
        update_id = input("Enter the user Library ID which you want to update: ")
        update_user_by_id(update_id) 




    def viewUserLog():
        pass

    def mainoptions():
        user_management_options = f"""
    ................................................
    """"""""""""""""""""""""""""""""""""""""""""""""
             User Management Operation
    ------------------------------------------------

    Your options are:
    1. Add User
    2. Remove User 
    3. Update user info
    4. View user's activities
    5. View User data
    6. Back to Menu
    """"""""""""""""""""""""""""""""""""""""""""""""      
Choose one of the four options: 
"""
        while True:
            print(user_management_options)
            selected = input("")
            if selected=="1":
                addUser()
            elif selected=="2":
                removeUser()
            elif selected=="3":
                updateUser()
            elif selected=="4":
                viewUserLog()
            elif selected=="5":
                print_user_details()

    mainoptions()