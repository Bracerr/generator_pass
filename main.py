import random
from tkinter import *
from tkinter import messagebox
import pyperclip as pc


def copy(a):
    pc.copy(a)
    messagebox.showinfo(title='Успех', message='Пароль успешно скопирован.')


def send():
    inputxt = lenghtpass.get()
    if inputxt.isdecimal():
        inputxt = int(inputxt)
        print("That's not an int!")
        string = '1234567890QERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
        password = ''
        for i in range(inputxt):
            password += random.choice(string)

        password_label = Label(frame, text=f'Ваш пароль: {password}')
        password_label.place(relx=0.5, rely=0.6, anchor='center', relheight=0.1)
        clp = Button(frame, border=4, text="Copy To Clipboard", bg='LightBlue1', command=lambda: copy(password))
        clp.place(x=175, y=250, anchor='center')
    else:
        messagebox.showerror(title='Ошибка', message='Введенное значение не является целочисленным.')

root = Tk()

root['bg'] = 'black'
root.title('Генератор паролей')
root.geometry('500x500')

frame = Frame(root, bg='gray')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)


title = Label(frame, text='Генератор паролей', font='Courier 14')
title.place(rely=0.05, relx=0.22)

lenghtpass = Entry(frame, bg='white', font='10')
lenghtpass.place(rely=0.2, relx=0.23)

info = Label(frame, text="Введите длину пароля", font='Courier 12')
info.place(rely=0.3, relx=0.2)

enter = Button(frame, text='Enter', font='Courier 12', command=send)
enter.place(relx=.5, rely=.5, anchor="center")

root.mainloop()
