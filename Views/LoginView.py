from tkinter import ttk, Tk
from Controllers.UserControllers import UserController

from Views.AdminView import AdminView
from Views.NewPasswordView import NewPasswordView


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
        self.message = ttk.Label(self, text="Введите логин и пароль")
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
            self.message["text"] = "Логин и/или пароль не введены"

        else:
            if not user:
                self.message["text"] = f"Вы ввели неверный логин или пароль,\nпожалуйста проверьте введёные данные"

                if login not in self.count_error:
                    self.count_error[login] = 0
                else:
                    self.count_error[login] =+ 1

                if self.count_error[login] >= 3:
                    UserController.update(user.id,ban = True)

            elif user.date_auth is not None:
                if (datetime.now() - user.date_auth).days >= 31:
                    UserController.update(user.id, ban = True)
                    self.message["text"] = f"Ваша учётная запись автоматически заблокированна.\nОбратитесь к администратору."

            elif user.ban:
                self.message["text"] = f"Вы заблокированны. Обратитесь к администратору"
            
            elif user.first_auth:
                self.count_error[login] = 0
                window = NewPasswordView(user)
            
            elif user.role_id.id == 1:
                self.count_error[login] = 0
                admin = UserController.show("admin")
                window = AdminView(admin)
                self.destroy()
            
            else:
                self.message["text"] = f"Добро пожаловать"
                self.count_error[login] = 0
                UserController.update(user.id,date_auth = datetime.now().date())
            

        # test_user = UserController.show(login)

        # # Проверка введённого логина
        # if test_user is not None:

        #     if login not in self.count_error:
        #         self.count_error[login] = 0 # добавить в словарь ключ-значение {user:0}

        #     self.count_error[login] += 1

        #     if self.count_error[login] >= 3:
        #         UserController.update(test_user.id,ban = 1)
        #     if user:
        #         self.count_error[login] = 0



if __name__ == "__main__":
    window = LoginView()
    window.mainloop()