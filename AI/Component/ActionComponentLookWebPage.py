# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActionComponentLookWebPage
# @note

from IActionComponent import IActionComponent
from IBodyComponent import IBodyComponent
from ComponentArgStimulusLook import ComponentArgStimulusLook
from ComponentArgLookWebPage import ComponentArgLookWebPage

class ActionComponentLookWebPage(IActionComponent):
    def __init__(self, virtual_body):
        self._virtual_body = virtual_body
    # def __init__

    def execute(self, args):
        result = self._execute_core(args)
        print(result)

        # 結果をComponentArgに変換
        stimulate_args = []
        for image_file in result["image_file"]:
            stimulate_args.append(ComponentArgStimulusLook(image_file))

        self._stimulate(stimulate_args)
        
        # look_arg = 
        # self._virtual_body.try_stimulate(look_arg)
        pass
    # def execute

    # private
    def _executable_arg_types(self):
        return [ComponentArgLookWebPage.ARG_TYPE]
    # def _execute_arg_types

    def _execute_core(self, args):
        execute_args = self._executable_args(args)

        result = {"text" : [], "image_file" : [], "url" : []}
        for arg in execute_args:
            sub_result = ActionComponentLookWebPage._access_to_url(arg.url)
            for k in sub_result:
                result[k] += sub_result[k]
            # for
        # for args

        return result
    # def _execute_core

    def _stimulate(self, args):
        for arg in args:
            self._virtual_body.try_stimulate(arg)
        # for
    # def _stimulate

    def _access_to_url(url):
        result = {"text" : [], "image_file" : [], "url" : []}

        # test code
        import os
        result["image_file"].append(os.path.join(os.path.dirname(__file__), "..", "..", "EyeSensor", "SampleImage", "Orange.jpg"))
        
        return result
    # def _access_to_url
# class ActionComponentLookWebPage


if __name__ == '__main__':
    action = ActionComponentLookWebPage(IBodyComponent())
    action._execute_core([ComponentArgLookWebPage()])
