import telebot
import command_manager as cm
import commands.help as help
import commands.manual as manual
import commands.new as new
import commands.view as view
import commands.history as history
import json
import database

with open("config.json") as config:
    config_data = json.load(config)
    TOKEN = config_data["token"]
    
OLLAMA_MODEL = "llama3.2"

bot = telebot.TeleBot(TOKEN)
db = database.UserDatabase("users.json")

command_manager = cm.CommandManager(bot, db)
command_manager.add_command("help", help.callback)
command_manager.add_alias("help", "start")
command_manager.add_command("manual", manual.callback)
command_manager.add_command("new", new.callback)
command_manager.add_command("view", view.callback)
command_manager.add_command("history", history.callback)
command_manager.listen()

bot.infinity_polling()