import logging

try:
    with open("commands/manual-message.txt", encoding="utf-8") as manual_message_file:
        manual_message = manual_message_file.read()
except:
    logging.critical("Failed to open manual-message.txt")
    exit(1)
else:
    def callback(bot, db, message):
        bot.send_message(message.from_user.id, manual_message)