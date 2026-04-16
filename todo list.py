import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-do List")
root.geometry("500x400")
root.resizable(False, False)

tasks = []

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

entry_label = tk.Label(frame, text="New Task:")
entry_label.grid(row=0, column=0, sticky="w")

task_entry = tk.Entry(frame, width=40)
task_entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))

task_listbox = tk.Listbox(frame, width=50, height=12)
task_listbox.grid(row=2, column=0, columnspan=2, sticky="nsew")

add_button = tk.Button(frame, text="Add Task", width=15)
add_button.grid(row=3, column=0, pady=10, sticky="w")

delete_button = tk.Button(frame, text="Delete Selected", width=15)
delete_button.grid(row=3, column=1, pady=10, sticky="e")

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)


def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


def add_task():
    new_task = task_entry.get().strip()
    if not new_task:
        messagebox.showwarning("Empty Task", "Please enter a task before adding.")
        return
    tasks.append(new_task)
    task_entry.delete(0, tk.END)
    refresh_task_list()


def delete_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("No Selection", "Please select a task to delete.")
        return
    index = selected_index[0]
    tasks.pop(index)
    refresh_task_list()

add_button.config(command=add_task)
delete_button.config(command=delete_task)

task_entry.focus()
root.mainloop()
