import tkinter as tk
from tkinter import messagebox
import datetime

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.description} | Due: {self.due_date} | Priority: {self.priority}"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.description_label = tk.Label(self.entry_frame, text="Description")
        self.description_label.grid(row=0, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.entry_frame, width=40)
        self.description_entry.grid(row=0, column=1, padx=5, pady=5)

        self.due_date_label = tk.Label(self.entry_frame, text="Due Date (YYYY-MM-DD)")
        self.due_date_label.grid(row=1, column=0, padx=5, pady=5)
        self.due_date_entry = tk.Entry(self.entry_frame, width=40)
        self.due_date_entry.grid(row=1, column=1, padx=5, pady=5)

        self.priority_label = tk.Label(self.entry_frame, text="Priority (High, Medium, Low)")
        self.priority_label.grid(row=2, column=0, padx=5, pady=5)
        self.priority_entry = tk.Entry(self.entry_frame, width=40)
        self.priority_entry.grid(row=2, column=1, padx=5, pady=5)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=0, padx=10)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=10)

        self.view_tasks_button = tk.Button(self.button_frame, text="View Tasks", command=self.view_tasks)
        self.view_tasks_button.grid(row=0, column=2, padx=10)

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if not description or not due_date or not priority:
            messagebox.showwarning("Warning", "All fields must be filled out.")
            return

        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Due date must be in YYYY-MM-DD format.")
            return

        task = Task(description, due_date, priority)
        self.tasks.append(task)
        self.clear_entries()
        self.view_tasks()

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{idx}. {task}")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return

        task_number = selected_task_index[0]
        del self.tasks[task_number]
        self.view_tasks()

    def clear_entries(self):
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
