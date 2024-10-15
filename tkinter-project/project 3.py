import tkinter as tk
root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("5x5 Checkbox Grid")
for i in range(5):
    for j in range(5):
        checkbox = tk.Checkbutton(root, text=f"{i},{j}")
        checkbox.grid(row=i, column=j, sticky="w")
root.mainloop()