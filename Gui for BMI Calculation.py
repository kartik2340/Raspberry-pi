import tkinter as tk
from tkinter.constants import LAST
from tkinter import *
#from tkinter import messagebox
root=Tk()
root.title('Sum of Numbers')
root.geometry('800x500')
output= Canvas(root,width = 300, height = 200)


def bmi():
    a= float(e1.get())
    b = float(e2.get())
    print(a)
    print(b)
    s=round(a/(b*b),2)
    T.delete("1.0","end")
    T.insert(tk.END, str(s))
    output.delete(1.0,END)
    #a=float(ent1.get())
    #b=float(ent2.get())
    #s=round(a/(b*b),2)
    #output.insert(1.0,str(s))
    bmi_index(s)

def bmi_index(s):
    if s < 18.5:
        canvas.create_image(
            50,
            10, 
            anchor=NW, 
            image=img
            )

        #messagebox.showinfo('bmi', f'BMI = {s} is Underweight')
    elif s> 18.5 and s < 24.9:
        canvas.create_image(
            50,
            10, 
            anchor=NW, 
            image=img1
            )

       #messagebox.showinfo('bmi', f'BMI = {s} is Normal')
    elif s > 24.9 and s < 29.9:
        canvas.create_image(
            50,
            10, 
            anchor=NW, 
            image=img2
            )
        #messagebox.showinfo('bmi', f'BMI = {s} is Overweight')
    else:
        canvas.create_image(
            50,
            10, 
            anchor=NW, 
            image=img3
            )
        #messagebox.showerror('b', 'something went wrong!')



e1 = tk.Entry(root,width=30)
e1.pack(pady=10)

e2 = tk.Entry(root,width=30)
e2.pack(pady=10)

T = tk.Text(root, height = 2, width = 10)
T.pack(pady=10)

btn1 = tk.Button(root,text="cal BMI",command=bmi)
btn1.pack(pady=10)
canvas = Canvas(
    root,
    width = 300, 
    height = 200
    )      
canvas.pack()      
img = PhotoImage(file='thin.png')      
img1 = PhotoImage(file='fit.png')
img2 = PhotoImage(file='fat.png')
img3 = PhotoImage(file='balls.png')
root.mainloop()
