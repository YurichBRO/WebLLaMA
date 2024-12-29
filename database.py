import json

class UserDatabase:
    def __init__(self, filepath):
        self.filepath = filepath
        self.load()
    
    def load(self):
        try:
            with open(self.filepath, 'r') as file:
                self.data = json.load(file)
        except:
            self.data = {}
            
    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=2)
    
    def add_chat(self, user):
        if str(user) not in self.data:
            self.data[str(user)] = {
                'chats': [[]],
                'current-chat': 0
            }
        else:
            self.data[str(user)]['chats'].append([])
            self.data[str(user)]['current-chat'] = len(self.data[str(user)]['chats']) - 1
        self.save()
    
    def get_current_chat_number(self, user):
        return self.data[str(user)]['current-chat']
    
    def add_message(self, user, message):
        if str(user) not in self.data:
            self.add_chat(user)
        self.data[str(user)]['chats'][self.get_current_chat_number(user)].append(message)
        self.save()
    
    def get_messages(self, user):
        return self.data[str(user)]['chats'][self.get_current_chat_number(user)]
    
    def get_history(self, user):
        return self.data[str(user)]['chats']
    
    def select_chat(self, user, index):
        if 0 <= index < len(self.data[user]['chats']):
            self.data[str(user)]['current-chat'] = index
            self.save()
        else:
            raise IndexError('Chat index out of range')
    
    def delete_chat(self, user, index):
        if 0 <= index < len(self.data[user]['chats']):
            del self.data[str(user)]['chats'][index]
            if len(self.data[str(user)]['chats']) == 0:
                self.new_chat(user, index)
            if self.get_current_chat_number(user) == len(self.data[str(user)]['chats']):
                self.select_chat(user, len(self.data[str(user)]['chats']) - 1)
            self.save()
        else:
            raise IndexError('Chat index out of range')