import tkinter as tk

class SimpleInterestCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple Interest Calculator")
        tk.Label(self.window, text="Principal Amount").grid(row=0, column=0)
        tk.Label(self.window, text="Interest Rate").grid(row=1, column=0)
        tk.Label(self.window, text="Time (years)").grid(row=2, column=0)
        self.principal_entry = tk.Entry(self.window)
        self.rate_entry = tk.Entry(self.window)
        self.time_entry = tk.Entry(self.window)
        self.principal_entry.grid(row=0, column=1)
        self.rate_entry.grid(row=1, column=1)
        self.time_entry.grid(row=2, column=1)
        tk.Button(self.window, text="Calculate", command=self.calculate_interest).grid(row=3, column=0, columnspan=2)
        tk.Label(self.window, text="Simple Interest").grid(row=4, column=0)
        self.interest_label = tk.Label(self.window, text="")
        self.interest_label.grid(row=4, column=1)

    def calculate_interest(self):
        principal = float(self.principal_entry.get())
        rate = float(self.rate_entry.get())
        time = float(self.time_entry.get())
        interest = (principal * rate * time) / 100
        self.interest_label.config(text=str(interest))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = SimpleInterestCalculator()
    calculator.run()

