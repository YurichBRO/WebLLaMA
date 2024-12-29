import logging
from database import UserDatabase

def callback(bot, db: UserDatabase, message):
    from_ = message.from_user.id
    db.add_chat(from_)
    bot.send_message(from_, "Чат успешно создан")
    logging.info(f"Chat created for user {from_}")