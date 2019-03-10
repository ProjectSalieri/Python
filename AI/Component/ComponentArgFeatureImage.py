# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgFeatureImage.py
# @note

from IComponentArg import IComponentArg

class ComponentArgFeatureImage(IComponentArg):
    ARG_TYPE = "FeatureImage"

    def __init__(self, feature):
        self._feature = feature
    # def __init__

    def feature(self):
        return self._feature
    # def feature

    def arg_type(self):
        return ComponentArgFeatureImage.ARG_TYPE
    # def arg_type
# class ComponentArgFeatureImage

if __name__ == '__main__':
    feature_image_arg = ComponentArgFeatureImage([1, 2, 3])
    print("[ArgType]:" + feature_image_arg.arg_type())
    print("[Arg]feature:" + str(feature_image_arg.feature()))
