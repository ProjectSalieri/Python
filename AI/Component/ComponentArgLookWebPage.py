# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgLookWebPage.py
# @note

from IComponentArg import IComponentArg
class ComponentArgLookWebPage(IComponentArg):
    ARG_TYPE = "LookWebPage"

    def __init__(self, url):
        self._url = url
        pass
    # def __init__

    def url(self):
        return self._url
    # def url

    def arg_type(self):
        return ComponentArgLookWebPage.ARG_TYPE
    # def arg_type
# class ComponentArgLookWebPage
