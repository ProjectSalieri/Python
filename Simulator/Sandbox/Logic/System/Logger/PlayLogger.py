# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayLogger.py
# @note

class PlayLog:

    def __init__(self, header, content_hash):
        self._header = header
        self._content_hash = content_hash
    # def __init__

    def get_header(self):
        return self._header
    # def get_header

    def get_content_hash(self):
        return self._content_hash
    # def get_content_hash

class PlayLogger:

    _instance = None

    def __init__(self):
        PlayLogger._instance = self
        self._additional_logger = []
    # def __init__

    @classmethod
    def add_logger(cls, logger):
        PlayLogger.get_instance()._additional_logger.append(logger)
    # def add_logger

    @classmethod
    def put_as_generate_object(cls, actor):
        content_hash = {
            "Name" : actor.get_name()
        }
        play_log = PlayLog("GenerateObject", content_hash)
        PlayLogger._put(play_log)
    # def log_as_generate_object

    @classmethod
    def put_as_dead_object(cls, actor, factor):
        content_hash = {
            "Name" : actor.get_name(),
            "Factor" : factor
        }
        play_log = PlayLog("DeadObject", content_hash)
        PlayLogger._put(play_log)
    # put_as_dead_object

    @classmethod
    def put_as_get_item(cls, item_name, get_user):
        content_hash = {
            "Name" : item_name,
            "GetUser" : get_user.get_name()
        }
        play_log = PlayLog("GetItem", content_hash)
        PlayLogger._put(play_log)
    # def put_as_get_item

    @classmethod
    def put_as_object_life(cls, obj):
        life_component = obj.get_object_component("Life")
        if life_component == None:
            return False
        
        content_hash = {
            "Name" : obj.get_name(),
            "Life" : life_component.get_dulability()
        }
        play_log = PlayLog("ObjectLife", content_hash)
        PlayLogger._put(play_log)
    # def put_as_object_life   

    @classmethod
    def get_instance(cls):
        logger = PlayLogger._instance
        if logger == None:
            logger = PlayLogger()
        return logger

    @classmethod
    def _put(cls, play_log):
        logger = PlayLogger.get_instance()

        for add_logger in logger._additional_logger:
            add_logger.put(play_log)

# class PlayLogger

if __name__ == "__main__":
    pass
