import telebot
import command_manager as cm
import commands.help as help
import commands.manual as manual
import json

with open("config.json") as config:
    config_data = json.load(config)
    TOKEN = config_data["token"]
    
OLLAMA_MODEL = "llama3.2"

bot = telebot.TeleBot(TOKEN)

command_manager = cm.CommandManager(bot)
command_manager.add_command("help", help.callback)
command_manager.add_alias("help", "start")
command_manager.add_command("manual", manual.callback)
command_manager.listen()

bot.infinity_polling()