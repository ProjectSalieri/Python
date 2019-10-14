# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActorUtil.py
# @note

import json
import os

class ActorUtil:

    @staticmethod
    def get_actor_setting(actor_name):
        actor_data_dir = ActorUtil._actor_data_dir()
        actor_json = os.path.join(actor_data_dir, "Actor", "%s.Actor.json" % (actor_name))
        actor_setting = None
        with open(actor_json) as f:
            actor_setting = json.load(f)

        return actor_setting
    # def actro_setting

    @staticmethod
    def get_component_setting(actor_setting, component_name):
        component_json = os.path.join(ActorUtil._actor_data_dir(), actor_setting["Components"][component_name])
        component_setting = None
        with open(component_json) as f:
            component_setting = json.load(f)
        return component_setting
    # def get_component_path

    @staticmethod
    def _actor_data_dir():
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "ActorData")
    # def _actor_data_dir

# class ActorUtil
