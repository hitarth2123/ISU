import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ATM Simulator")
        self.username = "admin"
        self.pin = "1234"
        self.balance = 1000
        self.login_frame = tk.Frame(self.window)
        self.login_frame.pack()
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.pack(side=tk.LEFT)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(side=tk.LEFT)
        self.pin_label = tk.Label(self.login_frame, text="Pin:")
        self.pin_label.pack(side=tk.LEFT)
        self.pin_entry = tk.Entry(self.login_frame, show="*")
        self.pin_entry.pack(side=tk.LEFT)
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(side=tk.LEFT)
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack()
        self.withdraw_label = tk.Label(self.main_frame, text="Withdraw Amount:")
        self.withdraw_label.pack(side=tk.LEFT)
        self.withdraw_entry = tk.Entry(self.main_frame)
        self.withdraw_entry.pack(side=tk.LEFT)
        self.withdraw_button = tk.Button(self.main_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(side=tk.LEFT)
        self.deposit_label = tk.Label(self.main_frame, text="Deposit Amount:")
        self.deposit_label.pack(side=tk.LEFT)
        self.deposit_entry = tk.Entry(self.main_frame)
        self.deposit_entry.pack(side=tk.LEFT)
        self.deposit_button = tk.Button(self.main_frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack(side=tk.LEFT)
        self.change_pin_label = tk.Label(self.main_frame, text="New Pin:")
        self.change_pin_label.pack(side=tk.LEFT)
        self.change_pin_entry = tk.Entry(self.main_frame, show="*")
        self.change_pin_entry.pack(side=tk.LEFT)
        self.change_pin_button = tk.Button(self.main_frame, text="Change Pin", command=self.change_pin)
        self.change_pin_button.pack(side=tk.LEFT)
        self.main_frame.pack_forget()

    def login(self):
        if self.username_entry.get() == self.username and self.pin_entry.get() == self.pin:
            self.login_frame.pack_forget()
            self.main_frame.pack()
        else:
            messagebox.showerror("Error", "Invalid username or pin")

    def withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient balance")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", "Withdrawal successful")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            self.balance += amount
            messagebox.showinfo("Success", "Deposit successful")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def change_pin(self):
        new_pin = self.change_pin_entry.get()
        self.pin = new_pin
        messagebox.showinfo("Success", "Pin changed successfully")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    atm = ATM()
    atm.run()

