import logging

def callback(bot, db, message):
    from_ = message.from_user.id
    db.add_chat(from_)
    bot.send_message(from_, "Чат успешно создан")
    logging.info(f"Chat created for user {from_}")