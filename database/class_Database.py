from sqlalchemy import create_engine
from database.models import metadata, User
from source.input_data import input_data
from sqlalchemy.orm import sessionmaker #  <--- подсказала нейронка

class Database:
    def __init__(self, file_name='access.db'):
        self.engine = create_engine(f"sqlite:///{file_name}")
        metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        
    def add_user(self, user_data):
        session = self.Session()
        user = User.users.insert().values(**user_data)  #   <--- подсказала нейронка
        session.execute(user)
        session.commit()
        session.close()
        
    def data(self):
        
        user_data = input_data()
        self.add_user(user_data)
        print("Пользователь добавлен")
        
        # user = User.users.insert().values(
        #     name=input_data().name,
        #     login=input_data().login,
        #     password=input_data().password,
        #     email=input_data().email,
        # )
        # self.add_user(user)
        # print("Пользователь добавлен")