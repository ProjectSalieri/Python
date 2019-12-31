# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActionExecutor
# @note


class ActionExecutor:

    def __init__(self):
        self._current_action = {
            "Lower" : None,
            "Upper" : None,
            "Brain" : None
        }
    # def __init__

    def try_start_action(self, action):
        execute_parts = action.get_execute_parts()
        for parts in execute_parts:
            if self._current_action[parts] != None:
                return False
        for parts in execute_parts:
            self._current_action[parts] = action
        
        return True
    # def try_start_action

    def try_start_action_with_cancel(self, action):
        pass
    # def try_start_action_with_cancel

    def update(self):
        current_actions = list(set(self._current_action.values()))
        for action in current_actions:
            if action == None:
                continue
            action.update()

        for key in list(self._current_action.keys()):
            if self._current_action[key] == None:
                continue
            if self._current_action[key].is_end():
                self._current_action[key] = None
    # def update

# class ActionExecutor
