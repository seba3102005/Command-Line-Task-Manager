def MenuShow ():
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
    print("======================")
    print("Please choose an option from 1-5")

MenuShow()
choice = input("Enter your choice: ")
choices = ['1','2','3','4','5']
while choice not in choices:
    print("Invalid choice ,Please Enter a valid one:")
    MenuShow()
    choice = input("Enter your choice: ")

else:
    pass

