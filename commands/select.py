def callback(bot, db, message):
    from_ = message.from_user.id
    i = 0
    while i < len(message.text) and message.text[i] in "/qwertyuiopasdfghjklzxcvbnm":
        i += 1
    while i < len(message.text) and message.text[i] == " ":
        i += 1
    param = message.text[i:]
    try:
        index = int(param)
    except:
        bot.send_message(from_, "Неверный параметр - нужно передать целое число")
        return
    
    if index < 0 or index >= len(db.get_history(from_)):
        bot.send_message(from_, "Индекс чата выходит за границы")
        return
    
    db.select_chat(from_, index)
    bot.send_message(from_, f"Выбран чат {index}")