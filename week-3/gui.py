import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
        tasks.pop(selected_task_index[0])

# Create the main app window
app = tk.Tk()
app.title("To-Do List")

# Entry field to type a task
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Button to add a task
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Button to remove a selected task
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Listbox to display tasks
task_list = tk.Listbox(app, width=40, height=10)
task_list.pack(pady=10)

# Run the main event loop
app.mainloop()
