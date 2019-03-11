# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SalieriStateActionGoogle.py
# @note Googleで何か検索して、達成 or 諦めるまでをハードコーディングしたステート(Thinkパート)

import SalieriImporter

from Component.BodyComponentPCVirtual import BodyComponentPCVirtual

class SalieriStateThinkGoogle:
    def __init__(self, virtual_body):
        self._virtual_body = virtual_body
    # def __init__

    # TODO : 何かに興味を持ち始める
    #      : 適当な条件でStateActionGoogleを開始
    #      : 検索情報を見て、目標達成条件を確認 -> Action->is_finishedでも達成してなかったら新しい条件でActionGoogleを開始
    #      : BodyComponentの条件とかみて諦める場合はAction->stopを呼び出す
    def execute(self):
        pass
    # def execute

# class SalieriStateThinkGoogle
