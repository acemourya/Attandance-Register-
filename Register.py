from tkinter import Tk,StringVar,ttk
from tkinter import *
from tkinter import messagebox
import time;
import datetime

root=Tk()
root.title('Attandace Ragister')
root.geometry('1350x750+0+0')
root.configure(bg='black')
#------------------------------------Frames--------------------------------------------------

leftFrame=Frame(root,width=1000,height=850,bd=8,relief='raise')
leftFrame.pack(side=LEFT)
RightFrame=Frame(root,width=350,height=850,bd=8,relief='raise')
RightFrame.pack(side=RIGHT)

leftFrame1=Frame(leftFrame,width=1000,height=100,bd=8,relief='raise')
leftFrame1.pack(side=TOP)
leftFrame2=Frame(leftFrame,width=1000,height=750,bd=8,relief='raise')
leftFrame2.pack(side=TOP)

RightFrame1=Frame(RightFrame,width=350,height=315,bd=8,relief='raise')
RightFrame1.pack(side=TOP)
RightFrame2=Frame(RightFrame,width=350,height=435,bd=8,relief='raise')
RightFrame2.pack(side=TOP)

#------------------------------------Variables--------------------------------------------------

DateofOrder = StringVar()
value0= StringVar()
value1= StringVar()
value2= StringVar()
value3= StringVar()
value4= StringVar()
value5= StringVar()
value6= StringVar()
value7= StringVar()
value8= StringVar()
value9= StringVar()
value10= StringVar()
value11= StringVar()
value12= StringVar()
value13=StringVar()

def Mark_Ragister():
    if value0.get() == '/':
        value0.set('/')
        value1.set('/')
        value2.set('/')
        value3.set('/')
        value4.set('/')
        value5.set('/')
        value6.set('/')
        value7.set('/')
        value8.set('/')
        value9.set('/')
        value10.set('/')
        value11.set('/')
        value12.set('/')
        value13.set('/')
    elif (value0.get() == 'P'):
        value0.set('P')
        value1.set('P')
        value2.set('P')
        value3.set('P')
        value4.set('P')
        value5.set('P')
        value6.set('P')
        value7.set('P')
        value8.set('P')
        value9.set('P')
        value10.set('P')
        value11.set('P')
        value12.set('P')
        value13.set('P')
    elif (value0.get() == 'A'):
        value0.set('A')
        value1.set('A')
        value2.set('A')
        value3.set('A')
        value4.set('A')
        value5.set('A')
        value6.set('A')
        value7.set('A')
        value8.set('A')
        value9.set('A')
        value10.set('A')
        value11.set('A')
        value12.set('A')
        value13.set('A')
    elif (value0.get() == 'O'):
        value0.set('O')
        value1.set('O')
        value2.set('O')
        value3.set('O')
        value4.set('O')
        value5.set('O')
        value6.set('O')
        value7.set('O')
        value8.set('O')
        value9.set('O')
        value10.set('O')
        value11.set('O')
        value12.set('O')
        value13.set('O')
    elif (value0.get() == 'L'):
        value0.set('L')
        value1.set('L')
        value2.set('L')
        value3.set('L')
        value4.set('L')
        value5.set('L')
        value6.set('L')
        value7.set('L')
        value8.set('L')
        value9.set('L')
        value10.set('L')
        value11.set('L')
        value12.set('L')
        value13.set('L')
    else :
        value0.set('S')
        value1.set('S')
        value2.set('S')
        value3.set('S')
        value4.set('S')
        value5.set('S')
        value6.set('S')
        value7.set('S')
        value8.set('S')
        value9.set('S')
        value10.set('S')
        value11.set('S')
        value12.set('S')
        value13.set('S')

def Reset():
    value0.set('')
    value1.set('')
    value2.set('')
    value3.set('')
    value4.set('')
    value5.set('')
    value6.set('')
    value7.set('')
    value8.set('')
    value9.set('')
    value10.set('')
    value11.set('')
    value12.set('')
    value13.set('')

def QExit():
    qExit= messagebox.askyesno('Exit System','Do you want to quit?')
    if qExit > 0:
        root.destroy()
        return

#------------------------------------Variables--------------------------------------------------

cont = Canvas(RightFrame2,width=350,height=435 ,bg='black',)
cont.grid(row=0,column=0)
Collage_image=PhotoImage(file='government-University.png')
image= cont.create_image(10,0,image=Collage_image)

#------------------------------------Components--------------------------------------------------

DateofOrder.set(time.strftime('%d/%m/%Y'))

#------------------------------------Leftframe1--------------------------------------------------

