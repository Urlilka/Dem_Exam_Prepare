from tkinter import ttk,Tk
from tkinter import *

from Controllers.UserControllers import UserController

from Views.EditView import EditView

class AdminView(Tk):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.title(f"Рабочий стол {user.login}")
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

        # Вывод всех пользователей и их изменения с помощью таблицы
        colums = ("login","password","ban","date_auth")
        self.users = ttk.Treeview(self, columns=colums, show="headings")
        self.users.pack(fill=BOTH,expand=1)

        self.table()
        self.users.bind("<<TreeviewSelect>>",self.item_selected)

    def item_selected(self, event):
        # Получить строку
        self.item = self.users.selection()[0]
        # Из строки взять логин пользователя
        self.user_date = self.users.item(self.item,"values")[0]
        # Передать логин в окно Изменения
        if self.user_date != "admin":
            window = EditView(self.user_date)

    def table(self):
        # Очистка таблицы при запуске программы
        for item in self.users.get_children():
            self.users.delete(item)
        
        # создаём список для записи пользователей
        list = UserController.get()
        user_list = []

        # переименовываем значения полей
        for user in list:
            # Поле бан
            if user.ban:
                # если есть бан - ДА
                ban = "Да"
            else:
                # Иначе - НЕТ
                ban = "Нет"

            # Поле входа
            if user.date_auth is None:
                # Если не входил - НЕ ВХОДИЛ
                date_auth = "Не входил"
            else:
                # Иначе указывается дата входа
                date_auth = user.date_auth
            
            # Подставка в список значений, включая переименованные
            user_list.append(
                (user.login,user.password,ban,date_auth)
            )

        # Переименование заголовковков
        self.users.heading("login",text="Логин")
        self.users.heading("password",text="Пароль")
        self.users.heading("ban",text="Заблокирован")
        self.users.heading("date_auth",text="Дата последней авторизации")

        # Вставка в таблицу
        for user in user_list:
            self.users.insert("",END,values=user)

    def Button_Clicked(self):
        login = self.input_login.get()
        password = self.input_password.get()
        test_user = UserController.show(login)
        
        if login == "" or password == "":
            self.message["text"] = "Логин и/или пароль не введены"
        elif test_user:
            self.message["text"] = "Данный пользователь существует"
        else:
            UserController.add(login,password)
            self.table()
            self.message["text"] = f"Пользователь {login} добавлен"

if __name__ == "__main__":
    admin = UserController.show("admin")
    window = AdminView(admin)
    window.mainloop()