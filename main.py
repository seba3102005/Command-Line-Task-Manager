description = {}
priority = {}
due_date = {}

def MenuShow ():
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
    print("======================")
    print("Please choose an option from 1-5")

def Add_task ():
    name = "Task"+str((len(description)+1))
    desc = input("Please Enter theTask descripyion")
    prio = input("Please enter the Priority of your task")
    date = input("enter the task's due date")

    description.setdefault( name , desc )
    priority.setdefault(name , prio )
    due_date.setdefault(name , date )

def show_tasks():
    i=1
    for x,y,z in zip(description.values(),priority.values(),due_date.values()):
        print (f"Task {i}: {x} , the priority of it is {y} ,the DUE DATE is on {z}")
        i+=1





MenuShow()
while (True):
    choice = input("Enter your choice: ")
    choices = ['1','2','3','4','5']
    while choice not in choices:
       print("Invalid choice ,Please Enter a valid one:")
       MenuShow()
       choice = input("Enter your choice: ")
    if(choice=='5'):
        break
    
    if(choice =='2'):
        Add_task()
    elif (choice=='1'):
        show_tasks()

    


