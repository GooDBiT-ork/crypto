import socket
import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_login.get()
    password = entry_password.get()
    #button_login = tk.Button(root, text="Закрыть окно", command=lambda: root.destroy())
    message = [username, password]
    client.send(message.encode())
    data = client.recv(1024) 
    messagebox.showerror('Успех!', data.decode())
    client.close()
    
client = socket.socket()            # создаем сокет клиента
hostname = socket.gethostname()     # получаем хост локальной машины
port = 12345                        # устанавливаем порт сервера
client.connect((hostname, port))  
root = tk.Tk()
root.title('Регистрация')

label_login = tk.Label(root, text='Логин')
label_login.grid(row=0, column=0, padx=10, pady=10)

entry_login = tk.Entry(root)
entry_login.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text='Пароль')  
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show='*')
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_login = tk.Button(root, text='Войти', command=login)
button_login.grid(row=2, column=0, pady=10)
root.mainloop()  