# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActionEat
# @note

class ActionEat:

    STATE_EATING = 1
    STATE_EAT_END = 2
    STATE_END = 3

    def __init__(self, host_actor):
        self.actor = host_actor

        self.state = ActionEat.STATE_END
    # def __init__

    def start(self):
        # 初期状態に
        self._reset()
    # def start

    def update(self):
        if self.state == STATE_EATING:
            self._eating()
        elif self.state == STATE_EAT_END:
            self._eat_end()
        elif self.state == STATE_END:
            pass
    # def update

    def is_finish(self):
        return self.state = ActionEat.STATE_END
    # def is_finish

    def _reset(self):
        self.state = ActionEat.STATE_EATING
    # def _reset(self):

    def _eating(self):
        sensor = self.actor.get("Sensor")
        self.state = ActionEat.STATE_EAT_END
    # def _eating

    def _eat_end(self):
        self.state = ActionEat.STATE_END
    # def _eat_end
    
# class ActionEat
