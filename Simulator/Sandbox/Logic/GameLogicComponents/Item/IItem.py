# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IItem.py
# @note

class IItem:

    def __init__(self):
        self._item_name = None
    # def __init__

    def init_from_setting(self, settings):
        self._item_name = settings["Name"]
    # init_from_setting

    def get_item_name(self):
        return self._item_name
    # def get_item_name

    def update(self):
        pass

    def post_update(self):
        pass

# class IItem

if __name__ == "__main__":
    pass
