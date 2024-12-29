from database import UserDatabase
from truncate import truncate

def callback(bot, db: UserDatabase, message):
    from_ = message.from_user.id
    chat = db.get_messages(from_)
    result = [f"Чат №{db.get_current_chat_number(from_)}"]
    for i in chat:
        role = i['role'].ljust(4)
        text = truncate(i.text, 80)
        result.append(f'{role}: {text}')
    bot.send_message(from_, '\n'.join(result))