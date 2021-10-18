from tkinter import *
from tkinter.ttk import *

master=Tk()

master.geometry("200x200")


def openNewWindow():
    newWindow=Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,text="This is a new Window").pack()

label=Label(master,text="This is the main window")
label.pack(pady=10)
btn=Button(master,text="CLick to open a new window",
command=openNewWindow)
btn.pack(pady=10)
mainloop()    