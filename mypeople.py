from tkinter import *
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("My People")
        self.resizable(False, False)

        # Frames
        self.top = Frame(self,height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=500, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and data
        self.top_image = PhotoImage(file='./icons/book.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y = 10)
        self.heading = Label(self.top, text='My Address Book APP', font='arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        #ScrollBar
        self.sb = Scrollbar(self.bottomFrame,orient=VERTICAL)

        # Listbox
        self.listBox = Listbox(self.bottomFrame, width=35, height=31)
        self.listBox.grid(row=0, column=0, padx=(40,0))
        self.sb.config(command= self.listBox.yview)
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)

        # # Buttons
        btnadd = Button(self.bottomFrame, text='Add', width=12, font='Sans 12 bold')
        btnadd.grid(row=0, column=2, sticky=N, padx=10, pady=10)

        btnupdate = Button(self.bottomFrame, text='Update', width=12, font='Sans 12 bold')
        btnupdate.grid(row=0, column=2, sticky=N, padx=10, pady=50)

        btndisplay = Button(self.bottomFrame, text='Display', width=12, font='Sans 12 bold')
        btndisplay.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        btndelete = Button(self.bottomFrame, text='Delete', width=12, font='Sans 12 bold')
        btndelete.grid(row=0, column=2, sticky=N, padx=10, pady=130)
