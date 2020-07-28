#Objective: Dynamically Copy & Rename Multiple Files
#Offered By: CAREERLABS TECHNOLOGIES PVT. LTD
#Release Data: 30-06-2020
#Last Update: 30-06-2020

import openpyxl
import os
import shutil
from tkinter import *
from tkinter import filedialog

# Capture main file to make copies 
def file_dialog():
    tempdir = filedialog.askopenfilename(parent=root, initialdir="./", title='Please Select a Document', filetypes=(("DOC files", "*.doc *.docx"), ("Any", "*.*")))
    main_name=str(tempdir).split("/")
    select_file.insert(0, main_name[len(main_name)-1])

# Capture the Excel file to create the new files
def file_xl():
    tempdir = filedialog.askopenfilename(parent=root, initialdir="./", title='Please Select Excel File', filetypes=(("XLSX files", "*.xlsx"), ("Any", "*.*")))
    xl_name=str(tempdir).split("/")
    select_xl.insert(0, xl_name[len(xl_name)-1])

# Start the process of making copies
def start_process():
    str(static_part.get())
    print(str(static_part.get()))
    createFiles()

# Stop the process after it's done 
def quit():
    root.destroy()

#Takes: start cell, end cell, and sheet you want to copy from.
def copyRange(startCol, startRow, endCol, endRow, sheet):
    rangeSelected = []
    #Loops through selected Rows
    for i in range(startRow,endRow + 1,1):
        #Appends the row to a RowSelected list
        rowSelected = []
        for j in range(startCol,endCol+1,1):
            rowSelected.append(sheet.cell(row = i, column = j).value)
        #Adds the RowSelected List and nests inside the rangeSelected
        rangeSelected.append(rowSelected)
 
    return rangeSelected

def createFiles():
    #New Folder Name
    folder = "Copied_Files"

    #File with file name data
    file_names = openpyxl.load_workbook(str(select_xl.get()))#Add the file name
    file_names_sheet = file_names['Sheet1']#Add the sheet name

    #Grab the file Template
    template = str(select_file.get())
    
    print('Processing...')

    #Make a foler for the files
    current_directory = os.getcwd()
    folder_n_path = os.path.join(current_directory,folder)
    print("Files saved to: "+folder_n_path)
    try:
        newFolder = os.makedirs(folder_n_path)
        
    except:
        print("Folder already exists")
        return

    #Get the Data to make the file names
    selectedRange = copyRange(1,2,2,int(rows_count.get())+1,file_names_sheet)
    print(selectedRange)
    #Loop through each row
    for i in selectedRange:
        print (i[0]+" "+i[1]+str(static_part.get()))
        file_name = str(static_part.get())+i[0]+"_"+i[1]+".docx"
        
        #Combine the file path with the new file name.
        combined_file_path = os.path.join(folder,file_name)
        print(combined_file_path)
        shutil.copy(template, combined_file_path)
    print('Done')
    quit()

# Tkinter design
root = Tk()
root.geometry('500x500')
root.title("Dynamically Copy & Rename Multiple Files")

label_0 = Label(root, text="Dynamically Copy & Rename Files",width=30,font=("bold", 20))
label_0.place(x=5,y=53)

label_1 = Label(root, text="Set Naming Convention",width=20,font=("bold", 10))
label_1.place(x=85,y=130)

static_part = Entry(root)
static_part.place(x=240,y=130)

label_2 = Label(root, text="Select Doc File",width=20,font=("bold", 10))
label_2.place(x=85,y=180)

select_file = Entry(root)
select_file.place(x=240,y=180)

Button(root, text='Browse',width=5,bg='black',fg='white', command = file_dialog).place(x=370,y=180)

label_3 = Label(root, text="Select Excel File",width=20,font=("bold", 10))
label_3.place(x=85,y=220)

select_xl = Entry(root)
select_xl.place(x=240,y=220)

Button(root, text='Browse',width=5,bg='black',fg='white', command = file_xl).place(x=370,y=220)

label_4 = Label(root, text="Number Of Names ?",width=20,font=("bold", 10))
label_4.place(x=85,y=260)

rows_count = Entry(root)
rows_count.place(x=240,y=260)

Button(root, text='Submit',width=20,bg='brown',fg='white', command = start_process).place(x=180,y=300)

root.mainloop()
