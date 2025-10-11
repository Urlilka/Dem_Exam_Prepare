from tkinter import ttk, Tk
from tkinter.constants import SOLID, X

from Controllers.UserControllers import UserController

class AdminView(Tk):
    def __init__(self, user):
        super().__init__()
        self.user = UserController.show(user)

        self.title("Админ Панель")
        self.geometry("500x500")

        # Раздел добавления пользователя
        self.add_frame = ttk.Frame(
            self,
            borderwidth=1,
            relief=SOLID,
            padding=[8,10]
        )
        self.add_frame.pack(
            anchor="center",
            fill = X,
            padx = 10,
            pady = 10
        )
        self.add_title = ttk.Label(self.add_frame, text="Добавление новых пользователей")
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
    
    def Button_Clicked(self):
        """ Метод события при нажатии на кнопку
        Returns:

        """
        login = self.input_login.get() # из поля ввода login в переменную
        password = self.input_password.get() # из поля ввода password в переменную
        test_user = UserController.show(login)

        if login == "" or password == "":
            self.message["text"] = "Логин и/или пароль не введены"
        elif test_user:
            self.message["text"] = "Данный пользователь существует"
        else:
            UserController.add(login,password)
            self.message["text"] = "Пользователь добавлен"

if __name__ == "__main__":
    window = AdminView("admin")
    window.mainloop()