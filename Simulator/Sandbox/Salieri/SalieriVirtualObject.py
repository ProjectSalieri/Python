# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SalieriVirtualObject.py
# @note

class SalieriVirtualObject:

    def __init__(self, name):
        import Object
        self.object = Object.Object(name)
        self.drawer = self.object.drawer
    # def __init__

    def is_dead(self):
        return self.object.is_dead()

    def get_pos(self):
        return self.object.get_pos()

    def get_object_component(self, component_name):
        return self.object.get_object_component(component_name)

    def get_game_logic_component(self, component_name):
        return self.object.get_game_logic_component(component_name)

    def update(self):
        self.object.update()

    def post_update(self):
        self.object.post_update()

# class SalieriVirtualObject

if __name__ == "__main__":
    pass
