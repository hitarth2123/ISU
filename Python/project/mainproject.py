import tkinter as Project
from project1 import *
from project2 import *
from project3 import *
from project4 import *
from project5 import *



def open_project1():
   app= StudentManagement() 
   app.run()
   
def open_project2():
    atm = ATM()
    atm.run()
    
def open_project3():
    calculator = Calculator()
    calculator.run()
    
def open_project4():
   clock= DigitalClock()
   clock.run()

   

def open_project5():
    calculator = SimpleInterestCalculator()
    calculator.run()

root = Project.Tk()
root.title("Projects Of Python")

button_frame = Project.Frame(root)
button_frame.pack()

project1_button = Project.Button(button_frame, text="1.Student Management APP", command=open_project1)
project1_button.pack(side=Project.LEFT)

project2_button = Project.Button(button_frame, text="2.ATM Simulator", command=open_project2)
project2_button.pack(side=Project.LEFT)

project3_button = Project.Button(button_frame, text="3.Calculator", command=open_project3)
project3_button.pack(side=Project.LEFT)

project4_button = Project.Button(button_frame, text="4.Digital Clock", command=open_project4)
project4_button.pack(side=Project.LEFT)

project5_button = Project.Button(button_frame, text="5.Simple Interest Calculator", command=open_project5)
project5_button.pack(side=Project.LEFT)

root.mainloop()

