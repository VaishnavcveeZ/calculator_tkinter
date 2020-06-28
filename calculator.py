from tkinter import *
import tkinter.font as font
import time
s=0
ans=0
r=0
k=0
window=Tk()
window.configure(bg='#22324e')
window.title('CALCULATOR')
l=Label(window,text='CALCULATOR')
l.grid()

myfont=font.Font(family='Helvetica')
bfont=font.Font(size=15,weight='bold')

screen=Entry(window, font=myfont,bg='#0000ff',fg='#F4D03F',width=50,borderwidth=5)
screen.grid(row=1,column=0,columnspan=4,padx=10,pady=10,ipady=15)



def button_click(clk) :
    s=globals()['s']
    if s==1:
        screen.delete(0,END)
        globals()['s'] =0

    k=globals()['k']
    result=globals()['r']

    read=screen.get()
    screen.delete(0,END)
    screen.insert(0,str(read)+str(clk))
    num=screen.get()
    print('num'+num)
    if clk=='+' or clk=='-' or clk=='*' or clk=='/':
        if k=='+':
            result=float(result)+float(num[:-1])
            screen.delete(0, END)
            print('ADDED')
        if k=='-':
            result=float(result)-float(num[:-1])
            screen.delete(0, END)
            print('SUBTRACTED')
        if k=='x':
            result=float(result)*float(num[:-1])
            screen.delete(0, END)
            print('MUL.')
        if k=='/':
            result=float(result)/float(num[:-1])
            screen.delete(0, END)
            print('DIV')
        if k==0:
            result=float(num[:-1])
            print('else',result)
            k=num[-1]
            screen.delete(0, END)




    print('button clicked',num)
    globals()['k']=k
    globals()['r'] =result


def button_result():
    print('sum')
    num=screen.get()

    button_click('+')
    result=globals()['r']
    globals()['r']=result
    globals()['k']=0
    screen.insert(0, result)
    globals()['ans']=result

    globals()['r'] = 0
    globals()['s'] =1



def button_clr():
    now=screen.get()
    x=now[:-1]
    screen.delete(0,END)
    screen.insert(0,x)

def button_del():
    screen.delete(0,END)

def button_ans():
    screen.delete(0,END)
    ans=globals()['ans']
    screen.insert(0,ans)

def button_exit():
    window.destroy()


x=50 #padx of to keys
y=10 #pady of to keys
w1=5#border width of to line keys
w2=5 #border width of other keys


button_CLR=Button(window,text='CLR' ,font=bfont,borderwidth=w1 ,padx=45,pady=y,bg='#666699',command=button_clr).grid(row=3 ,column=0)
button_MOD=Button(window,text='ANS.' ,font=bfont,borderwidth=w1,padx=45,pady=y,bg='#666699',command=button_ans).grid(row= 3,column=1)
button_ON=Button(window,text='DEL' ,font=bfont,borderwidth=w1,padx=45,pady=y,bg='#666699',command=button_del).grid(row= 3,column=2)
button_OFF=Button(window,text='EXIT' ,font=bfont,borderwidth=w1,padx=35,pady=y,bg='#666699',fg='red',command=button_exit).grid(row=3 ,column=3)

button_7=Button(window,text='7' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('7')).grid(row= 4,column=0)
button_8=Button(window,text='8' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('8')).grid(row= 4,column=1)
button_9=Button(window,text='9' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('9')).grid(row= 4,column=2)
button_ADD=Button(window,text='+' ,font=bfont,borderwidth=w2,padx=67,pady=y,bg='#666699',command=lambda: button_click('+')).grid(row=4 ,column=3)

button_4=Button(window,text='4' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('4')).grid(row= 5,column=0)
button_5=Button(window,text='5' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('5')).grid(row= 5,column=1)
button_6=Button(window,text='6' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('6')).grid(row= 5,column=2)
button_SUB=Button(window,text='-' ,font=bfont,borderwidth=w1,padx=69,pady=y,bg='#666699',command=lambda: button_click('-')).grid(row=5 ,column=3)

button_1=Button(window,text='1' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('1')).grid(row= 6,column=0)
button_2=Button(window,text='2' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('2')).grid(row= 6,column=1)
button_3=Button(window,text='3' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('3')).grid(row= 6,column=2)
button_MUL=Button(window,text='x' ,font=bfont,borderwidth=w1,padx=67,pady=y,bg='#666699',command=lambda: button_click('x')).grid(row=6 ,column=3)

button_DOT=Button(window,text='.' ,font=bfont,borderwidth=w2,padx=52,pady=y,bg='#666699',command=lambda: button_click('.')).grid(row= 7,column=0)
button_0=Button(window,text='0' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#B22222',command=lambda: button_click('0')).grid(row= 7,column=1)
button_EQL=Button(window,text='=' ,font=bfont,borderwidth=w2,padx=x,pady=y,bg='#eeeeee',command=button_result).grid(row=7 ,column=2)
button_DIV=Button(window,text='/' ,font=bfont,borderwidth=w1,padx=69,pady=y,bg='#666699',command=lambda: button_click('/')).grid(row= 7,column=3)








window.mainloop()