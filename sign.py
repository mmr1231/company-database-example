from tkinter import *

from tkinter import ttk ,messagebox
import time
from db import Database
db =Database('data.db')


pro=Tk()
pro.geometry('1300x700+1+1')
pro.config(bg='#ffffff')

pro.title('mmr')
pro.resizable(False,False)




name=StringVar()
job=StringVar()
adress=StringVar()
age=StringVar()
mobile=StringVar()
email=StringVar()







fr1=Frame(pro,bg='#2C4644',width=350,height=700)
fr1.place(x=1,y=1)
#############################################################
lb1=Label(fr1,text=': تسجيل بيانات العملاء ',bg='#2C4644',font=' bold 25',fg='#ffffff')
lb1.place(x=80,y=20)
lb2=Label(fr1,text='الاســــــــم',bg='#2C4644',font=' bold 15',fg='#ffffff')
lb2.place(x=250,y=100)
lb3=Label(fr1,text='الـــوظيفـه',bg='#2C4644',font=' bold 15',fg='#ffffff')
lb3.place(x=250,y=140)
lb4=Label(fr1,text=' الـــــســن ',bg='#2C4644',font=' bold 15',fg='#ffffff')
lb4.place(x=250,y=180)
lb5=Label(fr1,text='الاميـــــــل',bg='#2C4644',font=' bold 15',fg='#ffffff')
lb5.place(x=250,y=220)
lb6=Label(fr1,text='رقـم التلفون   ' ,bg='#2C4644',font=' bold 15',fg='#ffffff')
lb6.place(x=250,y=260)
lb7=Label(fr1,text='الـــــــنوع   ' ,bg='#2C4644',font=' bold 15',fg='#ffffff')
lb7.place(x=250,y=300)
lb8=Label(fr1,text=':الــعنــــوان' ,bg='#2C4644',font=' bold 15',fg='#ffffff')
lb8.place(x=250,y=380)
#############################################################
en1=Entry(fr1,font='bold 15',textvariable=name)
en1.place(x=20 ,y=105,width=200,height=25)
en2=Entry(fr1,font='bold 15',textvariable=job)
en2.place(x=20 ,y=145,width=200,height=25)
en3=Entry(fr1,font='bold 15',textvariable=age)
en3.place(x=20 ,y=185,width=200,height=25)
en4=Entry(fr1,font='bold 15',textvariable=email)
en4.place(x=20 ,y=225,width=200,height=25)
en5=Entry(fr1,font='bold 15',textvariable=mobile)
en5.place(x=20 ,y=265,width=200,height=25)
combox=ttk.Combobox(fr1,values=('ذكر','انثي'),state='readonly',width=15,font='bold 15')
combox.place(x=20 ,y=300,width=200,height=25)
en6=Entry(fr1,font='bold 15',textvariable=adress)
en6.place(x=20 ,y=410,width=310,height=25)



##################################################################


##############################################################
fr2=Frame(pro,bg='#fff15f',width=900,height=680)
fr2.place(x=380 ,y=1 )
###########################################
def getdata(event):
    select=tv.focus()
    data=tv.item(select)
    global row
    row=data['values']
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    mobile.set(row[5])
    adress.set(row[6])





def clear():

    name.set("")
    age.set('')
    job.set('')
    email.set('')
    mobile.set('')
    adress.set('')   



def display():
    tv.delete(*tv.get_children()) 
    for  row in db.fatch():
        tv.insert('',END,values=row)


def dele ():
    db.romove(row[0])
    clear()
    display()

def update():
    if   en1.get()=="" or en2.get()=="" or en3.get()=="" or en4.get()=="" or en5.get()=="" or en6.get()=="":
        messagebox.showerror('خطأ','برحاء ادخال البيانات اولا')  
    db.update(row[0],
        en1.get(),
        en2.get(),
        en3.get(),
        en4.get(),
        en5.get(),
        en6.get()

              )
    clear()
    display()

def add ():
    if   en1.get()=="" and en2.get()=="" and en3.get()=="" and en4.get()=="" and en5.get()=="" and en6.get()=="":
        messagebox.showerror('خطأ','برحاء ادخال البيانات اولا')  
        return
    db.insert(
        en1.get(),
        en2.get(),
        en3.get(),
        en4.get(),
        en5.get(),
        en6.get()


    )
    messagebox.showinfo('تم','تم اضافه العميل بنجاح ')
    
    clear()
    display()






#####################################################
scrol=Scrollbar(pro,orient='vertical')
scrol.pack(side=RIGHT,fill=Y)
tv=ttk.Treeview(fr2,columns=(1,2,3,4,5,6,7),show='headings',yscrollcommand=scrol.set)
scrol.config(command=tv.yview)
tv.heading('1',text='مسلسل')
tv.column('1',width=5)
tv.heading('2',text='الاســـــــم')
tv.column('2',width=150)
tv.heading('3',text='الوظيفه')
tv.column('3',width=50)
tv.heading('4',text='السن')
tv.column('4',width=50)
tv.heading('5',text='الاميل')
tv.column('5',width=100)
tv.heading('6',text='التــلفـون')
tv.column('6',width=100)
tv.heading('7',text='الــــعنوان')
tv.column('7',width=150)
tv.bind('<ButtonRelease-1>',getdata)

tv.place(x=1,y=1,width=898,height=680)
########################################
def hiden():
    pro.geometry('350x680')

def show():
    pro.geometry('1300x680+100+1')

buhide=Button(fr1,text='اخفاء البيانات',cursor='hand2',command=hiden)
buhide.place(x=10,y=640)
bushow=Button(fr1,text='اظهار البيانات',cursor='hand2',command=show)
bushow.place(x=180,y=640)
###############################################################





#################################################
############################################################
bu1=Button(text='تسجيل البيانات',bg='#EC3200',
           command=add,fg='#ffffff',font='bold 20')
bu1.place(x=10,y=500)
bu1=Button(text='تعديل البيانات',bg='#EC3200',fg='#ffffff',font='bold 20',command=update)
bu1.place(x=180,y=500)
bu1=Button(text='افراغ البيانات',bg='#EC3200',command=clear,fg='#ffffff',font='bold 20')
bu1.place(x=10,y=580)
bu1=Button(text='حذف البيانات',bg='#EC3200',fg='#ffffff',font='bold 20',command=dele)
bu1.place(x=180,y=580)





display()
pro.mainloop()