from Models.Users import *

class UserController:
    @classmethod
    def get(cls):
        """
        вывод всех пользователей
        :return: Список пользователей
        """
        return Users.select()
    
    @classmethod
    def add(cls, login, password, role_id = 2):
        """
        Добавить пользователя в систему
        :param login: логин пользователя
        :param password: Пароль пользователя
        :param role_id: Роль пользователя по умолчанию - Пользователь
        :param return: ничего
        """
        Users.create(login=login,password=password,role_id=role_id)
    
    @classmethod
    def update(cls,id,**fields):
        """
        Обновление данных одного пользователя
        :param id: id пользователя
        :param fields: поле и новое значение
        :param return: ничего
        """
        for key,value in fields.items():
            Users.update({key:value}).where(Users.id == id).execute()
    
    @classmethod
    def auth(cls,login,password):
        """ Метод аутенфикации пользователя
        Args:
            login (str): Логин пользователя
            password (str): Пароль ползователя
        Returns:
            True: Если в Таблице есть такой логин и  пароль
            False: Если в таблице нет такого логина или пароль не сооответствует этому логину
        """
        cls.user = cls.show(login)
        if cls.user is not None:
            if cls.user.password == password:
                return cls.user
            else:
                return False
        else:
            return False
    
    @classmethod
    def show(cls,login):
        """ Метод данных пользователя
        Args:
            login(str): Логин пользователя
        Returns:
            Optional[User]: Если в таблице есть такой пользрователь Возврощается объект описывающий пользователя
            False: Если в таблице нету такого пользователя Возврощается --- -None
        """
        return Users.get_or_none(Users.login == login)

if __name__ == "__main__":
    for row in UserController.get():
        print(row.login)

    # UserController.update(1,login="User")

    # UserController.add("admin", "123456", role_id=1)