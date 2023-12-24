import tkinter as tk
from tkinter import font as tkf

# Counter Project

class Multiply(tk.Tk):
    def __init__(self):
        super(Multiply, self).__init__()
        self.title("Counter Project")
        self.geometry("+500+250")
        self.font = tkf.Font(name='Arial', size=20, weight="bold")
        self.font2 = tkf.Font(name='Arial3', size=10, weight="bold")
        self.components()


    def components(self):
        self.entry1 = tk.Entry( font=self.font, relief=tk.GROOVE, width=10)
        self.entry1.pack(side=tk.LEFT)

        self.label = tk.Label(text="x", font=self.font, padx=20, pady=20)
        self.label.pack(side=tk.LEFT)

        self.entry2 = tk.Entry(font=self.font, relief=tk.GROOVE, width=10)
        self.entry2.pack(side=tk.LEFT)

        self.btresult = tk.Button(command=self.multiply, text="Result", font=self.font2, relief=tk.GROOVE, padx=20, pady=20, width=5)
        self.btresult.pack(side=tk.LEFT)

        self.label2 = tk.Label(text="0", font=self.font, padx=20, pady=20)
        self.label2.pack(side=tk.LEFT)

    def multiply(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1*num2
            self.label2.configure(text=str(result))
        except ValueError:
            print("please enter numbers")


multi = Multiply()
multi.mainloop()