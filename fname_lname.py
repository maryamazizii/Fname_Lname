from tkinter import *
import random
win=Tk()
y=win.winfo_screenheight()
x=win.winfo_screenwidth()
win.geometry(f'600x300+{x//2-300}+{y//2-150}')
win.title('my proje') 

lst_color='0123456789ABCDEF'
color='#'
for i in range (6):
    color+=random.choice(lst_color)
win.configure(background=color)
print(x,y) 

#=====function

def welcome ():
    fname=ent_welcom1.get()
    lname=ent_welcom2.get()
    lbl_welocm.configure(text=f'welcome {fname} {lname}')
    ent_welcom1.delete(0,END)
    ent_welcom2.delete(0,END)


#======widjet

lbl_fname=Label(win,text='fname :',font='Andalus 16 bold',foreground='black')
lbl_fname.place(x=30,y=10)
lbl_lname=Label(win,text='lname :',font='Andalus 16 bold',foreground='black')
lbl_lname.place(x=30,y=50)

btn_add=Button(win,text='add',font='Andaluse 8 bold',width=5,command=welcome)
btn_add.place(x=283,y=265)

ent_welcom1=Entry(win,width=30)
ent_welcom1.place(x=140,y=21)
ent_welcom2=Entry(win,width=30)
ent_welcom2.place(x=140,y=64)

lbl_welocm=Label(win,text='',font='arila 17 bold',foreground='blue')
lbl_welocm.place(x=30,y=150)

win.mainloop()
