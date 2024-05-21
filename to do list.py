class ToDoList:
    def __init__(self):
        self.tasks = [] #an empty list initialised to store tasks

    # function to add tasks
    def add_task(self, task):
        self.tasks.append(task) #adds tasks into the list
        print(f"Task '{task}' added successfully!")
        
    #function to remove tasks
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f" Your Task '{task}' was completed & removed successfully!")
        else:
            print("Task not found!")

    # function to display tasks in the to-do list
    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

# main function
def main():
    todo_list = ToDoList()
    while True:
        print("*********TO_DO_LIST**********")
        print("Choose from the below options:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting program.!")
            print("HAVE A NICE DAY")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__=="__main__":
    main()
