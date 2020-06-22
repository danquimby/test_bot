# coding=utf-8
import logging
from typing import AnyStr
from transitions import Machine
from bot.models.message import Message
from bot.models.states import states, answer
from bot.models.user import UserModel


class SelectAnswer:
    def __init__(self,answer_id: int, answer_name: AnyStr):
        self.answer_id = answer_id
        self.answer_name = answer_name

class User(UserModel):

    def __init__(self, name: AnyStr, message: Message):
        UserModel.__init__(self, name)
        self.log = logging.getLogger('chatBot')
        self.is_complete_order = False
        self.message = message
        self.answers = []
        self.chat_id = None
        self.passible_next_state = True
        machine = Machine(model=self, states=states, ordered_transitions=True, initial='gretings', after_state_change='on_enter')
        machine.add_transition('finished', 'Confirm', 'Cancel', unless=['is_complete_order'])
        machine.add_transition('finished', 'Confirm', 'Complete', conditions=['is_complete_order'])

    def on_enter(self):
        model = self._getStateModel()
        if 'enter' in model:
            if self.is_Confirm():
                self.is_complete_order = True if self.answers[-1].answer_id == 0 else False
                self.finished()
            elif self.is_CompleteOrder():
                if len(self.answers) > 1:
                    self.message.text = model.get('enter').format(self.answers[0].answer_name, self.answers[1].answer_name)
            else:
                self.message.text = model.get('enter')

    def chaeck_answer(self, message: Message):
        self.message.reply_text = ''
        model = self._getStateModel()
        self.message.reply_text = model.get('exit', '')
        if 'conditions' in model:
            pair = model.get('conditions', None)
            if pair:
                self.passible_next_state = False
                for i in range(len(pair)):
                    condition = pair[i]
                    result = [x for x in condition if x == self.message.text]
                    if result:
                        result = result[0] if not result[0].isnumeric() else condition[0]
                        msg_reply = model.get('exit', None)
                        if msg_reply:
                            self.message.reply_text = msg_reply.format(result)
                        self.answers.append(SelectAnswer(i, result))
                        self.passible_next_state = True
                        break
        else:
            # if not necessary
            self.passible_next_state = True
        if not self.passible_next_state:
            self.message.reply_text = model.get('error_answer', '')
        if self.passible_next_state:
            self.next_state()

    def _getStateModel(self):
        return answer.get(self.state)
