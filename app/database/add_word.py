from database.word import Word
from database.create_db import Session 
import openpyxl
import datetime
from random import randint 



def replace_excel(user_id: str, path_to_file: str) -> str:
    '''Обновляет таблицу пользователя'''

    try:
        def checklist(lst: list[str], i: int) -> str | None:
            if len(lst) > i:
                return lst[i].value
            else:
                return None 

        book = openpyxl.open(path_to_file, read_only=True) 
        sheet = book.active

        session = Session()
        session.query(Word).filter(Word.user_id == user_id).delete()

        for row in range(2, sheet.max_row + 1):

            word = Word(user_id,
                        sheet[row][0].value, 
                        sheet[row][1].value, 
                        checklist(sheet[row], 2),
                        checklist(sheet[row], 3), 
                        checklist(sheet[row], 4),
                        checklist(sheet[row], 5),  
                        checklist(sheet[row], 6))  
            if len({word.__dict__['first_language'], word.__dict__['second_language'], word.__dict__['third_language'], word.__dict__['fourth_language']} - {None}) > 1:
                session.add(word)

        session.commit()
        session.close()
        book.close()
        return 'Таблица обновлена'

    except:
        return 'Ошибка обновления таблицы'







def get_excel(user_id: str, username: str) -> str:
    '''Получение excel таблицы'''

    book = openpyxl.Workbook()
    sheet = book.active

    session = Session()

    sheet['A1'] = 'FIRST LANGUAGE'
    sheet['B1'] = 'SECOND LANGUAGE'
    sheet['C1'] = 'THIRD LANGUAGE'
    sheet['D1'] = 'FOURTH LANGUAGE'
    sheet['E1'] = 'TYPE WORD 1'
    sheet['F1'] = 'TYPE WORD 2'
    sheet['G1'] = 'TYPE WORD 3'

    result = session.query(Word.first_language, Word.second_language, Word.third_language, Word.fourth_language, Word.type_word_1, Word.type_word_2, Word.type_word_3).filter(Word.user_id == user_id).all()

    for i, row in enumerate(result):
        sheet[i+2][0].value = row[0]
        sheet[i+2][1].value = row[1]
        sheet[i+2][2].value = row[2]
        sheet[i+2][3].value = row[3]
        sheet[i+2][4].value = row[4]
        sheet[i+2][5].value = row[5]
        sheet[i+2][6].value = row[6]
    
    time = datetime.datetime.now()
    time = time.strftime("%d_%m_%Y__%H_%M_%S")
    name: str = f"document_xlsx/{username}_{user_id}_{time}.xlsx"
    book.save(name)
    book.close()

    return name







def add_word(user_id: str, first_language: str=None,  second_language: str=None, third_language: str=None, fourth_language: str=None, active_time: str=None) -> str | None:
    '''Записывает в БД слово'''

    session = Session()
    try:
        result = session.query(Word).filter(Word.user_id == user_id)
    except:
        return None

    if result:
        word = Word(user_id, first_language, second_language, third_language, fourth_language, active_time)
        session.add(word)
        session.commit()
        session.close()
        return 'Добавлено в БД'

    else:
        return 'Активируйте бота командой /start'







def get_word_quiz(user_id: str, command: str=None) -> list[tuple[str]]:
    '''Возвращае N количество слов'''

    session = Session()
    result = session.query(Word.first_language, Word.second_language, Word.third_language, Word.fourth_language, Word.type_word_1, Word.type_word_2, Word.type_word_3).filter(Word.user_id == user_id).all()

    if not result:
        return None
    
    return result














