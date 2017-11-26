# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAI.py
# @note AIのモック

import EyeSensor

class MockAI:
    def __init__(self):
        self.eye_sensor = EyeSensor.EyeSensor(16, 16)
    # end __init__

    def remind(self, input_file):
        feature = self.eye_sensor.execute(input_file)

        # test
        for i in range(len(feature)):
            feature[i] = -feature[i]

        self.eye_sensor.reconstruct(feature)
    # end remind
# end class MockAI

if __name__ == '__main__':
    input_file = "./SampleImage/Chris.jpg"

    ai = MockAI()
    ai.remind(input_file)
