from tkinter import *
import sys
import os
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.geometry("822x718")
root.geometry("+350+35")
root.title("Running python scipt")
root.iconbitmap('images/bg.ico')
root.resizable(0,0)

def morse():
    root.destroy()
    os.system('python morse.py')
    
def hospital():
    root.destroy()
    os.system('python hospital.py')
    
def video():
    root.destroy()
    os.system('python video.py')
    
def new_lang():
    root.destroy()
    os.system('python new_lang.py')
    
img= ImageTk.PhotoImage(Image.open("images/img.png"))
img1= ImageTk.PhotoImage(Image.open("images/1.png"))
img2= ImageTk.PhotoImage(Image.open("images/2.png"))
img3= ImageTk.PhotoImage(Image.open("images/3.png"))
img4= ImageTk.PhotoImage(Image.open("images/4.png"))

lbl=Label(root,font=('courier new',17,'bold'),text="Blinky Blink",image=img,width=822,height=55,bd=10,fg='white',bg='#EFE2BA')
lbl.grid(row=0,column=0,columnspan=2)


bt1=Button(root,font=('courier new',17,'bold'),width=390,command=morse,image=img1,height=300,bd=10,fg='white',bg='#EFE2BA')
bt1.grid(row=1,column=0)
bt1.place(x=0,y=75)
bt2=Button(root,font=('courier new',17,'bold'),width=390,command=hospital,image=img2,height=300,bd=10,fg='white',bg='#EFE2BA')
bt2.grid(row=1,column=0)
bt2.place(x=410,y=75)
bt3=Button(root,font=('courier new',17,'bold'),width=390,command=video,image=img3,height=300,bd=10,fg='white',bg='#EFE2BA')
bt3.grid(row=1,column=0)
bt3.place(x=0,y=395)
bt4=Button(root,font=('courier new',17,'bold'),width=390,command=new_lang,image=img4,height=300,bd=10,fg='white',bg='#EFE2BA')
bt4.grid(row=1,column=0)
bt4.place(x=410,y=395)

root.mainloop()
