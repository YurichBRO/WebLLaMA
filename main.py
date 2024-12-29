import telebot
import command_manager as cm
import commands.help as help

TOKEN = "7627113998:AAGd0gcNvdi3FfJfsdNh7sYoNT7YWaSR55c"
OLLAMA_MODEL = "llama3.2"

bot = telebot.TeleBot(TOKEN)
command_manager = cm.CommandManager(bot)
command_manager.add_command("help", help.callback)
command_manager.add_alias("help", "start")

command_manager.listen()
bot.infinity_polling()