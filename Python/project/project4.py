import tkinter as tk
import time

class DigitalClock:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Digital Clock")
        self.clock_label = tk.Label(self.window, font=('calibri', 40, 'bold'), background='black', foreground='green')
        self.clock_label.pack(fill='both', expand=1)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.window.after(1000, self.update_time)

    def run(self):
        self.update_time()
        self.window.mainloop()

if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()



