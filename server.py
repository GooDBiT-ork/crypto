# import hashlib
# from cryptography.fernet import Fernet
# import tkinter as tk
# from tkinter import messagebox

# # Словарь для хранения данных о пользователях
# users = {'user1': {'password': '202cb962ac59075b964b07152d234b70', 
#                   'info': 'Информация о пользователе 1'},
#          'user2': {'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 
#                   'info': 'Информация о пользователе 2'}}

# # Ключ для шифрования данных          
# key = Fernet.generate_key()
# fernet = Fernet(key)

# def encrypt(data):
#     return fernet.encrypt(data.encode())

# def decrypt(data):
#     return fernet.decrypt(data).decode()
    
# # Функция для входа в систему    
# def login():
#     username = entry_login.get()
#     password = entry_password.get()
    
#     # Хеширование пароля
#     hash_object = hashlib.sha256(password.encode())
#     hashed_password = hash_object.hexdigest()
    
#     # Проверка логина и пароля
#     if (username in users) == False:
#         users[username] = {'password':hashlib.sha256(password.encode()).hexdigest(), 'info':'default'}
#         messagebox.showinfo('Успех', 'Вы успешно зарегистрировались')
#         encrypted_data = users[username]['info']
#         decrypted_data = decrypt(encrypted_data)
        
#         text_info['state'] = 'normal'
#         text_info.delete(1.0, tk.END)
#         text_info.insert(tk.END, decrypted_data)
#         text_info['state'] = 'disabled'
        
#         button_login['state'] = 'disabled'
#         button_update['state'] = 'normal'  
#     elif username in users and users[username]['password'] == hashed_password:
#         messagebox.showinfo('Успех', 'Вы успешно вошли в систему')
        
#         # Загрузка и дешифрование данных о пользователе
#         encrypted_data = users[username]['info']
#         decrypted_data = decrypt(encrypted_data)
        
#         text_info['state'] = 'normal'
#         text_info.delete(1.0, tk.END)
#         text_info.insert(tk.END, decrypted_data)
#         text_info['state'] = 'disabled'
        
#         button_login['state'] = 'disabled'
#         button_update['state'] = 'normal'   
#     else:
#         messagebox.showerror('Ошибка', 'Неверный логин или пароль')
        
# # Функция для обновления данных        
# def update():
#     username = entry_login.get()
#     data = text_info.get(1.0, tk.END)
    
#     # Шифрование обновленных данных
#     encrypted_data = encrypt(data) 
#     users[username]['info'] = encrypted_data
    
#     messagebox.showinfo('Успех', 'Данные успешно обновлены')
    
# # Создание графического интерфейса
# root = tk.Tk()
# root.title('Программа')

# label_login = tk.Label(root, text='Логин')
# label_login.grid(row=0, column=0, padx=10, pady=10)

# entry_login = tk.Entry(root)
# entry_login.grid(row=0, column=1, padx=10, pady=10)

# label_password = tk.Label(root, text='Пароль')  
# label_password.grid(row=1, column=0, padx=10, pady=10)

# entry_password = tk.Entry(root, show='*')
# entry_password.grid(row=1, column=1, padx=10, pady=10)

# button_login = tk.Button(root, text='Войти', command=login)
# button_login.grid(row=2, column=0, pady=10)

# text_info = tk.Text(root, width=50, height=10, state='disabled')
# text_info.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# button_update = tk.Button(root, text='Обновить', state='disabled', command=update)
# button_update.grid(row=4, column=0, pady=10)

# root.mainloop()

# импортируем библиотеку tkinter всю сразу
# from tkinter import *
# from tkinter import messagebox

# # главное окно приложения
# window = Tk()
# # заголовок окна
# window.title('Авторизация')
# # размер окна
# window.geometry('450x230')
# # можно ли изменять размер окна - нет
# window.resizable(False, False)

# # кортежи и словари, содержащие настройки шрифтов и отступов
# font_header = ('Arial', 15)
# font_entry = ('Arial', 12)
# label_font = ('Arial', 11)
# base_padding = {'padx': 10, 'pady': 8}
# header_padding = {'padx': 10, 'pady': 12}


# # обработчик нажатия на клавишу 'Войти'
# def clicked():

#     # получаем имя пользователя и пароль
#     username = username_entry.get()
#     password = password_entry.get()

#     # выводим в диалоговое окно введенные пользователем данные
#     messagebox.showinfo('Заголовок', '{username}, {password}'.format(username=username, password=password))


# # заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# # для всех остальных виджетов настройки делаются также
# main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
# # помещаем виджет в окно по принципу один виджет под другим
# main_label.pack()

# # метка для поля ввода имени
# username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
# username_label.pack()

# # поле ввода имени
# username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
# username_entry.pack()

# # метка для поля ввода пароля
# password_label = Label(window, text='Пароль', font=label_font , **base_padding)
# password_label.pack()

# # поле ввода пароля
# password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
# password_entry.pack()

# # кнопка отправки формы
# send_btn = Button(window, text='Войти', command=clicked)
# send_btn.pack(**base_padding)


# # запускаем главный цикл окна
# window.mainloop()

import socket
from _thread import *
import tkinter as tk
from tkinter import messagebox
 
# функция для обработки каждого клиента
def client_thread (con):
    data = con.recv(1024)           # получаем данные от клиента
    message = data.decode()         # преобразуем байты в строку
    messagebox.showerror('Server-Успех!', message)
    con.send('Данные приняты'.encode())      # отправляем сообщение клиенту
    con.close()                     # закрываем подключение
 
server = socket.socket()            # создаем объект сокета сервера
hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 12345                        # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений
 
print("Server running")
while True:
    client, _ = server.accept()     # принимаем клиента
    start_new_thread(client_thread, (client, ))     # запускаем поток клиента