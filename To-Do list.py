tasks = []

def addTask(): # this is for adding the tasks. 
    task = input("Please enter what tasks you have to do today: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")

def listTasks(): # this is for listing the tasks.
    if not tasks:
      print("There are no tasks currently. ")
    else:
      print("Current tasks: ")
    for index, task in enumerate(tasks): # "enumerate" helps us to access each individual task.
      print(f"Task {index}. {task}")
        # for example if a task is like 1. Complete the assignment, 2. Go to buy grocery etc.
   
def deleteTask(): # this is for deleting a task upon its completion.
    listTasks()
    try:
        taskToDelete = int(input("Which task would you like to delete??: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks): # so that only +ve no.s are provided by the user or from the no.s that are available.
              tasks.pop(taskToDelete) # .pop helps in specifying what we want to delete.
              print(f"{taskToDelete} has been deleted/ completed successfully. ")
          
        else:
              print("Please enter from the number of tasks you have provided. ")
    except:
            print("There is no such number. ")

if _name_ == "_main_":
    #creating a loop to run the app
    print("Hello and welcome to the to do list app. I am here to plan out your day so that it can be really amazing and productive :)")
    while True:
        print("\n")
        print("Please select how you wanna plan your day out by choosing one of the following options:- ")
        print(".............................................")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")

        choice = input("So, what do you choose??: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        else:
            print("Sorry but you can only choose from the above options :( ")
