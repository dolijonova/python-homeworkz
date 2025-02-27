from dataclasses import dataclass
from abc import ABC, abstractmethod
import csv
import json

class Task:
    task_id: int
    title: str
    description: str
    due_date: str  # Optional (YYYY-MM-DD)
    status: str  # Pending, In Progress, Completed

class FileStorage(ABC):
    @abstractmethod
    def save_tasks(self, tasks, file_path): pass
    @abstractmethod
    def load_tasks(self, file_path): pass

class CSVStorage(FileStorage):
    def save_tasks(self, tasks, file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            writer.writerows([[t.task_id, t.title, t.description, t.due_date, t.status] for t in tasks])

    def load_tasks(self, file_path):
        try:
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                return [Task(int(r[0]), r[1], r[2], r[3], r[4]) for r in reader]
        except FileNotFoundError:
            return []

class JSONStorage(FileStorage):
    def save_tasks(self, tasks, file_path):
        with open(file_path, 'w') as f:
            json.dump([t.__dict__ for t in tasks], f, indent=4)

    def load_tasks(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return [Task(**item) for item in json.load(f)]
        except FileNotFoundError:
            return []

class TaskManager:
    def __init__(self, storage, file_path):
        self.tasks = storage.load_tasks(file_path)
        self.storage, self.file_path = storage, file_path

    def save_tasks(self):
        self.storage.save_tasks(self.tasks, self.file_path)

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for t in self.tasks:
                print(f"{t.task_id}, {t.title}, {t.description}, {t.due_date}, {t.status}")

    def update_task(self, task_id, **kwargs):
        for t in self.tasks:
            if t.task_id == task_id:
                for key, value in kwargs.items():
                    if value:
                        setattr(t, key, value)
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        print("Task deleted successfully!" if len(self.tasks) < initial_count else "Task not found.")

    def filter_tasks(self, status):
        filtered = [t for t in self.tasks if t.status.lower() == status.lower()]
        if not filtered:
            print("No tasks match the given status.")
        else:
            for t in filtered:
                print(f"{t.task_id}, {t.title}, {t.description}, {t.due_date}, {t.status}")

def main():
    storage_format = input("Choose storage format (csv/json): ").strip().lower()
    file_path = f"tasks.{storage_format}"
    storage = CSVStorage() if storage_format == "csv" else JSONStorage() if storage_format == "json" else None

    if not storage:
        print("Invalid storage format. Defaulting to JSON.")
        storage, file_path = JSONStorage(), "tasks.json"

    manager = TaskManager(storage, file_path)

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Filter Tasks\n6. Save Tasks\n7. Load Tasks\n8. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.add_task(Task(int(input("Task ID: ")), input("Title: "), input("Description: "),
                                  input("Due Date (YYYY-MM-DD): "), input("Status: ")))
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.update_task(int(input("Task ID: ")), title=input("New Title: ") or None,
                                description=input("New Description: ") or None,
                                due_date=input("New Due Date: ") or None,
                                status=input("New Status: ") or None)
        elif choice == "4":
            manager.delete_task(int(input("Task ID: ")))
        elif choice == "5":
            manager.filter_tasks(input("Filter by Status: "))
        elif choice == "6":
            manager.save_tasks()
            print("Tasks saved successfully!")
        elif choice == "7":
            manager.tasks = storage.load_tasks(file_path)
            print("Tasks loaded successfully!")
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
