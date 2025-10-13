from tkinter import ttk, Tk
from tkinter import *

class NewPasswordView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Смена пароля")
        self.geometry("500x200")


        # Старый Пароль
        self.title_old_password = ttk.Label(self, text="Введите старый пароль")
        self.title_old_password.pack(anchor="center")
        self.input_old_password = ttk.Entry(self)
        self.input_old_password.pack(anchor="center")

        # Новый Пароль
        self.title_new_password = ttk.Label(self, text="Введите новый пароль")
        self.title_new_password.pack(anchor="center")
        self.input_new_password = ttk.Entry(self)
        self.input_new_password.pack(anchor="center")

        # Подтвердить Новый Пароль
        self.title_confirm_new_password = ttk.Label(self, text="Введите новый пароль")
        self.title_confirm_new_password.pack(anchor="center")
        self.input_confirm_new_password = ttk.Entry(self)
        self.input_confirm_new_password.pack(anchor="center")

        # Сообщение
        self.message = ttk.Label(self, text="___")
        self.message.pack(anchor="center")

        # Кнопка
        self.button = ttk.Button(self, text="Изменить пароль")
        self.button.pack(anchor="center",expand=1)
        self.button["command"] = self.Button_Clicked
    

    def Button_Clicked(self):
        pass