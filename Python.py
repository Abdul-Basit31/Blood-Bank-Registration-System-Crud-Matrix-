import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#connection
def connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root', 
        password='12345a',
        db='pro',
    )
    return conn
    
def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("BB BLOOD BANK")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM asarr")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    PatientID = str(PatientIDEntry.get())
    NAME = str(NAMEEntry.get())
    BloodGroup = str(BloodGroupEntry.get())
    BRANCH = str(BRANCHEntry.get())
    PHONE = str(PHONEEntry.get())

    if (PatientID == "" or PatientID == " ") or (NAME == "" or NAME == " ") or (BloodGroup == "" or BloodGroup == " ") or (BRANCH == "" or BRANCH == " ") or (PHONE == "" or PHONE == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO asarr VALUES ('"+PatientID+"','"+NAME+"','"+BloodGroup+"','"+BRANCH+"','"+PHONE+"') ")
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showinfo("Error", "Patient ID already exist")
            print(e)
            return

    refreshTable()
    

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM asarr")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM asarr WHERE PatientID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        PatientID = str(my_tree.item(selected_item)['values'][0])
        NAME = str(my_tree.item(selected_item)['values'][1])
        BloodGroup = str(my_tree.item(selected_item)['values'][2])
        BRANCH = str(my_tree.item(selected_item)['values'][3])
        PHONE = str(my_tree.item(selected_item)['values'][4])

        setph(PatientID,1)
        setph(NAME,2)
        setph(BloodGroup,3)
        setph(BRANCH,4)
        setph(PHONE,5)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    PatientID = str(PatientIDEntry.get())
    NAME = str(NAMEEntry.get())
    BloodGroup = str(BloodGroupEntry.get())
    BRANCH = str(BRANCHEntry.get())
    PHONE = str(PHONEEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM asarr WHERE PatientID='"+
    PatientID+"' or NAME='"+
    NAME+"' or BloodGroup='"+
    BloodGroup+"' or BRANCH='"+
    BRANCH+"' or PHONE='"+
    PHONE+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedPatientID = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedPatientID = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    PatientID = str(PatientIDEntry.get())
    NAME = str(NAMEEntry.get())
    BloodGroup = str(BloodGroupEntry.get())
    BRANCH = str(BRANCHEntry.get())
    PHONE = str(PHONEEntry.get())

    if (PatientID == "" or PatientID == " ") or (NAME == "" or NAME == " ") or (BloodGroup == "" or BloodGroup == " ") or (BRANCH == "" or BRANCH == " ") or (PHONE == "" or PHONE == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE asarr SET PatientID='"+
            PatientID+"', NAME='"+
            NAME+"', BloodGroup='"+
            BloodGroup+"', BRANCH='"+
            BRANCH+"', PHONE='"+
            PHONE+"' WHERE PatientID='"+
            selectedPatientID+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Patient ID already exist")
            return

    refreshTable()

label = Label(root, text="BB BLOOD BANK", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

PatientIDLabel = Label(root, text="Patient ID", font=('Arial', 15))
NAMELabel = Label(root, text="NAME", font=('Arial', 15))
BloodGroupLabel = Label(root, text="BloodGroup", font=('Arial', 15))
BRANCHLabel = Label(root, text="BRANCH", font=('Arial', 15))
PHONELabel = Label(root, text="PHONE", font=('Arial', 15))

PatientIDLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
NAMELabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
BloodGroupLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
BRANCHLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
PHONELabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

PatientIDEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
NAMEEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
BloodGroupEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
BRANCHEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
PHONEEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

PatientIDEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
NAMEEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
BloodGroupEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
BRANCHEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
PHONEEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Patient ID","NAME","Blood Group","BRANCH","PHONE")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Patient ID", anchor=W, width=170)
my_tree.column("NAME", anchor=W, width=150)
my_tree.column("Blood Group", anchor=W, width=150)
my_tree.column("BRANCH", anchor=W, width=165)
my_tree.column("PHONE", anchor=W, width=150)

my_tree.heading("Patient ID", text="Patient ID", anchor=W)
my_tree.heading("NAME", text="NAME", anchor=W)
my_tree.heading("Blood Group", text="Blood Group", anchor=W)
my_tree.heading("BRANCH", text="Branch", anchor=W)
my_tree.heading("PHONE", text="PHONE", anchor=W)

refreshTable()

root.mainloop()