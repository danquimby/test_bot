# coding: utf8
import os
import requests
from typing import AnyStr
from requests import Response

from bot.models.message import Message

url_api = os.getenv("TELEGRAM_API_URL", 'https://api.telegram.org')


class ApiHelper:

    def __init__(self, token: AnyStr, callback=None):
        self.token = token
        self.new_offset = None
        self.api_url = "{}/bot{}/".format(url_api, token)
        self.callback = callback

    def get_updates_sources(self, offset=None, timeout: int=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        print ('result_json ' + str(resp.json()))
        return resp.json()['result']

    def send_message_source(self, chat_id: AnyStr, text: AnyStr) -> Response:

        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self) -> AnyStr:
        get_result = self.get_updates_sources()
        if len(get_result) > 0:
            last_update = get_result[-1] # get last element from array
        else:
            last_update = get_result[len(get_result)]
        # TODO maybe error if answer is empty need check later
        return last_update

    def loop(self):
        while True:
            self.get_updates_sources(self.new_offset)
            last_update = self.get_last_update()
            message = Message(last_update)
            self.new_offset = message.update_id + 1
            if self.callback != None:
                self.callback(message)

