# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayLogger.py
# @note

import datetime

class PlayLog:

    def __init__(self, header, content_hash):
        self._header = header
        self._content_hash = content_hash

        self._content_hash["LogTime"] = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
    # def __init__

    def get_header(self):
        return self._header
    # def get_header

    def get_content_hash(self):
        return self._content_hash
    # def get_content_hash

    @classmethod
    def get_object_common_content(cls, obj):
        content = {
            "Name" : obj.get_name(),
            "ObjectId" : obj.get_object_id()
        }
        return content
    # def get_object_common_content

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
        content_hash = PlayLog.get_object_common_content(actor)
        play_log = PlayLog("GenerateObject", content_hash)
        PlayLogger._put(play_log)
    # def log_as_generate_object

    @classmethod
    def put_as_dead_object(cls, actor, factor):
        content_hash = PlayLog.get_object_common_content(actor)
        content_hash["Factor"] = factor
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
    def put_as_use_item(cls, item_name, user):
        content_hash = {
            "Name" : item_name,
            "User" : user.get_name()
        }
        play_log = PlayLog("UseItem", content_hash)
        PlayLogger._put(play_log)
    # def put_as_use_item

    @classmethod
    def put_as_object_status(cls, obj):
        life_component = obj.get_object_component("Life")
        content_hash = PlayLog.get_object_common_content(obj)
        content_hash["Pos"] = obj.get_pos()
        content_hash["Life"] = -1 if life_component == None else life_component.get_dulability()
        play_log = PlayLog("ObjectStatus", content_hash)
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
