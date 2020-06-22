import logging
from abc import abstractmethod, ABCMeta
from typing import AnyStr


class ChatBotBase:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.log = logging.getLogger('chatBot')

    @abstractmethod
    def sendMessage(self, messge: AnyStr): raise NotImplementedError

    @abstractmethod
    def replyMessage(self, messge: AnyStr): raise NotImplementedError

    @abstractmethod
    def start(self): raise NotImplementedError
