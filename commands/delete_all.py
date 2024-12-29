def callback(bot, db, message):
    from_ = message.from_user.id
    db.delete_all_chats(from_)
    bot.send_message(from_, "Все чаты удалены")