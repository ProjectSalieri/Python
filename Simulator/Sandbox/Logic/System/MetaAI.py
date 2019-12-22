#
# @file MetaAI.py
# @brief メタAI
#

from .ObjectRegionDirectorBase import ObjectRegionDirectorBase

import Object

class MetaAI(ObjectRegionDirectorBase):

    def __init__(self):
        super().__init__()
    # def __init__

    def update(self, objects, center_pos):
        new_object_list = [obj for obj in objects if obj.is_dead() == False]
        
        super().update(new_object_list, center_pos)

        add_objects = self._generate(objects)
        for obj in add_objects:
            new_object_list.append(obj)

        return new_object_list

    def _update_region(self, objs_in_region):
        pass
    # def update

    def _generate(self, objects):
        add_objects = []

        if len(objects) > 10:
            return add_objects
            
        object = Object.Object("Apple")
        object.reset_pos((100, 0, 100))
        add_objects.append(object)

        return add_objects

if __name__ == "__main__":
    pass
