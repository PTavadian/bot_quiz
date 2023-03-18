from database.user import User
from database.create_db import Session 
from database.emoji_flags import emoji_flags





def add_user(user_id: str, first_name: str, last_name: str, full_name: str) -> str:
    '''Записывает в БД данные пользователя'''

    session = Session()
    try:
        result = session.query(User).filter(User.user_id == user_id).one()
    except:
        result = None

    if not result:
        user = User(user_id, first_name, last_name, full_name)
        session.add(user)
        session.commit()
        session.close()
        return 'Бот готов к работе, загрузи свой .xlsx файл'

    else:
        return 'Бот готов к работе'







def update_emoji(user_id: str, language: str, emoji: str) -> str:
    '''Обновляет эмоджи в БД'''

    def check(emoji: str) -> str | None:
        if set([emoji]) & set(emoji_flags.keys()):
            return emoji_flags[emoji]
        else:
            return None
 
    if emoji != 'None' and not check(emoji):
        return 'Вы ввели недопустивый символ, можно загружать только эмоджи с флагом'


    session = Session()
    try:
        result = session.query(User).filter(User.user_id == user_id).one()
    except:
        result = None

    if result:
        if language == 'first_language':
            session.query(User).filter(User.user_id == user_id).update({User.first_language: check(emoji)})

        elif language == 'second_language':
            session.query(User).filter(User.user_id == user_id).update({User.second_language: check(emoji)})

        elif language == 'third_language':
            session.query(User).filter(User.user_id == user_id).update({User.third_language: check(emoji)})

        elif language == 'fourth_language':
            session.query(User).filter(User.user_id == user_id).update({User.fourth_language: check(emoji)})

        session.commit()
        session.close()
        return 'Эмоджи сохранены'
    
    else:
        return 'Сперва нажмите команду /start'







def send_emoji(user_id: str) -> tuple[str | None]:
    '''Возвращает список используемых пользователем эмоджи'''

    session = Session()
    try:
        result = session.query(User.first_language, User.second_language, User.third_language, User.fourth_language).filter(User.user_id == user_id).one()
    except:
        result = (None, None, None, None)
    
    return result




