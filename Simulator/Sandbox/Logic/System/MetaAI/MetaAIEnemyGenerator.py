# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MetaAIEnemyGenerator.py
# @note

import numpy as np

from .MetaAIProcessOrder import MetaAIProcessOrder

class MetaAIEnemyGenerator:

    def __init__(self):
        pass
    # def __init__

    def execute(self, pack_data):
        return self._execute_sample(pack_data)

    def _execute_sample(self, pack_data):
        enemy_num = 0
        for object_id, status in pack_data["ObjectStatus"].items():
            # TODO : 仮実装
            if status.get("Name") == "SampleEnemy":
                enemy_num += 1
        # for _object_status

        # 敵の数が多い場合は手加減
        if enemy_num > 5:
            return None

        player_pos = None
        player_life = None
        for object_id, status in pack_data["PlayerStatus"].items():
            player_pos = np.array(status["Pos"])
            player_life = status.get("Life")

        # プレイヤーのライフが少ないので手加減
        if player_life == None or player_life < 5000:
            return None
        
        import random
        appear_pos = player_pos + np.array([random.randint(-200, 200), 0, random.randint(-200, 200)])

        option = {
            "Pos" : appear_pos,
            "Name" : "SampleEnemy" # TODO
        }
        order = MetaAIProcessOrder(MetaAIProcessOrder.ORDER_GENERATE_ENEMY, None, option)
        return order
    # def _execute_sample
        

# class MetaAIEnemyGenerator
