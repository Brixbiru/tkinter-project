import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("My First GUI")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox=tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10) 

#myentry = tk.Entry(root)
#myentry.pack()

#button = tk.Button(root, text = "Click Me!", font = ('Arial', 18))
#button.pack(padx=10, pady=10)

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

btn1=tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2=tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3=tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=1, column=0, sticky=tk.W+tk.E)

btn4=tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=1, sticky=tk.W+tk.E)

buttonframe.pack()
#buttonframe.pack(fill='x')

anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=200, y=250, height=100, width=100 )

root.mainloop()