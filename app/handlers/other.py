from aiogram import types, Dispatcher 
from create_bot import dp, bot
from handlers.commands import commands, bot_commands
from database.add_user import add_user 




async def start(message: types.Message):
    '''Добавление в БД при первом запуске. Добавление меню.'''
    msg = add_user(message.from_user.id, 
                   message.from_user.first_name,
                   message.from_user.last_name,
                   message.from_user.full_name,)
    await bot.send_message(message.from_user.id, msg, reply_markup=types.ReplyKeyboardRemove())
    await commands()


    

async def help(message: types.Message): 
    msg = 'Для работы с ботом доступны следующие команды:\n'
    for i, cmd in enumerate(bot_commands):
        msg += cmd[2] + ';\n' if i != len(bot_commands) - 1 else cmd[2] + '.'
    await bot.send_message(message.from_user.id, '<i>' + msg + '</i>', parse_mode='HTML', reply_markup=types.ReplyKeyboardRemove())





def regisret_handlers_other(dp : Dispatcher):

    dp.register_message_handler(start,  commands='start')
    dp.register_message_handler(help,  commands='help')


