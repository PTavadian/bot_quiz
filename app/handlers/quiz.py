from aiogram import types, Dispatcher 
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup 
from database.add_word import get_word_quiz 
from database.add_user import send_emoji
from database.filter import filter, filter_sort
from keyboards.keyboard_quiz import get_kb_quiz
import emoji
import asyncio




class FSMQuiz(StatesGroup):    
    quiz = State()







async def start_quiz(message: types.Message, state: FSMContext):
    command: str = message.text
    data_words: tuple[list[str]] = get_word_quiz('1' if command == '/quiz_test' else message.from_user.id, command)
    if not data_words:
        await bot.send_message(message.from_user.id, 'Сперва нужно загрузить .xlsx файл со своими словами')
        return

    data_emoji: tuple[str] = send_emoji('1' if command == '/quiz_test' else message.from_user.id)
    if command == '/quiz_any':
        words: list[list[str]] = filter(data_words, data_emoji)
    else:
        words: list[list[str]] = filter_sort(data_words, data_emoji)

    cmd = {'/quiz': None, '/quiz_any': None, '/quiz_test': None, '/answer_first': 0, '/answer_second': 1, '/answer_third': 2, '/answer_fourth' : 3,} 
    language_answer_id: int = cmd[message.text]
    kb, lng_answer, main_list = get_kb_quiz(words, language_answer_id)

    words_all: list[str] = []
    msg_id_all: list[int] = []
    checklist: list[str] = []
 
    words_all.append(main_list)

    bot_msg_kb = await bot.send_message(message.from_user.id, emoji.emojize(lng_answer), reply_markup=kb)
    msg_id_all.append(bot_msg_kb.message_id) 

    async with state.proxy() as data:
        data['count'] = 1
        data['words'] = words_all
        data['msg_id_all'] = msg_id_all
        data['checklist'] = checklist
        data['command'] = command
        data['data_words'] = data_words
        data['data_emoji'] = data_emoji
        data['type_quiz'] = message.text
        data['language_answer_id'] = language_answer_id

    await FSMQuiz.quiz.set()

    await asyncio.sleep(120)
    current_state = await state.get_state()
    
    if current_state == 'FSMQuiz:quiz' or current_state == 'FSMQuiz:quiz_one_to_one':
        async with state.proxy() as data_1:

            if message.message_id + 22 < data_1['msg_id_all'][0]:
                return

            for i in data_1['msg_id_all']:
                try:
                    await bot.delete_message(chat_id=message.chat.id, message_id=i)
                except:
                    pass
        msg_id = await bot.send_message(message.from_user.id, 'время вышло!')
        await state.finish()
        await asyncio.sleep(3)
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=msg_id.message_id)
        except:
            pass







async def quiz(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['count'] += 1

    if data['count'] - 1 <= 9:

        if data['type_quiz'] == '/quiz_any':
            words: list[list[str]] = filter(data['data_words'], data['data_emoji'])
        else:
            words: list[list[str]] = filter_sort(data['data_words'], data['data_emoji'])

        kb, lng_answer, main_list = get_kb_quiz(words, data['language_answer_id'])

        bot_msg_kb = await bot.send_message(message.from_user.id, emoji.emojize(lng_answer), reply_markup=kb)

        async with state.proxy() as data:
            data['words'].append(main_list)
            data['msg_id_all'].append(message.message_id) 
            data['msg_id_all'].append(bot_msg_kb.message_id)
            data['checklist'].append(message.text[2:] if message.text[:2] == message.text[:2].upper() and message.text[1] != ' ' else message.text)
        await FSMQuiz.quiz.set()

    else:
        async with state.proxy() as data:
            data['msg_id_all'].append(message.message_id)
            data['checklist'].append(message.text[2:] if message.text[:2] == message.text[:2].upper() and message.text[1] != ' ' else message.text)

        msg: str = ''
        for i, row in enumerate(data['words']):
            r: str = f"  (<b>error:</b> <s>{data['checklist'][i]}</s>)\n"
            error = r
            for n, column in enumerate(row):

                if n == 0:
                    msg += f'<b>{column.strip()}</b>'
                elif column:
                    msg += f' >> {column.strip()}'

                if error == r and column.count(data['checklist'][i].strip()):
                        error = '\n'

            msg += error

        await bot.send_message(message.from_user.id, emoji.emojize(f'<i>Тест завершен:\n{msg}</i>'), parse_mode='HTML', reply_markup=types.ReplyKeyboardRemove())
        
        for i in data['msg_id_all']:
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=i)
            except:
                pass
        
        await state.finish()
        return







def regisret_handlers_quiz(dp : Dispatcher):

    dp.register_message_handler(start_quiz, commands=['quiz', 'quiz_any', 'quiz_test', 'answer_first', 'answer_second', 'answer_third', 'answer_fourth'], state='*')
    dp.register_message_handler(quiz, state=FSMQuiz.quiz)






