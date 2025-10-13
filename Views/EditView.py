from tkinter import ttk,Tk
from tkinter import *

from Controllers.UserControllers import UserController


class EditView(Tk):
    def __init__(self, login):
        super().__init__()
        self.login = login
        self.title(f"Рабочий стол {self.login}")
        self.geometry("800x500")

        # Раздел добавления пользователей
        self.add_frame = ttk.Frame(
            self,
            borderwidth=1,
            relief= SOLID,
            padding=[8,10]
        )
        self.add_frame.pack(
            anchor="center",
            fill= X,
            padx=10,
            pady=10
        )
        self.add_title = ttk.Label(
            self.add_frame, #отображение внутри фрейма add_frame
            text="Добавление новых пользователей"
        )
        self.add_title.pack()

        # Ввод логина
        self.title_login = ttk.Label(self.add_frame, text="Введите Логин")
        self.title_login.pack(anchor="center")

        self.input_login = ttk.Entry(self.add_frame)
        self.input_login.pack(anchor="center")

        # Пароль
        self.title_password = ttk.Label(self.add_frame, text="Введите пароль")
        self.title_password.pack(anchor="center")

        self.input_password = ttk.Entry(self.add_frame)
        self.input_password.pack(anchor="center")

        # Сообщение
        self.message = ttk.Label(self.add_frame, text="Введите логин и пароль")
        self.message.pack(anchor="center")

        # Кнопка
        self.button = ttk.Button(self.add_frame, text="Добавить пользователя")
        self.button.pack(anchor="center",expand=1)
        self.button["command"] = self.Button_Clicked

        if self.user.ban:
            ban_massage = "Разблокировать"
        else:
            ban_massage = "Блокировать"

        # Кнопка блокировки/разблокировки
        self.button_ban = ttk.Button(self.add_frame, text="Изменить данные блокировки")
        self.button_ban.pack(anchor="center")

        # Кнопка
        self.button = ttk.Button(self.add_frame, text="Сброс даты")
        self.button.pack(anchor="center",expand=1)
        self.button["command"] = self.Button_Undate


    def button_ban(self):
        UserController.update(self.user_id,ban = not self.user_ban)

    def Button_Undate(self):
        UserController.update(self.user_id, date_auth = None)

    def Button_Clicked(self):
        login = self.input_login.get()
        password = self.input_password.get()

        if login != "":
            UserController.update(self.user.id,login=login)
        if password != "":
            UserController.update(self.user.id,password=password)
        