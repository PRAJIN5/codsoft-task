class ToDoList:
    def __init__(self):  # Correcting the constructor
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def update_task(self, task_number, updated_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1] = updated_task
            print(f"Task {task_number} updated to '{updated_task}'")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted!")
        else:
            print("Invalid task number!")

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("\nEnter a new task: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.view_tasks()
            task_number = int(input("\nEnter the task number to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(task_number, updated_task)
        elif choice == '4':
            todo_list.view_tasks()
            task_number = int(input("\nEnter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
