from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji


b1 = KeyboardButton('first_language') 
b2 = KeyboardButton('second_language') 
b3 = KeyboardButton('third_language') 
b4 = KeyboardButton('fourth_language') 
b5 = KeyboardButton('/cancel') 

kb_language = ReplyKeyboardMarkup(resize_keyboard=True) 
kb_language.add(b1).add(b2).add(b3).add(b4).add(b5)





def kb_emoji(emojis: tuple[str]) -> str:

    languages = ('first_language', 'second_language', 'third_language', 'fourth_language')
    kb_emoji = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='выбери вариант ответа')

    for i, emj in enumerate(emojis):
        if emj:
            kb_emoji.add(KeyboardButton(emoji.emojize(languages[i] + ' ' + emj)))

    kb_emoji.add(b5)

    return kb_emoji
















