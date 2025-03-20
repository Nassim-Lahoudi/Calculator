import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry('250x300')
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.quitFunction)
        self.window.attributes( "-topmost", True)
        
        tk.Label(self.window, text="Calculator", font="monospace 13").pack(side=tk.TOP, pady=20)
        
        tk.Label(self.window, text="1st Number", font="monospace 9").pack()
        
        self.num1 = tk.Entry(self.window)
        self.num1.pack(pady=10)
        
        self.operatortype = tk.StringVar()
        
        tk.Label(self.window, text="operators", font="monospace 9").pack()
        
        self.comboOperator = ttk.Combobox(self.window, textvariable=self.operatortype)
        self.comboOperator["values"] = ("+", "-", "*", "/")
        self.comboOperator.pack(pady=5)
        
        tk.Label(self.window, text="2nd Number", font="monospace 9").pack()
        
        self.num2 = tk.Entry(self.window)
        self.num2.pack(pady=10)
        
        self.calculate = tk.Button(self.window, text="Calculate", borderwidth=0.5, command=self.performOperation)
        self.calculate.pack(pady=10)
        
    def performOperation(self):
        num1 = self.num1.get()
        opt = self.comboOperator.get()
        num2 = self.num2.get()
        
        
        if opt == "+":
            result = int(num1) + int(num2)
        elif opt == "-":
            result = int(num1) - int(num2)
        elif opt == "*":
            result = int(num1) * int(num2)
        elif opt == "/":
            if int(num2) != 0:
                result = int(num1) / int(num2)
            else:
                tk.messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            
        tk.messagebox.showinfo(title="Result", message=f"The Result is {result} ")
        
    def quitFunction(self): 
        msg = tk.messagebox.askquestion(title="Warning", message="Are you sure!", icon="warning")
        if msg == "yes":
            self.window.quit()
        
    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    app = Calculator()
    app.run()
    