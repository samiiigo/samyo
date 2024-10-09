from customtkinter import *

def add():
    s1 = n1.get()
    s2 = n2.get()
    ans.configure(text=s1+s2)

root = CTk()

CTkLabel(root,text='CALCULATOR',font=('Calibri',20,'bold')).pack(padx=20,pady=17)

CTkLabel(root,text='Number 1',font=('Calibri',13)).pack(padx=20,pady=5)
n1 = CTkEntry(root,placeholder_text='Enter Number',width=250)
n1.pack(padx=20,pady=5)

CTkLabel(root,text='Number 2',font=('Calibri',13)).pack(padx=20,pady=5)
n2 = CTkEntry(root,placeholder_text='Enter Number',width=250)
n2.pack(padx=20,pady=5)

CTkButton(root,text='Add',command=lambda:add()).pack(padx=20,pady=7)

fr = CTkFrame(root)
fr.pack(padx=20,pady=20)
CTkLabel(fr,text='Answer',width=250,font=('Calibri',15,'bold')).pack(padx=20,pady=10)
ans = CTkLabel(fr,text='')
ans.pack(padx=20,pady=11)

root.mainloop()