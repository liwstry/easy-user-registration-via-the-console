from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import metadata, User
from source.input_data import input_data

class Database:
    def __init__(self, file_name='access.db'):
        self.engine = create_engine(f"sqlite:///{file_name}")
        metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_user(self, user_data):
        session = self.Session()
        user = User.users.insert().values(**user_data)
        session.execute(user)
        session.commit()
        session.close()

    def data(self):

        user_data = input_data()
        self.add_user(user_data)
