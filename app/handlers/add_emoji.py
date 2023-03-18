from aiogram import types, Dispatcher 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup 
from database.add_user import send_emoji, update_emoji
from keyboards.keyboard_emoji import kb_emoji, kb_language




class FSMEmoji_add(StatesGroup):    
    language = State()
    emoji = State()


class FSMEmoji_del(StatesGroup):    
    emoji = State()





async def set_language(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Введи язык для которого хочешь добавить или поменять эмоджи', reply_markup=kb_language)
    await FSMEmoji_add.language.set()




async def get_language(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['language'] = message.text
    await bot.send_message(message.from_user.id, 'Отправь эмоджи', reply_markup=types.ReplyKeyboardRemove())
    await FSMEmoji_add.emoji.set()




async def get_emoji(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['language']
    msg = update_emoji(message.from_user.id, data['language'], message.text)
    await bot.send_message(message.from_user.id, msg)
    await state.finish()




async def set_language_del(message: types.Message, state: FSMContext):
    lng = send_emoji(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Какие эможди хочешь удалить?', reply_markup=kb_emoji(lng))
    await FSMEmoji_del.emoji.set()




async def get_emoji_del(message: types.Message, state: FSMContext):
    msg = update_emoji(message.from_user.id, message.text[:-3], 'None')
    await bot.send_message(message.from_user.id, msg, reply_markup=types.ReplyKeyboardRemove())
    await state.finish()







def regisret_handlers_emoji(dp : Dispatcher):

    dp.register_message_handler(set_language, commands='set_emoji')
    dp.register_message_handler(get_language, state=FSMEmoji_add.language)
    dp.register_message_handler(get_emoji, state=FSMEmoji_add.emoji) 

    dp.register_message_handler(set_language_del, commands='del_emoji')
    dp.register_message_handler(get_emoji_del, state=FSMEmoji_del.emoji) 

