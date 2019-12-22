# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ItemHolder.py
# @note

class ItemHolder:

    def __init__(self):
        self._items = []
        self._is_item_get_action = False
    # def __init__

    def is_item_get_action(self):
        return self._is_item_get_action
    # def is_item_get_action

    def set_is_item_get_action(self):
        self._is_item_get_action = True
    # def set_is_item_get_action

    def reset_flags(self):
        self._is_item_get_action = False
    # def reset_flags

    def add_item(self, item):
        self._items.append(item)
    # def add_item

    def update(self):
        pass

    def post_update(self):
        pass

# class ItemHolder

if __name__ == "__main__":
    pass
