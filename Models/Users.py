from Models.Base import *
from Models.Roles import Roles

class Users(Base):

    """
    Модель описывающая пользователя
    id = первичный ключ
    login
    password
    ban
    role_id
    first_auth
    date_auth


    """

    id = PrimaryKeyField()
    login = CharField(unique=True, max_length=25)
    password = CharField(max_length=255)
    ban = BooleanField(default=False)
    role_id = ForeignKeyField(Roles)
    first_auth = BooleanField(default=True)
    date_auth = DateField(null=True)

if __name__ == "__main__":
    mysql.create_tables([Users])