class CommandManager:
    def __init__(self, bot, no_command_action=lambda bot, message: None):
        self.commands = {}
        self.bot = bot
        self.no_command_action = no_command_action
    
    def add_command(self, command, callback):
        self.commands[command] = callback
    
    def add_alias(self, command, alias):
        if command in self.commands:
            self.commands[alias] = self.commands[command]
    
    @staticmethod
    def get_command_name(text):
        i = 1
        while i < len(text) and text[i].isalnum():
            i += 1
        command_name = text[1:i].lower()
        return command_name
    
    def listen(self):
        @self.bot.message_handler(content_types=['text'])
        def handle_message(message):
            text = message.text
            if text and text[0] == '/':
                command_name = self.get_command_name(text)
                if command_name in self.commands:
                    self.commands[command_name](self.bot, message)
                else:
                    self.no_command_action(self.bot, message)
            else:
                self.no_command_action(self.bot, message)
            