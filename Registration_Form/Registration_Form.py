from tkinter import *
from tkinter import filedialog

def save_info():
    full_name = entry_1.get()
    email = entry_2.get()
    gender = ""
    subject = {}
    count = 0
    print(full_name)
    print(email)
    if var.get()== 1:
        gender = "Male"
    else:
        gender = "Female"
    print(gender)
    print(c.get())
    if var1.get():
        subject[count] = "Java"
        count = count + 1
    else:
        subject[count] = "None"
        count = count + 1
    if var2.get():
        subject[count] = "Python"
        count = count + 1
    else:
        subject[count] = "None"
        count = count + 1
    print(subject)

    # if len(tempdir) > 0:
    #     print("You chose %s" % tempdir)

    entry_1.delete(0, END)
    entry_2.delete(0, END)
    var.set(0)
    var1.set(0)
    var2.set(0)
    c.set("select your country")

def file_dialog():
    tempdir = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
    entry_3.insert(0, str(tempdir))

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var1 = IntVar()
Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(root, text="python", variable=var2).place(x=290,y=330)

label_5 = Label(root, text="Brose FIle Path",width=20,font=("bold", 10))
label_5.place(x=85,y=380)

entry_3 = Entry(root)
entry_3.place(x=240,y=380)

Button(root, text='Browse',width=5,bg='black',fg='white', command = file_dialog).place(x=370,y=380)

Button(root, text='Submit',width=20,bg='brown',fg='white', command = save_info).place(x=180,y=440)

root.mainloop()
