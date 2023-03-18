from aiogram.utils import executor 
from database import db
from create_bot import dp


async def on_startup(_):
    db.sql_start()


from handlers import other, add_words, excel, quiz, cancel, add_emoji

cancel.regisret_handlers_cancel(dp)
add_emoji.regisret_handlers_emoji(dp)
excel.regisret_handlers_excel(dp)
quiz.regisret_handlers_quiz(dp)
add_words.regisret_handlers_word(dp)
other.regisret_handlers_other(dp)





executor.start_polling(dp, skip_updates=True, on_startup=on_startup) 

