# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Object.py
# @note

from ActorUtil import ActorUtil

class Object:

    def __init__(self, name, load_option = {}):
        self._object_id = load_option.get("ObjectId")
        if self._object_id == None:
            import random, datetime
            self._object_id = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f') + str(random.randint(0, 100))
        # if _object_id

        self._init_common(name)

        if load_option.get("Life") != None:
            pass
        if load_option.get("Pos") != None:
            self.reset_pos(load_option.get("Pos"))
        # if load_option
    # def __init__

    def get_name(self):
        return self._name
    # def get_name

    def get_object_id(self):
        return self._object_id
    # def get_object_id

    def reset_pos(self, pos):
        self.get_object_component("Physics").reset_pos(pos)

    def get_pos(self):
        return self.get_object_component("Physics").get_pos()

    def kill(self):
        self._is_dead = True

    def is_dead(self):
        if self._is_dead == True:
            return True
        
        life_component = self.get_object_component("Life")
        if life_component == None:
            return False
        return life_component.is_dead()

    def get_object_component(self, component_name):
        return self.object_components.get(component_name)
    # get_object_component

    def get_game_logic_component(self, component_name):
        # game_logic_components初期化中の場合は一時登録を参照する
        if self.game_logic_components == None:
            return self._inserted_game_logic_components.get(component_name)
        
        return self.game_logic_components.get(component_name)
    # get_game_logic_component

    def insert_game_logic_component(self, component_name, component):
        if self.game_logic_components == None:
            self._inserted_game_logic_components[component_name] = component
        else:
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

    def _init_common(self, name):
        self._name = name
        
        # 初期化ファイル
        actor_setting = ActorUtil.load_actor_setting(name)

        self.object_components = ActorUtil.create_object_components(actor_setting)
        self.game_data_components = ActorUtil.create_game_data_components(actor_setting)
        
        self._inserted_game_logic_components = {} # GameLogicComponents同士で依存があるので最後にマージ
        self.game_logic_components = None
        self.game_logic_components = ActorUtil.create_game_logic_components(actor_setting, self)
        # GameLogicComponentsが別のGameLogicComponentsを生成している場合のマージ
        for component_name, component in self._inserted_game_logic_components.items():
            self.game_logic_components[component_name] = component


        self._is_dead = False

        self.drawer = self.game_data_components.get("Draw")
    # def _init_common

# class Object

if __name__ == "__main__":
    pass