lblNo=Label(leftFrame1,font=('arial',10,'bold'),text='No.',bd=16)
lblNo.grid(row=0,column=0,sticky=W)
lblStudentNo=Label(leftFrame1,font=('arial',10,'bold'),text='Student No.',bd=16)
lblStudentNo.grid(row=0,column=1,sticky=W)
lblStudentName=Label(leftFrame1,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=0,column=2,sticky=W)
lblCourseCode=Label(leftFrame1,font=('arial',10,'bold'),text='Course Code',bd=16)
lblCourseCode.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(leftFrame1,textvariable=value0,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=0,column=4)

btnArraw=Button(leftFrame1,text='Fill',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command= Mark_Ragister).grid(row=0,column=5)

btnReset=Button(leftFrame1,text='Reset',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1,command= Reset).grid(row=0,column=6)

btnExit=Button(leftFrame1,text='Exit',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1,command= QExit).grid(row=0,column=7)

lblDateofOrder=Label(leftFrame1,font=('arial',10,'bold'),text='Course Code',textvariable=DateofOrder,
                     padx=2,pady=2,fg='black',bg='white',relief='sunken')
lblDateofOrder.grid(row=0,column=8,sticky=W)

#------------------------------------Leftframe2,Row-1--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='01.',bd=16)
lblNo.grid(row=1,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=1,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=1,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=1,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value1,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=1,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=1,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=1,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=1,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=1,column=8)


#------------------------------------Leftframe2,Row-2--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='02.',bd=16)
lblNo.grid(row=2,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=2,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=2,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=2,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value2,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=2,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=2,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=2,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=2,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=2,column=8)

#------------------------------------Leftframe2,Row-3--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='03.',bd=16)
lblNo.grid(row=3,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=3,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=3,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=3,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value3,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=3,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=3,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=3,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=3,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=3,column=8)

#------------------------------------Leftframe2,Row-4--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='04.',bd=16)
lblNo.grid(row=4,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=4,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=4,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=4,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value4,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=4,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=4,column=8)

#------------------------------------Leftframe2,Row-5--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='05.',bd=16)
lblNo.grid(row=5,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=5,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=5,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=5,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value5,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=5,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=5,column=8)

#------------------------------------Leftframe2,Row-6--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='06.',bd=16)
lblNo.grid(row=6,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=6,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=6,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=6,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value6,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=6,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=6,column=8)

#------------------------------------Leftframe2,Row-7--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='07.',bd=16)
lblNo.grid(row=7,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=7,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=7,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=7,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value7,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=7,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=7,column=8)

#------------------------------------Leftframe2,Row-8--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='08.',bd=16)
lblNo.grid(row=8,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=8,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=8,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=8,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value8,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=8,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=8,column=8)

#------------------------------------Leftframe2,Row-9--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='09.',bd=16)
lblNo.grid(row=9,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=9,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=9,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=9,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value9,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=9,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=9,column=8)

#------------------------------------Leftframe2,Row-10--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='10.',bd=16)
lblNo.grid(row=10,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=10,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=10,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value10,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=10,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=10,column=8)

#------------------------------------Leftframe2,Row-11--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='11.',bd=16)
lblNo.grid(row=11,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716',bd=16)
lblStudentNo.grid(row=11,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=11,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=11,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value11,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=11,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=11,column=8)

#------------------------------------Leftframe2,Row-12--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='12.',bd=16)
lblNo.grid(row=12,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716.',bd=16)
lblStudentNo.grid(row=12,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=12,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=12,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value12,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=12,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=12,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=12,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=12,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=12,column=8)

#------------------------------------Leftframe2,Row-13--------------------------------------------------

lblNo=Label(leftFrame2,font=('arial',10,'bold'),text='13.',bd=16)
lblNo.grid(row=13,column=0,sticky=W)
lblStudentNo=Label(leftFrame2,font=('arial',10,'bold'),text='   55302716.',bd=16)
lblStudentNo.grid(row=13,column=1,sticky=W)
lblStudentName=Label(leftFrame2,font=('arial',10,'bold'),text='Student Name',bd=16)
lblStudentName.grid(row=13,column=2,sticky=W)
lblCourseCode=Label(leftFrame2,font=('arial',10,'bold'),text='CSE/16/   ',bd=16)
lblCourseCode.grid(row=13,column=3,sticky=W)

box=ttk.Combobox(leftFrame2,textvariable=value13,state='readonly')
box['value']=(' ','P','A','O','L','S')
box.current(0)
box.grid(row=13,column=4)

btnArraw=Button(leftFrame2,text=' ',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=13,column=5)

btnReset=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
                font=('arial',10,'bold'),width=12,height=1).grid(row=13,column=6)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=13,column=7)

btnExit=Button(leftFrame2,text='',padx=2,pady=2,fg='black',
               font=('arial',10,'bold'),width=12,height=1).grid(row=13,column=8)



root.mainloop()