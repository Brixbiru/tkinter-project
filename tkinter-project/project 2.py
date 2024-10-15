
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter.scrolledtext import ScrolledText
class b:
    def __init__(self):
        #self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Starters")
        self.root.configure(bg='black')
        
        self.check_state_1 = tk.IntVar()
        self.check_state_2= tk.IntVar()
        self.check_state_3 = tk.IntVar()
        self.check_state_4 = tk.IntVar()
        self.check_state_5 = tk.IntVar()

        #self.buttonframe=tk.Frame(self.root)
        #self.buttonframe.columnconfigure(0, weight=1)
        #self.buttonframe.columnconfigure(1, weight=1)

        self.image_1=PhotoImage(file=r'/Users/brindap/Downloads/Veg Manchuria Small.png')

        self.check_1 = tk.Checkbutton(self.root, text="Veg Manchuria 70", font=('Arial', 16), bg='black', fg='maroon', image=self.image_1, variable=self.check_state_1)
        self.check_1.grid(row=0, column=0, padx=45, pady=30)
        self.check_1.image=self.image_1

        self.image_2=PhotoImage(file=r'/Users/brindap/Downloads/Chicken Manchuria Small.png')

        self.check = tk.Checkbutton(self.root, text="Chicken Manchuria 100", font=('Arial', 16), bg='black', fg='maroon', image=self.image_2, variable=self.check_state_2)
        self.check.grid(row=0, column=1, padx=30, pady=30)
        self.check.image=self.image_2

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Fruit Salad Small.png')

        self.check = tk.Checkbutton(self.root, text="Fruit Salad 50", font=('Arial', 16), bg='black', fg='maroon', image=self.image, variable=self.check_state_3)
        self.check.grid(row=0, column=2, padx=45, pady=30)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Vegetable Salad Small.png')

        self.check = tk.Checkbutton(self.root, text="Vegetable Salad 30", font=('Arial', 16), bg='black', fg='maroon', image=self.image, variable=self.check_state_4)
        self.check.grid(row=1, column=0, padx=90, pady=20)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Fruit custard Small.png')

        self.check = tk.Checkbutton(self.root, text="Fruit Custard 50", font=('Arial', 16), bg='black', fg='maroon', image=self.image, variable=self.check_state_5)
        self.check.grid(row=1, column=1, padx=90, pady=20)
        self.check.image=self.image


        self.root.mainloop()

b()