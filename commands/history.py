from truncate import truncate

def callback(bot, db, message):
    from_ = message.from_user.id
    chats = db.get_history(from_)
    result = [f"История чатов (сейчас выбран {db.get_current_chat_number(from_)})"]
    for i, chat in enumerate(chats):
        if len(chat) == 0:
            result.append(f'{i}, сообщ.: 0')
            continue
        first_message = chat[0]['content']
        result.append(f'{i}, сообщ.: {len(chat)}')
        result.append(truncate(first_message, 80))
    bot.send_message(from_, '\n'.join(result))