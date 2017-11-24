# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file TLP.py
# @note 三層パーセプトロン

import random
import math

class TLP:
    def __init__(self, input_dim, middle_layer_num, output_dim):
        self.input_dim = input_dim
        self.middle_layer_num = middle_layer_num
        self.output_dim = output_dim
        self.w_i = []
        self.w_o = []

        # input -> middleのウェイト
        for i in range(self.input_dim+1):
            self.w_i.append([self._random_weight() for m in range(self.middle_layer_num)])

        # middle -> outputのウェイト
        for o in range(self.output_dim):
            self.w_o.append([self._random_weight() for m in range(self.middle_layer_num+1)])
    # end __init__

    def deserialize(self, param_file):
        import pickle
        import os
        if os.path.exists(param_file) == False:
            return self
        tlp = self
        with open(param_file, "rb") as f:
            tlp = pickle.load(f)
        return tlp
    # end deserialize

    def serialize(self, param_file):
        import pickle
        with open(param_file, "wb") as f:
            pickle.dump(self, f)
    # end serialize

    def output(self, input_buf):
        middle_output_buf = self.middle_output(input_buf)
        output_buf = self.middle_to_output(middle_output_buf)
        return output_buf
    # end output

    def middle_output(self, input_buf):
        middle_output_buf = [ 0.0 for m in range(self.middle_layer_num) ]
        for m in range(self.middle_layer_num):
            sum = self.w_i[self.input_dim][m]
            for i in range(self.input_dim):
                sum += input_buf[i] * self.w_i[i][m]
            try:
                exp_v = math.exp(-sum)
                middle_output_buf[m] = 1.0 / ( 1.0 + math.exp(-sum) )
            except OverflowError:
                middle_output_buf[m] = 0.0
            
        return middle_output_buf

    def middle_to_output(self, middle_output_buf):
        output_buf = [ self.w_o[o][self.middle_layer_num] for o in range(self.output_dim) ]

        for o in range(self.output_dim):
            sum = 0.0
            for m in range(self.middle_layer_num):
                sum += middle_output_buf[m] * self.w_o[o][self.middle_layer_num]
            output_buf[o] += sum

        return output_buf
    # end middle_to_output

    def backpropagation(self, input_buf, output_buf):
        eta = 0.01

        middle_output_buf = self.middle_output(input_buf)
        predict_buf = self.middle_to_output(middle_output_buf)

        # 最終層修正
        for o in range(self.output_dim):
            delta_error = (predict_buf[o] - output_buf[o])
            for m in range(self.middle_layer_num):
                self.w_o[o][m] -= eta*(delta_error)*(middle_output_buf[m])
            self.w_o[o][self.middle_layer_num] -= eta*delta_error

    # end backpropagation

    def _random_weight(self):
        return random.uniform(-1, 1)
    # end _random_weight
# end class TLP

if __name__ == '__main__':
    pass
