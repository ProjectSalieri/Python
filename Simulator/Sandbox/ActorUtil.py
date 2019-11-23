# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActorUtil.py
# @note

import json
import os

from Logic.AI import IAI
from Logic.Eat import IEat
from Logic.Eat import IEatable
from Logic.Sensor import ISensor
from Logic.Physics import IPhysics

#
from Logic.GameLogicComponents.CharacterAI import AIFactory

# GameDataComponentsは分離予定
from IDraw import IDraw

class ActorUtil:

    @staticmethod
    def load_actor_setting(actor_name):
        actor_data_dir = ActorUtil._actor_data_dir()
        actor_json = os.path.join(actor_data_dir, "Actor", "%s.Actor.json" % (actor_name))
        actor_setting = None
        with open(actor_json) as f:
            actor_setting = json.load(f)
        return actor_setting
    # def actro_setting

    @staticmethod
    def create_object_components(actor_setting):
        setting = actor_setting["ObjectComponents"]
        object_components = {}
        if setting == None:
            return object_components
        settings = ActorUtil.load_component_setting("", setting["SettingPath"])
        for component_name in settings["Components"]:
            component = None
            if component_name == "Physics":
                component = IPhysics.IPhysics()
            # if component_name

            if component == None:
                continue
            
            component.init_from_setting(ActorUtil.load_component_setting("ObjectComponents", settings["Components"][component_name]["SettingPath"]))
            object_components[component_name] = component
            
        # for settings
        return object_components
    # def create_object_components

    @staticmethod
    def create_game_logic_components(actor_setting, actor):
        logic_components = {}
        setting = actor_setting.get("GameLogicComponents")
        if setting == None:
            return logic_components

        settings = setting
        for setting in settings:
            component_name = setting
            component_setting = ActorUtil.load_component_setting("GameLogicComponents", settings[component_name])
            if component_name == "CharacterAI":
                factory = AIFactory.AIFactory()
                logic_components[component_name] = factory.create_ai_component_from_setting(component_setting, actor)
            elif component_name == "ObjectControl":
                pass
        # for
        return logic_components
            
    # def create_game_logic_component

    @staticmethod
    def create_game_data_components(actor_setting):
        settings = actor_setting["GameDataComponents"]
        game_data_components = {}
        for component_name in settings:
            if component_name == "Draw":
                draw_setting = ActorUtil.load_component_setting("GameDataComponents", settings[component_name])
                component = IDraw(draw_setting["Image"])
                game_data_components[component_name] = component
            else:
                pass
            # if component_name
        # for settings
        return game_data_components
    # def create_game_data_component

    @staticmethod
    def load_component_setting(components_category, component_setting_path):
        component_json = os.path.join(ActorUtil._actor_data_dir(), components_category, component_setting_path)
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