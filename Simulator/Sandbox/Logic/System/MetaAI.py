#
# @file MetaAI.py
# @brief メタAI
#

from .ObjectRegionDirectorBase import ObjectRegionDirectorBase

import Object

class MetaAI(ObjectRegionDirectorBase):

    def __init__(self):
        super().__init__()

        self._count = 0
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

        self._count = self._count + 1
        if self._count < 300:
            return add_objects
        else:
            self._count = 0

        add_objects += self._generate_food(objects)
        add_objects += self._generate_enemy(objects)

        return add_objects
    # def _generate

    def _generate_enemy(self, objects):
        add_objects = []

        if len(objects) > 7:
            return add_objects

        import random
        object = Object.Object("SampleEnemy")
        object.reset_pos((100 + random.randint(-50, 50), 0, 100 + random.randint(-50, 50)))
        add_objects.append(object)

        return add_objects
    # def _generate_enemy

    def _generate_food(self, objects):
        add_objects = []

        if len(objects) > 7:
            return add_objects

        import random
        object = Object.Object("Apple")
        object.reset_pos((100 + random.randint(-50, 50), 0, 100 + random.randint(-50, 50)))
        add_objects.append(object)

        return add_objects
    # def _generate_food

if __name__ == "__main__":
    pass
