import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

class StudentManagement:
    def __init__(self):
        self.students = []
        self.window = tk.Tk()
        self.window.title("Student Management System")
        self.frame1 = tk.Frame(self.window)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.window)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.window)
        self.frame3.pack()
        self.frame4 = tk.Frame(self.window)
        self.frame4.pack()
        self.rollno_label = tk.Label(self.frame1, text="Roll No:")
        self.rollno_label.pack(side=tk.LEFT)
        self.rollno_entry = tk.Entry(self.frame1)
        self.rollno_entry.pack(side=tk.LEFT)
        self.name_label = tk.Label(self.frame2, text="Name:")
        self.name_label.pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.frame2)
        self.name_entry.pack(side=tk.LEFT)
        self.marks_label = tk.Label(self.frame3, text="Marks:")
        self.marks_label.pack(side=tk.LEFT)
        self.marks_entry = tk.Entry(self.frame3)
        self.marks_entry.pack(side=tk.LEFT)
        self.add_button = tk.Button(self.frame4, text="Add Student", command=self.add_student)
        self.add_button.pack(side=tk.LEFT)
        self.display_button = tk.Button(self.frame4, text="Display Students", command=self.display_students)
        self.display_button.pack(side=tk.LEFT)
        self.search_button = tk.Button(self.frame4, text="Search Student", command=self.search_student)
        self.search_button.pack(side=tk.LEFT)
        self.remove_button = tk.Button(self.frame4, text="Remove Student", command=self.remove_student)
        self.remove_button.pack(side=tk.LEFT)
        self.total_button = tk.Button(self.frame4, text="Total Students", command=self.total_students)
        self.total_button.pack(side=tk.LEFT)

    def add_student(self):
        rollno = self.rollno_entry.get()
        name = self.name_entry.get()
        marks = self.marks_entry.get()
        student = Student(rollno, name, marks)
        self.students.append(student)
        messagebox.showinfo("Success", "Student added successfully!")

    def display_students(self):
        result = ""
        for student in self.students:
            result += f"Roll No: {student.rollno}, Name: {student.name}, Marks: {student.marks}\n"
        messagebox.showinfo("Students", result)

    def search_student(self):
        rollno = self.rollno_entry.get()
        for student in self.students:
            if student.rollno == rollno:
                messagebox.showinfo("Student", f"Name: {student.name}, Marks: {student.marks}")
                return
        messagebox.showinfo("Error", "Student not found!")

    def remove_student(self):
        rollno = self.rollno_entry.get()
        for student in self.students:
            if student.rollno == rollno:
                self.students.remove(student)
                messagebox.showinfo("Success", "Student removed successfully!")
                return
        messagebox.showinfo("Error", "Student not found!")

    def total_students(self):
        messagebox.showinfo("Total Students", str(len(self.students)))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = StudentManagement()
    app.run()




