from sqlalchemy import Column, Integer, String
from database.create_db import Base


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)

    first_language = Column(String)
    second_language = Column(String)
    third_language = Column(String)
    fourth_language = Column(String)

    type_word_1 = Column(String)
    type_word_2 = Column(String)
    type_word_3 = Column(String)





    def __check(self, some: str) -> str | None:
        '''Удаляет лишние пробелы'''
        if some:
            return str(some).strip()
        else:
            return some
                

    def __init__(self, 
                 user_id: str, 
                 first_language: str=None, 
                 second_language: str=None,
                 third_language: str=None, 
                 fourth_language: str=None, 
                 type_word_1: str=None,
                 type_word_2: str=None,
                 type_word_3: str=None):


        self.user_id = user_id
        self.first_language = self.__check(first_language)
        self.second_language = self.__check(second_language)
        self.third_language = self.__check(third_language)
        self.fourth_language = self.__check(fourth_language)
        self.type_word_1 = self.__check(type_word_1)
        self.type_word_2 = self.__check(type_word_2)
        self.type_word_3 = self.__check(type_word_3)
