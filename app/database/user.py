from sqlalchemy import Column, Integer, String
from database.create_db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String)

    first_language = Column(String)
    second_language = Column(String)
    third_language = Column(String)
    fourth_language = Column(String)

    active_time = Column(String)


    def __init__(self, 
                 user_id: str, 
                 first_name: str, 
                 last_name: str, 
                 full_name: str, 
                 first_language: str=None, 
                 second_language: str=None,
                 third_language: str=None, 
                 fourth_language: str=None, 
                 active_time: str=None):
        
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.first_language = first_language
        self.second_language = second_language
        self.third_language = third_language
        self.fourth_language = fourth_language
        self.active_time = active_time



