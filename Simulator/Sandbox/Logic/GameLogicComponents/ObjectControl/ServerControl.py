# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ServerControl.py
# @note サーバー側で処理するときにクライアントのプレイヤーオブジェクトに対して設定

from ...Input import PlayerController
from .PlayerControl import PlayerControl

class ServerControl(PlayerControl):

    def __init__(self, actor):
        super().__init__()
        super()._set_control_actor(actor)

        # test
        self._cnt = 0
    # def __init__

    def update(self):        
        inputs = self._receive_network_inputs()
        super()._update_core(inputs)
    # def update

    def _receive_network_inputs(self):
        self._cnt = self._cnt +1
        if self._cnt % 60 != 0:
            return []
        return [PlayerController.PlayerController.KEY_DOWN]
    
# class ServerControl
