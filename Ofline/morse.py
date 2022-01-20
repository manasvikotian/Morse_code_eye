
from tkinter import *
import sys
import os
from PIL import ImageTk,Image
from tkinter import filedialog

def morse_run():
    root.destroy()
    import globalfile
    import recog
    #os.system('python recog.py')
    temp = globalfile.conti
    if( temp == 1):
        os.system('python morse_run.py --shape-predictor shape_predictor_68_face_landmarks.dat')
        os.system('python abc.py')
    elif(temp == 0):
        os.system('python main.py')
def morse_open():
    global my_img
    top = Toplevel()
    top.title("Morse code")
    top.geometry("+930+35")
    my_img = ImageTk.PhotoImage(Image.open('images\morse.jpg'))
    my_label = Label(top,image=my_img).pack()
def back():
    root.destroy()
    os.system('python main.py')
    
root=Tk()
root.geometry("822x718")
root.geometry("+350+35")
root.title("Morse Code")
root.iconbitmap('images/bg.ico')
root.resizable(0,0)

top=Frame(root,width=822,height=60, bd=4,relief='raise')
top.pack(side=LEFT,pady=10)
top.place(x=0,y=0)

f1=Frame(root, bd=2,width=822,height=600, relief="raise",bg='#eeeeee')
f1.pack(side=LEFT)
f1.place(x=0,y=60)

f2=Frame(root, bd=2, relief="raise",width=822,height=100,bg='white')
f2.pack(side=LEFT)
f2.place(x=0,y=618)

lb1=Label(top,width=48,height=1,font=('Times new Roman',22,'bold'),text="MORSE CODE ",bd=10,bg='#EFE2BA',fg='#F13C20')
lb1.place(x=0,y=0)

lb1=Label(f1,font=('Times new Roman',23,'underline'),text="Morse code Image : ",bd=10,bg='#eeeeee',fg='black')
#lb1.grid(row=0,column=0,columnspan=6)
lb1.place(x=100,y=70)
bt1=Button(f1,font=('courier new',17,'bold'),text="CODE",command=morse_open,width=7,height=1,bd=10,fg='white',bg='#4056A1')
#bt1.grid(row=1,column=0)
bt1.place(x=359,y=150)
lb2=Label(f1,font=('Times new Roman',23,'underline'),text="Run the morse code program : ",bd=10,bg='#eeeeee',fg='black')
#lb2.grid(row=3,column=0)
lb2.place(x=100,y=280)
bt2=Button(f1,font=('courier new',17,'bold'),text="RUN",command=morse_run,width=7,height=1,bd=10,fg='white',bg='#4056A1')
#bt2.grid(row=4,column=0)
bt2.place(x=359,y=365)

#back= ImageTk.PhotoImage(Image.open("images/icon.png"))
bt3=Button(f2,font=('courier new',17,'bold'),text="Back",command=back,bd=10,fg='white',bg='#4056A1')
#bt3.grid(row=0,column=0)
bt3.place(x=10,y=17)

root.mainloop()
