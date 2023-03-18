from aiogram import types, Dispatcher 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext






async def cancel_handler(message: types.Message, state: FSMContext):
    '''Выход из состояний'''
    current_state = await state.get_state()
    if current_state == 'FSMQuiz:quiz' or current_state == 'FSMQuiz:quiz_one_to_one':
        async with state.proxy() as data:
            for i in data['msg_id_all']:
                try:
                    await bot.delete_message(chat_id=message.chat.id, message_id=i)
                except:
                    pass

    await message.reply('Ok', reply_markup=types.ReplyKeyboardRemove()) 
    await state.finish()






def regisret_handlers_cancel(dp : Dispatcher):

    dp.register_message_handler(cancel_handler, state='*', commands='cancel')


