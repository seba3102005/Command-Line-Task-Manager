description = {}
priority = {}
due_date = {}
data ={}

def MenuShow ():
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
    print("======================")
    print("Please choose an option from 1-5")

def Add_task ():
    name = str((len(data)+1))
    desc = input("Please Enter theTask description: ")
    prio = input("Please enter the Priority of your task: ")
    date = input("enter the task's due date: ")

    data[name]= {"description": desc , "priority" : prio , "date" : date}
    # description.setdefault( name , desc )
    # priority.setdefault(name , prio )
    # due_date.setdefault(name , date )

def show_tasks():
    
    print (len(data))
    print('=============================================')

    
    for indx,value in zip(data.keys(),data.values()):
        print (f" Task {indx}: the description: {value.get('description')}, the priority of it is {value.get('priority')} ,the DUE DATE is on {value.get('date')}")
        
    print('=============================================')

def deleteTask():
    if(len(data)==0):
        print('the task list is already empty')
        return
    show_tasks()
    choices_list = [str(a) for a in range (1,len(data)+1)]
    choice = input("enter the number of the task that you want to delete")
    

    while choice not in choices_list:
        print('invalid task to delete , please enter a valid one')
        show_tasks()
        choice = input("enter the number of the task that you want to delete")


    name =  choice
    print(f"deleting { name }")
    data.pop(name)
    
    
    new_dic = {str(idx): value for idx, value in enumerate(data.values(), start=1)}

    
    data.clear()
    i=1
    for value in new_dic.values():
        data[str(i)] = {"description": value['description'] , "priority" : value['priority'] , "date" : value['date']}
        
    
    
def Update_Task ():
    show_tasks()
    choices_list = [str(a) for a in range (1,len(data)+1)]
    choice = input("enter the number of the task that you want to update")

    while choice not in choices_list:
        print('invalid task to update , please enter a valid one')
        show_tasks()
        choice = input("enter the number of the task that you want to update")

    name =  choice
    print(f"updating { name }")
    desc = input("Please Enter theTask description")
    prio = input("Please enter the Priority of your task")
    date = input("enter the task's due date")

    data.update( {name : {'description' : desc , 'priority' : prio , 'date' : date }} )
    







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
    

    

