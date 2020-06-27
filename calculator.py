from tkinter import *
window=Tk()

l=Label(window,text='CALCULATOR').grid()
screen=Entry(window, width=60,borderwidth=5)
screen.grid(row=1,column=0,columnspan=4,padx=5,pady=10)

def button_click() :
    print('button clicked')
x=40
y=20

button_CLR=Button(window,text='CLR' ,padx=x,pady=y,command=button_click).grid(row=3 ,column=0)
button_MOD=Button(window,text='%' ,padx=x,pady=y,command=button_click).grid(row= 3,column=1)
button_ON=Button(window,text='ON' ,padx=x,pady=y,command=button_click).grid(row= 3,column=2)
button_OFF=Button(window,text='OFF' ,padx=x,pady=y,command=button_click).grid(row=3 ,column=3)

button_7=Button(window,text='7' ,padx=x,pady=y,command=button_click).grid(row= 4,column=0)
button_8=Button(window,text='8' ,padx=x,pady=y,command=button_click).grid(row= 4,column=1)
button_9=Button(window,text='9' ,padx=x,pady=y,command=button_click).grid(row= 4,column=2)
button_ADD=Button(window,text='+' ,padx=x,pady=y,command=button_click).grid(row=4 ,column=3)

button_4=Button(window,text='4' ,padx=x,pady=y,command=button_click).grid(row= 5,column=0)
button_5=Button(window,text='5' ,padx=x,pady=y,command=button_click).grid(row= 5,column=1)
button_6=Button(window,text='6' ,padx=x,pady=y,command=button_click).grid(row= 5,column=2)
button_SUB=Button(window,text='-' ,padx=x,pady=y,command=button_click).grid(row=5 ,column=3)

button_1=Button(window,text='1' ,padx=x,pady=y,command=button_click).grid(row= 6,column=0)
button_2=Button(window,text='2' ,padx=x,pady=y,command=button_click).grid(row= 6,column=1)
button_3=Button(window,text='3' ,padx=x,pady=y,command=button_click).grid(row= 6,column=2)
button_MUL=Button(window,text='x' ,padx=x,pady=y,command=button_click).grid(row=6 ,column=3)

button_DOT=Button(window,text='.' ,padx=x,pady=y,command=button_click).grid(row= 7,column=0)
button_0=Button(window,text='0' ,padx=x,pady=y,command=button_click).grid(row= 7,column=1)
button_EQL=Button(window,text='=' ,padx=x,pady=y,command=button_click).grid(row=7 ,column=2)
button_DIV=Button(window,text='/' ,padx=x,pady=y,command=button_click).grid(row= 7,column=3)








window.mainloop()