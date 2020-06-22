# -*- coding: utf-8 -*-
from typing import AnyStr


class UserModel:
    def __init__(self, name: AnyStr):
        self.name = name

    def __str__(self):
        return u'{}'.format(self.name).encode('utf8')
