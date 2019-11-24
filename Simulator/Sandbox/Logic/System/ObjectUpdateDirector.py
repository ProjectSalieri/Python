# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ObjectUpdateDirector
# @note

import math

from .ObjectRegionDirectorBase import ObjectRegionDirectorBase

class ObjectUpdateDirector(ObjectRegionDirectorBase):

    def __init__(self):
        super().__init__()
    # def __init__

    def _update_region(self, objs_in_region):
        for obj in objs_in_region:
            obj.update()
            obj.post_update()
        # for objs_in_region
    # def _update_region
        
# class ObjectUpdateDirector

if __name__ == "__main__":
    pass
