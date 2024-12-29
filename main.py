import telebot
import command_manager as cm
import commands_list
import aliases_list
import json
import database
import ollama
import logging

with open("config.json") as config:
    config_data = json.load(config)
    TOKEN = config_data["token"]

bot = telebot.TeleBot(TOKEN)
db = database.UserDatabase("users.json")

def assistant_responce(bot: telebot.TeleBot, db, message):
    from_ = message.from_user.id
    new_message = bot.send_message(from_, "Ожидайте ответа")
    interval = 10
    db.add_message(from_, {"role": "user", "content": message.text})
    responce = ollama.chat("llama3.2", db.get_messages(from_), stream=True)
    text = ''
    for index, chunk in enumerate(responce):
        text += chunk['message']['content']
        if index % interval == 0:
            try:
                bot.edit_message_text(text, from_, new_message.id)
            except:
                logging.error(f"Failed to edit message in chat {from_}")
    try:
        bot.edit_message_text(text, from_, new_message.id)
    except:
        logging.error(f"Failed to edit message in chat {from_}")
    db.add_message(from_, {'role': 'assistant', 'content': text})

command_manager = cm.CommandManager(bot, db, no_command_action=assistant_responce)
for i in dir(commands_list):
    if i.startswith("__"):
        continue
    module = getattr(commands_list, i)
    command_manager.add_command(i, module.callback)
for i in dir(aliases_list):
    if i.startswith("__"):
        continue
    val = getattr(aliases_list, i)
    command_manager.add_alias(val, i)
command_manager.listen()

bot.infinity_polling()