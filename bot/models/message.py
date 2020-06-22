# -*- coding: utf-8 -*-
from typing import Dict


class Message:
    def __init__(self, src: Dict):
        if src:
            self.update_id = src['update_id']
            self.text = src['message']['text']
            self.chat_id = src['message']['chat']['id']
            self.chat_name = src['message']['chat']['first_name']
        self.reply_text = u''

    def __str__(self):
        return u'roomId={} text={} reply={}'.format(self.chat_id, self.text, self.reply_text).encode('utf8')
