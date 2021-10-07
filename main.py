from cli.task_list import *

def list_options_make_choice():

    options = {
        "1": "List all tasks", 
        "2": "Create a task",
        "3": "View one task", 
        "4": "Update task", 
        "5": "Delete task", 
        "6": "Mark complete",
        "7": "Mark incomplete",
        "8": "Delete all tasks",
        "10": "Quit"
        }
    print("Here are the features")
    for number, feature in options.items():
        print(f"{number}. {feature}")

    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Make your selection using the option number: ")

    return choice

def print_stars(sentence):
    print("\n**************************\n")
    print(sentence)
    print("\n**************************\n")

def get_task_from_user(msg = "Input the id of the task you would like to work with: "):
    id = input(msg)
    task = get_task(id)
    if not task:
        print_stars("I cannot find that task.")
    return task

def run_cli():
    
    play = True
    while play:

        # get input and validate
        choice = list_options_make_choice()

        if choice=='1':
            print("Tasks:")
            tasks = list_tasks()
            if not tasks:
                print_stars("No tasks")
            else:
                for task in tasks:
                    print(task)
        elif choice=='2':
            print("Great! Let's create a new task.")
            title=input("What is the title of your task? ")
            description=input("What is the description of your task? ")
            response = create_task(title=title, description=description)
            print("New task:", response)
        elif choice=='3':
            task = get_task_from_user("Input the id of the task you would like to select ")
            if task:
                print_stars(f"Selected task: {response}")
        elif choice=='4':
            task = get_task_from_user()
            if task:
                title=input("What is the new title of your task? ")
                description=input("What is the new description of your task? ")
                response = update_task(task["id"], title, description)
                print_stars(f"Updated task: {response}")
        elif choice=='5':
            task = get_task_from_user("Input the id of the task you would like to delete: ")
            if task:
                delete_task(task["id"])
                print("Task has been deleted.")
                tasks = list_tasks()
                if not tasks:
                    print_stars("No tasks")
                else:
                    for task in tasks:
                        print(task)
        elif choice=='6':
            task = get_task_from_user("Input the id of the task you would like mark complete: ")
            if task:
                response = mark_complete(task["id"])
                print_stars(f"Completed task: {response}")
        elif choice=='7':
            task = get_task_from_user("Input the id of the task you would like mark incomplete: ")
            if task:
                response = mark_complete(task["id"])
                print_stars(f"Completed task: {response}")
        elif choice=='8':
            for task in list_tasks():
                delete_task(task["id"])
            print_stars("Deleted all tasks.")

        elif choice=='10':
            play=False

  
        print_stars("")

print("Welcome to the Task List CLI")
run_cli()