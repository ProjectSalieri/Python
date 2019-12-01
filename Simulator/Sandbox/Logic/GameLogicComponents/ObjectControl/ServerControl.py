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
        self._test_client = None
    # def __init__

    def set_test_client(self, test_client):
        self._test_client = test_client
    # def set_test_client

    def update(self):        
        inputs = self._receive_network_inputs()
        super()._update_core(inputs)
    # def update

    def _receive_network_inputs(self):
        # TODO : ネットワーク越しにキー入力を受信
        if self._test_client != None:
            return self._test_client.send_network_inputs()
        return []
# class ServerControl
