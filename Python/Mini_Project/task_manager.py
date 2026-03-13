import sys
import json
import os

class TaskManager:
    DB_FILE = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.DB_FILE):
            try:
                with open(self.DB_FILE, 'r') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = []

    def save_tasks(self):
        with open(self.DB_FILE, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title):
        self.tasks.append({"title": title, "done": False})
        self.save_tasks()
        print(f"Task '{title}' added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks pending.")
            return
        for i, task in enumerate(self.tasks):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i + 1}. {status} {task['title']}")

    def toggle_task(self, index):
        try:
            target = index - 1
            if 0 <= target < len(self.tasks):
                self.tasks[target]["done"] = not self.tasks[target]["done"]
                self.save_tasks()
                print(f"Task index {index} toggled.")
            else:
                print("Index out of bound.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py [add/list/toggle] <args>")
        sys.exit(1)

    manager = TaskManager()
    command = sys.argv[1].lower()

    if command == "list":
        manager.list_tasks()
    elif command == "add" and len(sys.argv) > 2:
        title = " ".join(sys.argv[2:])
        manager.add_task(title)
    elif command == "toggle" and len(sys.argv) > 2:
        manager.toggle_task(int(sys.argv[2]))
    else:
        print("Invalid command.")