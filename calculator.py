from tkinter import *
window=Tk()

l=Label(window,text='CALCULATOR')
l.grid()
screen=Entry(window, width=60,borderwidth=5)
screen.grid(row=1,column=0,columnspan=4,padx=10,pady=10,ipady=15)

def button_click(clk) :
    print('button clicked',clk)
x=40
y=20
w1=5
w2=3

button_CLR=Button(window,text='CLR' ,borderwidth=w1 ,padx=x,pady=y,command=lambda: button_click(100)).grid(row=3 ,column=0)
button_MOD=Button(window,text='%' ,borderwidth=w1,padx=x,pady=y,command=lambda: button_click(101)).grid(row= 3,column=1)
button_ON=Button(window,text='ON' ,borderwidth=w1,padx=x,pady=y,command=lambda: button_click(102)).grid(row= 3,column=2)
button_OFF=Button(window,text='OFF' ,borderwidth=w1,padx=x,pady=y,command=lambda: button_click(103)).grid(row=3 ,column=3)

button_7=Button(window,text='7' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(7)).grid(row= 4,column=0)
button_8=Button(window,text='8' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(8)).grid(row= 4,column=1)
button_9=Button(window,text='9' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(9)).grid(row= 4,column=2)
button_ADD=Button(window,text='+' ,borderwidth=w1,padx=50,pady=y,command=lambda: button_click(104)).grid(row=4 ,column=3)

button_4=Button(window,text='4' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(4)).grid(row= 5,column=0)
button_5=Button(window,text='5' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(5)).grid(row= 5,column=1)
button_6=Button(window,text='6' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(6)).grid(row= 5,column=2)
button_SUB=Button(window,text='-' ,borderwidth=w1,padx=50,pady=y,command=lambda: button_click(105)).grid(row=5 ,column=3)

button_1=Button(window,text='1' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(1)).grid(row= 6,column=0)
button_2=Button(window,text='2' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(2)).grid(row= 6,column=1)
button_3=Button(window,text='3' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(3)).grid(row= 6,column=2)
button_MUL=Button(window,text='x' ,borderwidth=w1,padx=50,pady=y,command=lambda: button_click(106)).grid(row=6 ,column=3)

button_DOT=Button(window,text='.' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(107)).grid(row= 7,column=0)
button_0=Button(window,text='0' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(108)).grid(row= 7,column=1)
button_EQL=Button(window,text='=' ,borderwidth=w2,padx=x,pady=y,command=lambda: button_click(109)).grid(row=7 ,column=2)
button_DIV=Button(window,text='/' ,borderwidth=w1,padx=50,pady=y,command=lambda: button_click(110)).grid(row= 7,column=3)








window.mainloop()