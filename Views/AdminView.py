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

if __name__ == "__main__":
    window = AdminView("admin")
    window.mainloop()