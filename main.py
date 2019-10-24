from tkinter import *
import datetime

date = datetime.datetime.now().date()

class Application(object):
    def __init__(self, master):
        self.master =  master

        # Frames
        self.top = Frame(master,height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#adff2f')
        self.bottom.pack(fill=X)

        # Heading, image and data
        self.top_image = PhotoImage(file='./icons/book.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y = 10)
        self.heading = Label(self.top, text='My Address Book APP', font='arial 15 bold',
                             fg='#ffa500', bg='white')
        self.heading.place(x=260, y=60)
        self.date_lbl = Label(self.top, text="Today's date - " + str(date), font='arial 12 bold',
                                bg='white', fg='#ffa500')
        self.date_lbl.place(x=450, y=5)

        # First Button
        self.btn1Icon = PhotoImage(file='./icons/man.png')
        self.personBtn= Button(self.bottom, text='    My People    ', font='arial 12 bold')
        self.personBtn.config(image=self.btn1Icon, compound=LEFT)
        self.personBtn.place(x=250, y=10)

        # Second Button
        self.btn2Icon = PhotoImage(file='./icons/add.png')
        self.personBtn = Button(self.bottom, text='   Add People  ', font='arial 12 bold')
        self.personBtn.config(image=self.btn2Icon, compound=LEFT)
        self.personBtn.place(x=250, y=70)

        # Third Button
        self.btn3Icon = PhotoImage(file='icons/info.png')
        self.personBtn= Button(self.bottom, text='    About Us    ', font='arial 12 bold')
        self.personBtn.config(image=self.btn3Icon, compound=LEFT)
        self.personBtn.place(x=250, y=130)


def main():
    root = Tk()
    app = Application(root)
    root.title("Address Book App")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    main()
