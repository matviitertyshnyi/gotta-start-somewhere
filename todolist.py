import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
if not os.path.exists('todolist.json'):
    with open('todolist.json', 'w') as file:
        json.dump([], file) 
while True:
    clear_screen()

    with open('todolist.json', 'r') as file:
        data = json.load(file)
    
    
    print("1. See and check tasks out\n")
    print("2. Add tasks\n")
    print("3. Remove tasks\n")
    print("4. See completed tasks\n")
    print("5. See uncompleted tasks\n")
    print("6. See tasks that are in progress\n")
    print("7. Exit\n") 
    
    print("")
    choice = input("Pick: 1-7\n")
    print("")
    match choice:
        
        case "1":
            clear_screen()
            print("Cuurent tasks\n")
            for i, item in enumerate(data, start=1):
                print(f"{i}. {item['task']} [{item['status']}]")
            check_out = input("Which did u manage to complete? Enter task's number: \n")
            if check_out == "":
                continue
            check_out_status = input("Mark as 'Completed'(Type '1') or as 'In Progress'(Type: '2') ")
            if check_out_status == "":
                continue
            for i, item in enumerate(data, start=1):
                if(int(check_out) == i ):
                    if(int(check_out_status) == 1):
                        item["status"] = "Completed"
                    elif(int(check_out_status) == 2):
                        item["status"] = "In progress"
            with open('todolist.json','w') as file:
                json.dump(data, file, indent=3)
        case "2":
            clear_screen()
            print("Adding a task\n")
            new_task = input("Enter task: ")
            
            new_task_dict = {
                "task": new_task,
                "status": "Uncompleted"
            }
            
            data.append(new_task_dict)
            
            with open('todolist.json','w') as file:
                json.dump(data, file, indent=3)
                
            print("\nTask added\n")
            input("Press enter to go back\n")
        case "3":
            clear_screen()
            print("Removing a task...\n")
            print("Current tasks: \n")
            for i, item in enumerate(data, start=1):
                print(f"{i}. {item['task']} [{item['status']}]")
            to_remove = input("Which do you want to remove? Enter task's number: \n")
            if to_remove == "":
                continue
            task_index = int(to_remove) - 1
            for i, item in enumerate(data, start=1):
                if(int(to_remove) == i ):
                    confirmation = input("Type '1' to confirm, '0' to cancel removing: ")
                    if(int(confirmation)==1):
                        removed_task = data.pop(task_index)
                        with open ('todolist.json', 'w') as file:
                            json.dump(data, file, indent = 3)
                            print(f"Task '{removed_task['task']}' was deleted successfully")
                    else:
                        break
            input("Press enter to go back\n")
        case "4":
            clear_screen()
            print("Completed tasks:\n")
            for i, item in enumerate(data, start=1):
                if(item['status'] == "Completed"):
                    print(f"{i}. {item['task']}")
            input("Press enter to go back\n")
        case "5":
            clear_screen()
            print("Tasks to yet be done: \n")
            for i, item in enumerate(data, start=1):
                if(item['status'] == "Uncompleted"):
                    print(f"{i}. {item['task']}")
            input("Press enter to go back\n")
        case "6":
            clear_screen()
            print("Ongoing tasks\n")
            for i, item in enumerate(data, start=1):
                if(item['status'] == "In progress"):
                    print(f"{i}. {item['task']}")
            input("Press enter to go back\n")
        case "7":
            clear_screen()
            print("Goodbye!\n")
            break
        case _: 
            print("Invalid choice, please try again.\n")
            input("Press enter to go back\n")
