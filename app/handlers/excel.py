from aiogram import types, Dispatcher 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup 
from database.add_word import get_excel, replace_excel
from deleting import deleting_file
import datetime



class FSMExcel(StatesGroup):    
    upload = State()




async def download(message: types.Message, state: FSMContext):
    '''Фотрирует и отправляет .xlsx файл пользователю'''
    command = message.text
    name = get_excel(message.from_user.id if command == '/download' else 1, message.chat.username)
    doc = open(name, 'rb')
    time = datetime.datetime.now()
    time = time.strftime("%d_%m_%Y__%H_%M")
    await bot.send_document(message.from_user.id, (f'{message.chat.username}_{time}.xlsx', doc))
    deleting_file(name)
    await state.finish() 




async def replace(message: types.Message, state: FSMContext): 
    '''Запуск МС для принятия .xlsx файла''' 
    await bot.send_message(message.from_user.id, 'пришли excel документ')
    await FSMExcel.upload.set()




async def upload(message: types.Message, state: FSMContext):
    '''Примает .xlsx файл. Записывает в БД.'''
    if message.document.file_name[-5:] == '.xlsx':
        time = datetime.datetime.now()
        time = time.strftime("%d_%m_%Y__%H_%M_%S")
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        name = f"document_xlsx/{message.chat.username}_{message.from_user.id}_{time}.xlsx"  
        await bot.download_file(file_path, name)
        msg = replace_excel(message.from_user.id, name)
        deleting_file(name)
        await bot.send_message(message.from_user.id, msg)

    else:
        await bot.send_message(message.from_user.id, 'отправьте файл с расширением .xlsx')

    await state.finish()





def regisret_handlers_excel(dp : Dispatcher):

    dp.register_message_handler(download,  commands=['download', 'download_sample'], state='*')
    dp.register_message_handler(replace,  commands='replace')
    dp.register_message_handler(upload, content_types=['document'], state=FSMExcel.upload) 





