import os
import pickle  # For saving and loading tasks
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False  # Tasks start as not completed

    def __str__(self):
        status = '[X]' if self.completed else '[ ]'
        return f'{status} {self.description}'
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index!")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                print(f'{i+1}. {task}')

    def save_tasks(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)
def main():
    todo_list = ToDoList()

    # Load tasks from file (if exists)
    filename = 'tasks.pickle'
    todo_list.load_tasks(filename)

    while True:
        print("\n==== To-Do List App ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Remove Task")
        print("5. Save and Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            task = Task(description)
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)

        elif choice == '4':
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(index)

        elif choice == '5':
            todo_list.save_tasks(filename)
            print("Tasks saved. Exiting.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
