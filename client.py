import socket
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap

def login():
    username = entry_login.get()
    password = entry_password.get()
    message = username+','+ password
    client.send(message.encode())
    data = client.recv(1024) 
    messagebox.showerror('Client-Успех!', data.decode())
    client.close()
    
client = socket.socket()            
hostname = socket.gethostname()     
port = 12345                     
client.connect((hostname, port))  
 
window = ttkbootstrap.Window(themename='darkly')
window.title('Авторазиция')
window.geometry('500x500+500+200')
 
 
def login():
    data_login = entry_login.get()
    data_password = entry_password.get()
    if data_login == 'admin' and data_password == 'admin':
        ttkbootstrap.dialogs.dialogs.Messagebox.ok('login good', 'u have entered')
 
 
def showpass():
    if entry_password['show'] == '*':
        entry_password['show'] = ''
    else:
        entry_password['show'] = '*'
 
 
ttkbootstrap.Label(window, text='Login:', bootstyle=ttkbootstrap.PRIMARY).pack(pady=20)
entry_login = ttkbootstrap.Entry(window, width=40, bootstyle=ttkbootstrap.PRIMARY)
entry_login.pack()
 
ttkbootstrap.Label(window, text='Password:', bootstyle=ttkbootstrap.PRIMARY).pack(pady=20)
entry_password = ttkbootstrap.Entry(window, width=40, show='*', bootstyle=ttkbootstrap.PRIMARY)
entry_password.pack()
ttkbootstrap.Button(window, text='show', bootstyle=ttkbootstrap.PRIMARY, command=showpass).place(x = 430, y = 160)
 
ttkbootstrap.Button(window, text='Sign in', bootstyle=ttkbootstrap.PRIMARY, command=login).pack(pady=20)
 
window.mainloop()