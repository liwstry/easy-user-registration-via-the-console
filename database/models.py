from sqlalchemy import MetaData, Table, Column, String, Integer

metadata = MetaData()

class User:
    users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('email', String),
        Column('password', String),
        Column('login', String),
    )
