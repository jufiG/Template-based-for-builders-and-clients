from tkinter import *
import tkinter.font as font
import tkinter as tk
import tkinter.messagebox

def mybuttonclick():
    
    tkinter.messagebox.showinfo('hello world','welcome')
    print('button called')

obj=Tk(className="arun")
obj.title("Login")
obj.geometry("700x500")

myFont = font.Font(family='Arial', size=30, weight='bold')
button = Button(obj, text='My Button')
#applying font to the button label
button['font'] = myFont
button.pack()

label1=Label(obj, text = "This is my new project in python!")
label1['font']=myFont
label1.pack()




mybutton= Button(obj, text='Click me',font = ("Bahnschrift", 14),command=(mybuttonclick()))
mybutton.pack()

mylabel= Label(obj,text='hello',font = ("Arial", 19))
mylabel.pack()

mylist= Listbox(obj)
mylist.insert(1,'my list 1')
mylist.insert(2,'my list 2')
mylist.insert(3,'my list 3')
mylist.pack()

mymessage=Menubutton(obj,text='welcome to python')
mymessage.pack()

myradiobutton=Radiobutton(obj, text='option 1',value=1)
myradiobutton.pack()
ourradiobutton=Radiobutton(obj, text='option 2',value=0)
ourradiobutton.pack()


obj.mainloop()



