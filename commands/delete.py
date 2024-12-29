def callback(bot, db, message):
    from_ = message.from_user.id
    db.delete_chat(from_, db.get_current_chat_number(from_))
    bot.send_message(from_, "Текущий чат был удален")