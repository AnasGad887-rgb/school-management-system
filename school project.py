import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

#  Database Functions 
def init_db():
    conn=sqlite3.connect("school.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        phone TEXT,
                        grade INTEGER,
                        student_class TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS teachers (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        phone TEXT,
                        subject TEXT,
                        salary REAL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        person_id TEXT,
                        role TEXT,
                        comment TEXT)""")
    conn.commit()
    conn.close()

def add_student_to_db(s):
    conn=sqlite3.connect("school.db")
    cursor=conn.cursor()
    cursor.execute("""INSERT OR REPLACE INTO students (id,name,age,phone,grade,student_class)
                      VALUES (?,?,?,?,?,?)""",
                   (s.id,s.name,s.age,s.phone,s.grade,s.student_class))
    conn.commit()
    conn.close()

def add_teacher_to_db(t):
    conn=sqlite3.connect("school.db")
    cursor=conn.cursor()
    cursor.execute("""INSERT OR REPLACE INTO teachers (id,name,age,phone,subject,salary)
                      VALUES (?,?,?,?,?,?)""",
                   (t.id,t.name,t.age,t.phone,t.subject,t.salary))
    conn.commit()
    conn.close()

def add_feedback(person_id,role,comment):
    conn=sqlite3.connect("school.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO feedback (person_id,role,comment) VALUES (?,?,?)",
                   (person_id,role,comment))
    conn.commit()
    conn.close()

def load_students():
    conn=sqlite3.connect("school.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY id")
    rows=cursor.fetchall()
    conn.close()
    return rows

def load_teachers():
    conn=sqlite3.connect("school.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM teachers ORDER BY id")
    rows=cursor.fetchall()
    conn.close()
    return rows

def load_feedback():
    conn=sqlite3.connect("school.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM feedback ORDER BY id DESC")
    rows=cursor.fetchall()
    conn.close()
    return rows

#  Classes 
class Student:
    def __init__(self,id,name,age,phone,grade,student_class):
        self.id=id
        self.name=name
        self.age=age
        self.phone=phone
        self.grade=grade
        self.student_class=student_class
        self.grades={}

    def add_grade(self,subject,grade):
        if 0<=grade<=100:
            self.grades[subject]=grade

    def average(self):
        return sum(self.grades.values())/len(self.grades) if self.grades else 0

class Teacher:
    def __init__(self,id,name,age,phone,subject,salary):
        self.id=id
        self.name=name
        self.age=age
        self.phone=phone
        self.subject=subject
        self.salary=salary
        self.classes=[]

# GUI
class SchoolGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("School Management System")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root,text="Bright Future School",font=("Arial",24,"bold"),
                 bg="#f0f0f0",fg="#2c3e50").pack(pady=20)

        frame=tk.Frame(self.root,bg="#f0f0f0")
        frame.pack(pady=10)

        tk.Button(frame,text="Add Student",width=18,bg="#3498db",fg="white",
                  command=self.add_student_window).grid(row=0,column=0,padx=5,pady=5)
        tk.Button(frame,text="Add Teacher",width=18,bg="#e67e22",fg="white",
                  command=self.add_teacher_window).grid(row=0,column=1,padx=5,pady=5)
        tk.Button(frame,text="Show Students",width=18,bg="#9b59b6",fg="white",
                  command=self.show_students).grid(row=0,column=2,padx=5,pady=5)
        tk.Button(frame,text="Show Teachers",width=18,bg="#1abc9c",fg="white",
                  command=self.show_teachers).grid(row=1,column=0,padx=5,pady=5)
        tk.Button(frame,text="Add Feedback",width=18,bg="#f39c12",fg="white",
                  command=self.add_feedback_window).grid(row=1,column=1,padx=5,pady=5)
        tk.Button(frame,text="Show Feedback",width=18,bg="#95a5a6",fg="white",
                  command=self.show_feedback).grid(row=1,column=2,padx=5,pady=5)

    #  Student Window
    def add_student_window(self):
        win=tk.Toplevel(self.root)
        win.title("Add Student")
        win.geometry("400x400")
        labels=["ID","Name","Age","Phone","Grade","Class"]
        entries={}
        for l in labels:
            tk.Label(win,text=l).pack()
            e=tk.Entry(win)
            e.pack()
            entries[l]=e

        def add_student_action():
            s=Student(entries["ID"].get(),entries["Name"].get(),int(entries["Age"].get()),
                      entries["Phone"].get(),int(entries["Grade"].get()),entries["Class"].get())
            add_student_to_db(s)
            messagebox.showinfo("Success",f"Student {s.name} added!")
            win.destroy()

        tk.Button(win,text="Add Student",bg="#3498db",fg="white",command=add_student_action).pack(pady=10)

    # Teacher Window 
    def add_teacher_window(self):
        win=tk.Toplevel(self.root)
        win.title("Add Teacher")
        win.geometry("400x400")
        labels=["ID","Name","Age","Phone","Subject","Salary"]
        entries={}
        for l in labels:
            tk.Label(win,text=l).pack()
            e=tk.Entry(win)
            e.pack()
            entries[l]=e

        def add_teacher_action():
            t=Teacher(entries["ID"].get(),entries["Name"].get(),int(entries["Age"].get()),
                      entries["Phone"].get(),entries["Subject"].get(),float(entries["Salary"].get()))
            add_teacher_to_db(t)
            messagebox.showinfo("Success",f"Teacher {t.name} added!")
            win.destroy()

        tk.Button(win,text="Add Teacher",bg="#e67e22",fg="white",command=add_teacher_action).pack(pady=10)

    # Show Students 
    def show_students(self):
        win=tk.Toplevel(self.root)
        win.title("All Students")
        win.geometry("600x400")
        tree=ttk.Treeview(win)
        tree["columns"]=("ID","Name","Age","Phone","Grade","Class","Average")
        tree.heading("#0",text="")
        tree.column("#0",width=0)
        for col in tree["columns"]:
            tree.heading(col,text=col)
            tree.column(col,width=80)
        tree.pack(fill="both",expand=True)
        for r in load_students():
            s=Student(*r)
            tree.insert("", "end", values=(s.id,s.name,s.age,s.phone,s.grade,s.student_class,f"{s.average():.2f}"))

    #  Show Teachers 
    def show_teachers(self):
        win=tk.Toplevel(self.root)
        win.title("All Teachers")
        win.geometry("600x400")
        tree=ttk.Treeview(win)
        tree["columns"]=("ID","Name","Age","Phone","Subject","Salary")
        tree.heading("#0",text="")
        tree.column("#0",width=0)
        for col in tree["columns"]:
            tree.heading(col,text=col)
            tree.column(col,width=90)
        tree.pack(fill="both",expand=True)
        for r in load_teachers():
            tree.insert("", "end", values=r)

    #  Feedback 
    def add_feedback_window(self):
        win=tk.Toplevel(self.root)
        win.title("Add Feedback")
        win.geometry("400x300")
        tk.Label(win,text="Person ID").pack()
        id_entry=tk.Entry(win); id_entry.pack()
        tk.Label(win,text="Role (Student/Teacher)").pack()
        role_entry=tk.Entry(win); role_entry.pack()
        tk.Label(win,text="Comment").pack()
        comment_entry=tk.Text(win,height=5); comment_entry.pack()
        def save_feedback():
            add_feedback(id_entry.get(),role_entry.get(),comment_entry.get("1.0",tk.END).strip())
            messagebox.showinfo("Success","Feedback added!")
            win.destroy()
        tk.Button(win,text="Add Feedback",bg="#f39c12",fg="white",command=save_feedback).pack(pady=10)

    def show_feedback(self):
        win=tk.Toplevel(self.root)
        win.title("All Feedback")
        win.geometry("600x400")
        tree=ttk.Treeview(win)
        tree["columns"]=("ID","Person ID","Role","Comment")
        tree.heading("#0",text="")
        tree.column("#0",width=0)
        for col in tree["columns"]:
            tree.heading(col,text=col)
            tree.column(col,width=120)
        tree.pack(fill="both",expand=True)
        for r in load_feedback():
            tree.insert("", "end", values=r)

# Main 
if __name__=="__main__":
    init_db()
    root=tk.Tk()
    app=SchoolGUI(root)
    root.mainloop()
