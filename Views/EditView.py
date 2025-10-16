from tkinter import ttk,Tk
from tkinter import *

from Controllers.UserControllers import UserController


class EditView(Tk):
    def __init__(self, login):
        super().__init__()
        self.user = UserController.show(login)
        self.title(f"Рабочий стол: {login}")
        self.geometry("500x500")

        # Раздел добавления пользователей
        self.add_frame = ttk.Frame(
            self,
            borderwidth=1,
            relief= SOLID,
            height=450,
            padding=[8,10]
        )
        self.add_frame.pack(
            anchor="center",
            fill= X,
            padx=10,
            pady=10
        )

        self.add_frame.pack_propagate(0)

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
        self.message.pack(anchor="center",expand=1)

        # Кнопка
        self.button = ttk.Button(self.add_frame, text="изменить данные пользователя")
        self.button.pack(anchor="center",expand=1)
        self.button["command"] = self.Button_Clicked

        

        # Кнопка блокировки/разблокировки
        self.button_ban = ttk.Button(self.add_frame, text="Изменить данные блокировки")
        self.button_ban.pack(anchor="center")
        self.button_ban["command"] = self.Button_Ban
            
        # Сообщение бан кнопки
        if self.user.ban:
            self.ban_message = ttk.Label(self.add_frame, text="Блокировать")
        else:
            self.ban_message = ttk.Label(self.add_frame, text="Разблокировать")
        self.ban_message.pack(anchor="center")

        # Кнопка сброса даты
        self.button_undate = ttk.Button(self.add_frame, text="Сброс даты")
        self.button_undate.pack(anchor="center",expand=1)
        self.button_undate["command"] = self.Button_Undate

        # Кнопка выхода
        self.button_exit = ttk.Button(self.add_frame, text="Выход")
        self.button_exit.pack(anchor="center",expand=1)
        self.button_exit["command"] = self.Button_Exit
    
    def Button_Exit(self):
        self.destroy()

    def Button_Ban(self):
        UserController.update(self.user.id,ban = not self.user.ban)
        self.ban_message["text"] = "Изменено"

    def Button_Undate(self):
        UserController.update(self.user.id, date_auth = None)

    def Button_Clicked(self):
        login = self.input_login.get()
        password = self.input_password.get()

        if login != "":
            UserController.update(self.user.id,login=login)
        if password != "":
            UserController.update(self.user.id,password=password)

if __name__ == "__main__":
    window = EditView("admin")
    window.mainloop()
        