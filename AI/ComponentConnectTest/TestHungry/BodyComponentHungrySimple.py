
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IBodyComponent import IBodyComponent
from Component.ComponentArgCollection import ComponentArgCollection
from Component.DurabilityComponentHungryVirtual import DurabilityComponentHungryVirtual

class BodySubComponentHungrySimple:
    def __init__(self):
        self._hungry_durability = DurabilityComponentHungryVirtual()
    # def __init__

    def get_component_types(self):
        return ["DurabilityComponentHungry"]
    # def get_component_types

    def calc_hungry(self):
        return self._hungry_durability.getDurability()
    # def calc_hungry
# class BodySubComponentHungrySimple

# 標準的なPC情報を使った仮想ボディ
class BodyComponentHungrySimple(IBodyComponent):
    def __init__(self):
        self._body_sub_components = [
            BodySubComponentHungrySimple()
        ]
        self._hungry_durability = DurabilityComponentHungryVirtual()
        
        # 刺激情報スタック
        self._stimuli = ComponentArgCollection()

        # センサー処理した特徴量スタック
        self._features = ComponentArgCollection()

        # 行動情報スタック
        self._actions = ComponentArgCollection()
    # def __init__

    def is_enable(self):
        return True
    # def is_enable

    def enable(self):
        pass
    # def eable

    def disable(self):
        pass
    # def disable

    def try_stimulate(self, component_arg):
        self._stimuli.append(component_arg)
    # def stimulate

    def try_action(self, component_arg):
        self._actions.append(component_arg)
    # def try_action

    # ThinkComponentに渡す情報を
    def pop_features(self, query_arg_types):
        pass
    # def pop_to_brain

    def pop_to_body_component(self):
        pass
    # def pop_to_body_component

    def update(self):
        self.hungry_durability.update()

        self._update_self()
    # def update

    def execute_action(self):
        arg = self._actions.pop()
        # ActionComponentEat
        # arg.execute_class().execute(arg, self) # ActionComponentはstaticクラス
        # hungry_components = body.get_components(["DurabilityComponentHungry"])
        # hungry_components.add_durability()
    # def execute_action

    # 汎用AI作成時にBodyComponentから得られるパラメータを全て得る
    # ハードコーディングAI用にはget_durabilityなど、個別のget関数を実装してください
    def get_parameters(self):
        pass
    # def get_parameters

    # private

    # 条件反射などBodyComponent自身で判断して、何かする処理
    def _update_self(self):
        pass
    # def _update_self
# BodyComponentHungrySimple

# test code
if __name__ == '__main__':
    body = BodyComponentHungrySimple()
