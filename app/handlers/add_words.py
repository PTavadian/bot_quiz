from aiogram import types, Dispatcher 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup 
from database.add_word import add_word



class FSMAdd(StatesGroup):    
    get_word = State()




async def add_word(message: types.Message, state: FSMContext):
    '''Запуск МС для ручного добавления слов'''
    
    msg_1 = 'first_lang >> second_lang >> third_lang >> fourth_lang\n'
    msg_2 = 'first_lang >> second_lang\n'
    msg_3 = 'first_lang >> >> third_lang >> fourth_lang'
    await bot.send_message(message.from_user.id, 'введи слово в формате:\n' + msg_1 + msg_2 + msg_3)
    await FSMAdd.next()




async def get_word(message : types.Message, state: FSMContext):
    '''Принимает и записывает слово в БД'''

    if message.text.find('»') != -1:
        word: list = message.text.split('»')
    elif message.text.find('>>') != -1:
        word: list = message.text.split('>>')
    else:
        word = None

    if word:
        for i in range(len(word)):
            word[i] = word[i].strip()
        while len(word) < 4:
            word.append(None)
        msg = add_word(message.from_user.id, word[0], word[1], word[2], word[3])
        await bot.send_message(message.from_user.id, msg)
    else:
        await bot.send_message(message.from_user.id, 'Неправильный формат ввода')
    await state.finish() 








def regisret_handlers_word(dp : Dispatcher):

    dp.register_message_handler(add_word,  commands='add_word')
    dp.register_message_handler(get_word, state=FSMAdd.get_word) 






