# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Object.py
# @note

from ActorUtil import ActorUtil

class Object:

    def __init__(self, name):
        # 初期化ファイル
        actor_setting = ActorUtil.load_actor_setting(name)

        self.object_components = ActorUtil.create_object_components(actor_setting)
        self.game_data_components = ActorUtil.create_game_data_components(actor_setting)
        self.game_logic_components = ActorUtil.create_game_logic_components(actor_setting, self)

        self.drawer = self.game_data_components["Draw"]

    # def __init__

    def reset_pos(self, pos):
        self.get_object_component("Physics").reset_pos(pos)

    def get_pos(self):
        return self.get_object_component("Physics").get_pos()

    def get_object_component(self, component_name):
        return self.object_components.get(component_name)
    # get_object_component

    def get_game_logic_component(self, component_name):
        return self.game_logic_components.get(component_name)
    # get_game_logic_component

    def insert_game_logic_component(self, component_name, component):
        self.game_logic_components[component_name] = component
    # def insert_game_logic_component

    def send_msg(msg):
        send_components = [
            get_game_logic_component("Eat")
        ]
        for component in receive_components:
            if component == None:
                continue
            component.send_msg(msg, self)
    # def send_msg

    def receive_msg(msg, send_actor):
        receive_components = [
            get_game_logic_component("Sense")
        ]
        for component in receive_components:
            if component == None:
                continue
            if component.receive_msg(msg, send_actor) == True:
                return True

        return False
    # def receive_msg

    def update(self):
        # Object共通コンポーネント
        for name, component in self.object_components.items():
            component.update()
        # ゲームロジック用コンポーネント
        for name, component in self.game_logic_components.items():
            component.update()
        # ゲーム用コンポーネント
        for name, component in self.game_data_components.items():
            component.update()
    # def update

    def post_update(self):
        # Object共通コンポーネント
        for name, component in self.object_components.items():
            component.post_update()
        # ゲームロジック用コンポーネント
        for name, component in self.game_logic_components.items():
            component.post_update()
        # ゲーム用コンポーネント
        for name, component in self.game_data_components.items():
            component.post_update()
    # def post_update

# class Object

if __name__ == "__main__":
    pass
