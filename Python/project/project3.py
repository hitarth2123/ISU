from tkinter import *

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Simple Calculator")
        self.math_expression = ""

        def update_expression(num):
            self.math_expression += str(num)
            equation.set(self.math_expression)

        def evaluate_expression():
            try:
                result = str(eval(self.math_expression))
                equation.set(result)
                self.math_expression = result
            except Exception as e:
                equation.set("Error")
                self.math_expression = ""

        def clear():
            self.math_expression = ""
            equation.set(self.math_expression)
        equation = StringVar()
        expression_field = Entry(self.window, textvariable=equation, width=20)
        expression_field.grid(row=0, column=0, columnspan=4)
        button_1 = Button(self.window, text="1", width=5, command=lambda: update_expression(1))
        button_1.grid(row=1, column=0)
        button_2 = Button(self.window, text="2", width=5, command=lambda: update_expression(2))
        button_2.grid(row=1, column=1)
        button_3 = Button(self.window, text="3", width=5, command=lambda: update_expression(3))
        button_3.grid(row=1, column=2)
        button_4 = Button(self.window, text="4", width=5, command=lambda: update_expression(4))
        button_4.grid(row=2, column=0)
        button_5 = Button(self.window, text="5", width=5, command=lambda: update_expression(5))
        button_5.grid(row=2, column=1)
        button_6 = Button(self.window, text="6", width=5, command=lambda: update_expression(6))
        button_6.grid(row=2, column=2)
        button_7 = Button(self.window, text="7", width=5, command=lambda: update_expression(7))
        button_7.grid(row=3, column=0)
        button_8 = Button(self.window, text="8", width=5, command=lambda: update_expression(8))
        button_8.grid(row=3, column=1)
        button_9 = Button(self.window, text="9", width=5, command=lambda: update_expression(9))
        button_9.grid(row=3, column=2)
        button_0 = Button(self.window, text="0", width=5, command=lambda: update_expression(0))
        button_0.grid(row=4, column=0)
        button_add = Button(self.window, text="+", width=5, command=lambda: update_expression("+"))
        button_add.grid(row=1, column=3)
        button_subtract = Button(self.window, text="-", width=5, command=lambda: update_expression("-"))
        button_subtract.grid(row=2, column=3)
        button_multiply = Button(self.window, text="*", width=5, command=lambda: update_expression("*"))
        button_multiply.grid(row=3, column=3)
        button_divide = Button(self.window, text="/", width=5, command=lambda: update_expression("/"))
        button_divide.grid(row=4, column=3)
        button_equal = Button(self.window, text="=", width=10, command=evaluate_expression)
        button_equal.grid(row=4, column=1, columnspan=2)
        button_clear = Button(self.window, text="Clear", width=20, command=clear)
        button_clear.grid(row=5, column=0, columnspan=4)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()



