import telebot
import command_manager as cm
import commands_list
import aliases_list
import json
import database

with open("config.json") as config:
    config_data = json.load(config)
    TOKEN = config_data["token"]
    
OLLAMA_MODEL = "llama3.2"

bot = telebot.TeleBot(TOKEN)
db = database.UserDatabase("users.json")

command_manager = cm.CommandManager(bot, db)
for i in dir(commands_list):
    print(i)
    if i.startswith("__"):
        continue
    module = getattr(commands_list, i)
    command_manager.add_command(i, module.callback)
for i in dir(aliases_list):
    print(i)
    if i.startswith("__"):
        continue
    val = getattr(aliases_list, i)
    command_manager.add_alias(val, i)
print(command_manager.commands)
command_manager.listen()

bot.infinity_polling()