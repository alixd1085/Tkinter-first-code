import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter training")
Label = tk.Label(root, text="This is a label")
entry = tk.Entry(root, width=40)
output_label = tk.Label(root, text="")


root.geometry("400x300")
Label.pack(pady=10)
entry.pack(pady=10)
output_label.pack(pady=10)

def show_input():
    user_input= entry.get()
    output_label.config(text=f"You wrote {user_input}")

button = tk.Button (root, text="Show", command=show_input)
button.pack(pady=10)
root.mainloop()