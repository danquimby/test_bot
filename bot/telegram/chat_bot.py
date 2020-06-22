# coding: utf8
import os
from typing import AnyStr

from bot.chat_bot_base import ChatBotBase
from bot.telegram.api_helper import ApiHelper
from bot.user import User

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN", '1168060739:AAG0dM7LRfC5cGfPuv4jWNXbnBZw4BdiA6Y')

class ChatBot(ChatBotBase):

    def __init__(self):
        self.all_users = [] # User
        super(ChatBot, self).__init__()
        self.apiHelper = ApiHelper(API_TOKEN, self.replyMessage)

    def replyMessage(self, messge: AnyStr):
        _users = [user for user in self.all_users if user.name == messge.chat_name]

        if len(_users) > 0:
            user = _users[-1]
            user.message = messge
        else:
            user = User(messge.chat_name, messge)
            self.all_users.append(user)
        user.chaeck_answer(messge)
        self.sendMessage(user.message)

    def sendMessage(self, messge: AnyStr):
        # first send reply after message
        if messge.reply_text:
            self.apiHelper.send_message_source(messge.chat_id, messge.reply_text)
        self.apiHelper.send_message_source(messge.chat_id, messge.text)

    def start(self):
        self.apiHelper.loop()


