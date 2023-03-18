from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import randint 
import emoji




def get_kb_quiz(words: list[list[str | None]], some_type: str, answer_id: int) -> (ReplyKeyboardMarkup | str | list[str]):
    '''Возвращает клавиатуру с варианстами ответа'''

    id_main_list: int = randint(0, len(words) - 1) #id списка с правильным вариантом ответа 

    while True:
        id_main: int = randint(0, len(words[id_main_list]) - 1) #id правльного ответа lng_answer

        if words[id_main_list][id_main] and id_main != answer_id:
            break

    
    def any_str(row: list[str]) -> str:
        '''Возвращает любую строку из списка'''
        wd = row[randint(0, len(row) - 1)]
        while not wd:
            wd = row[randint(0, len(row) - 1)]
        return wd


    msg = some_type if some_type != 'NULL' else 'any'
    kb_quiz = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder= 'type: ' + msg)

    main: str = words[id_main_list][id_main] #правильный вариант ответа
    main_list: list[str] = words[id_main_list].copy() #список с правильным вариантом ответа

    for i, row in enumerate(words):
        if i == id_main_list:

            if answer_id:
                wd = row[answer_id]
                
                if not wd:
                    main = row.pop(id_main) 
                    wd = any_str(row)

            else:
                main = row.pop(id_main) 
                wd = any_str(row)

            kb_quiz.add(KeyboardButton(emoji.emojize(wd)))

        else:
            row.pop(id_main)
            wd = any_str(row)
            kb_quiz.add(KeyboardButton(emoji.emojize(wd)))

    return kb_quiz, main, main_list






