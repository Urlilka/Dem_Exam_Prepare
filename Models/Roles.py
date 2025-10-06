from Models.Base import *

class Roles(Base):

    '''
    Модель описывающая роли пользователя
    id = Первичный ключ
    role = Название роли, уникальное имя, до 100 символв
    '''

    id = PrimaryKeyField()
    role = CharField(unique=True, max_length=100)

if __name__ == "__main__":
    mysql.create_tables([Roles])
