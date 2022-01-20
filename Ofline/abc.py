import tkinter
import sys
import os
window = tkinter.Tk()
window.title("Output")
window.geometry('800x300')
window.geometry("+500+300")
window.configure(bg='#ebf0fa')
# to rename the title of the window window.title("GUI")
f = open("text.txt", "r")
# pack is used to show the object in the window
b=f.read()
label1 = tkinter.Label(window, bg='#ebf0fa', text=" THE STRING IS :",bd=10,font=('arial',28,'bold'), width= 15, height=2).pack()
label2 = tkinter.Label(window, bg='#ebf0fa',text= b,bd=1,font=("Times 32"),  height=-5 ).pack()
#f = open(r"C:\xampp\htdocs\text.txt", "w")
#f.write(" **Incorrect input** ")
#f.close()
f.close()
def run1():
    window.destroy()
    os.system('python main.py')
def run2():
    window.destroy()
    
    
button1 = tkinter.Button(window, text="RUN AGAIN",bg='#005ce6', fg='#ffffff',width=9, height=1,font=('arial',15,'bold'),bd=10,command=run1)
button1.place(relx=1,x=-700,y=200)
button2 = tkinter.Button(window, text="QUIT",bg='#005ce6', fg='#ffffff',width=9, height=1,font=('arial',15,'bold'),bd=10,command=run2)
button2.place(relx=1,x=-200,y=200)
window.mainloop()
