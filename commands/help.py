import logging

try:
    with open("commands/help-message.txt", encoding="utf-8") as help_message_file:
        help_message = help_message_file.read()
except:
    logging.critical("Failed to open help-message.txt")
    exit(1)
else:
    def callback(bot, message):
        bot.send_message(message.from_user.id, help_message)