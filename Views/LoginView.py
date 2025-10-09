from tkinter import ttk, Tk
from Controllers.UserControllers import UserController


class LoginView(Tk):
    """ Класс для создания окна Авторизации
    """
    def __init__(self):
        super().__init__()
        self.title("Вход в систему")
        self.geometry("500x300")

        # Логин
        self.title_login = ttk.Label(self, text="Логин")
        self.title_login.pack(anchor="center")

        self.input_login = ttk.Entry(self)
        self.input_login.pack(anchor="center")

        # Пароль
        self.title_password = ttk.Label(self, text="Введите пароль")
        self.title_password.pack(anchor="center")

        self.input_password = ttk.Entry(self)
        self.input_password.pack(anchor="center")

        # Сообщение
        self.message = ttk.Label(self, text="Вставить нужное")
        self.message.pack(anchor="center")

        # Кнопка
        self.button = ttk.Button(self, text="Войти")
        self.button.pack(anchor="center",expand=1)
        self.button["command"] = self.Button_Clicked

        # Словарь подсчёта попыток входа
        self.count_error = {}

    def Button_Clicked(self):
        """Метод события при нажатии на кнопку

        Returns:
            message(str): Сообщение пользователю.
            count_error(list): Подсчёт неверных попыток входа, далее изменение записи ban(boolean) в БД

        """

        login = self.input_login.get() #Из поля login в переменную
        password = self.input_password.get() # из поля password в переменную
        user = UserController.auth(login,password)
        if login == "" or password == "":
            self.message["text"] = "Введите логин и пароль"
        elif user:
            self.message["text"] = f" Здравствуйте {login}"
        else:
            self.message["text"] = f"Вы ввели неверный логин или пароль,\nпожалуйста проверьте введёные данные"

        test_user = UserController.show(login)
        # Проверка введённого логина
        if test_user is not None:
            if login not in self.count_error:
                self.count_error[login] = 0 # добавить в словарь ключ-значение {user:0}
            self.count_error[login] += 1
            if self.count_error[login] >= 3:
                UserController.update(test_user.id,ban = 1)
            if user:
                self.count_error[login] = 0
        print(self.count_error)



if __name__ == "__main__":
    window = LoginView()
    window.mainloop()