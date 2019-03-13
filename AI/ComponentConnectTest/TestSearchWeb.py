# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file TestSearchWeb.py
# @note ウェブ探索のテスト

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from Component.ActionComponentLookWebPage import ActionComponentLookWebPage
from Component import BodyComponentPCVirtual
from Component.ComponentArgFeatureImage import ComponentArgFeatureImage
from Component.ComponentArgLookWebPage import ComponentArgLookWebPage
from Component.ComponentArgStimulusLook import ComponentArgStimulusLook

if __name__ == "__main__":
    # Bodyに視覚刺激
    body = BodyComponentPCVirtual.BodyComponentPCVirtual()
    body.enable()

    image_file = os.path.join(os.path.dirname(__file__), "..", "..", "EyeSensor", "SampleImage", "Apple.jpg")
    look_arg = ComponentArgStimulusLook(image_file)
    body.try_stimulate(look_arg)

    for i in range(2):
        features = []
        cnt = 0
        while len(features) == 0:
            print("\rLoopWait for pop_features:" + str(cnt), end="")
            features = body.pop_features([ComponentArgFeatureImage.ARG_TYPE])
            cnt += 1

        # image_fileからDesireComponent更新

        # DesireComponentからurlを生成

        # LookPageAction
        action = ActionComponentLookWebPage(body)
        action.execute([ComponentArgLookWebPage("https://ja.wikipedia.org/wiki/%E3%83%AA%E3%83%B3%E3%82%B4")])
    # for 
    body.disable()
