from tkinter import ttk, Tk
from tkinter import *

from Controllers.UserControllers import UserController


class NewPasswordView(Tk):
    """Класс для создания окна "создания новго пароля при первом входе пользователя"
    """
    def __init__(self, login):
        super().__init__()
        self.user = UserController.show(login)
        self.title(f"Смена пароля: {self.user.login}")
        self.geometry("400x200")


        # Старый Пароль
        self.title_old_password = ttk.Label(self, text="Введите старый пароль")
        self.title_old_password.pack(anchor="center")
        # Ввод старого пароля
        self.input_old_password = ttk.Entry(self)
        self.input_old_password.pack(anchor="center")

        # Новый Пароль
        self.title_new_password = ttk.Label(self, text="Введите новый пароль")
        self.title_new_password.pack(anchor="center")
        # Ввод нового пароля
        self.input_new_password = ttk.Entry(self)
        self.input_new_password.pack(anchor="center")

        # Подтвердить Новый Пароль
        self.title_confirm_new_password = ttk.Label(self, text="Введите новый пароль снова")
        self.title_confirm_new_password.pack(anchor="center")
        # Повторный ввод нового пароля
        self.input_confirm_new_password = ttk.Entry(self)
        self.input_confirm_new_password.pack(anchor="center")

        # Сообщение
        self.message = ttk.Label(self, text="___")
        self.message.pack(anchor="center", expand=1)

        # Кнопка
        self.button = ttk.Button(self, text="Изменить пароль")
        self.button.pack(anchor="center",expand=1)
        self.button["command"] = self.Button_Clicked
    

    def Button_Clicked(self):
        """Метод события при нажатии на кнопку.\n\nСравнивает старый пароль с введёным старым, и новые пароли друг с другом. Далее меняет пароль на новый.
        """
        curr_login = self.user
        old_pass = self.input_old_password.get()
        new_pass = self.input_new_password.get()
        conf_new_pass = self.input_confirm_new_password.get()

        if old_pass == "" or new_pass == "" or conf_new_pass == "":
            self.message["text"] = "Одно или несколько полей пустые"
        elif old_pass !=  curr_login.password:
            self.message["text"] = "Старый пароль введён неверно"
        elif old_pass == new_pass or old_pass == conf_new_pass:
            self.message["text"] = "Новый пароль должен быть отличным от старого"
        elif new_pass == conf_new_pass:
            self.message["text"] = "Пароль обновлён"
            UserController.update(curr_login.id, password = new_pass, first_auth = 0)
            self.destroy()
        else:
            self.message["text"] = "Новый пароль не совпадает с введёным повторно"


if __name__ == "__main__":
    window = NewPasswordView("test")
    window.mainloop()