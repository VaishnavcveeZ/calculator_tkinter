from tkinter import *
window=Tk()
window.geometry('400x600')
l=Label(window,text='CALCULATOR').pack()
screen=Entry(window, width=60,)
screen.pack()

button=Button(window,text='' ,padx=40,pady=20,command=button_click).grid(row= ,column=)






window.mainloop()