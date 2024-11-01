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
    desc = input("Please Enter theTask description: ")
    prio = input("Please enter the Priority of your task: ")
    date = input("enter the task's due date: ")

    description.setdefault( name , desc )
    priority.setdefault(name , prio )
    due_date.setdefault(name , date )

def show_tasks():
    i=1
    print('=============================================')
    for x,y,z in zip(description.values(),priority.values(),due_date.values()):
        print (f"Task {i}: {x} , the priority of it is {y} ,the DUE DATE is on {z}")
        i+=1
    print('=============================================')

def deleteTask():
    if(len(description)==0):
        print('the task list is already empty')
        return
    show_tasks()
    choices_list = [str(a) for a in range (1,len(description)+1)]
    choice = input("enter the number of the task that you want to delete")
   

    while choice not in choices_list:
        print('invalid task to delete , please enter a valid one')
        show_tasks()
        choice = input("enter the number of the task that you want to delete")

    name = "Task"+ choice
    print(f"deleting { name }")
    description.pop(name)
    priority.pop(name)
    due_date.pop(name)


def Update_Task ():
    show_tasks()
    choices_list = [str(a) for a in range (1,len(description)+1)]
    choice = input("enter the number of the task that you want to update")

    while choice not in choices_list:
        print('invalid task to update , please enter a valid one')
        show_tasks()
        choice = input("enter the number of the task that you want to update")

    name = "Task"+ choice
    print(f"updating { name }")
    desc = input("Please Enter theTask description")
    prio = input("Please enter the Priority of your task")
    date = input("enter the task's due date")

    description.update( {name : desc} )
    priority.update({name : prio} )
    due_date.update({name : date })








while (True):

    MenuShow()
    choice = input("Enter your choice: ")
    choices = ['1','2','3','4','5']

    while choice not in choices:
       print("Invalid choice ,Please Enter a valid one:")
       MenuShow()
       choice = input("Enter your choice: ")

    if(choice=='5'):
        print("exitting the program\n ======== \n BYE BYE")
        break
    
    if(choice =='2'):
        Add_task()

    elif (choice=='1'):
        show_tasks()

    elif choice=='3':
        Update_Task()

    elif (choice=='4'):
        deleteTask()
    

    

