# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file TLP.py
# @note 三層パーセプトロン

class TLP:
    def __init__(self, input_dim, middle_layer_num, output_dim):
        self.input_dim = input_dim
        self.middle_layer_num = middle_layer_num
        self.output_dim = output_dim
        pass
    # end __init__

    def output(self, input_buf):
        middle_output_buf = self.middle_output(input_buf)
        output_buf = self.middle_to_output(middle_output_buf)
        return output_buf
    # end __output__

    def middle_output(self, input_buf):
        middle_output_buf = [ 0.0 for i in range(self.middle_layer_num) ]
        return middle_output_buf

    def middle_to_output(self, middle_output_buf):
        output_buf = [ 0.0 for i in range(self.output_dim) ]
        # test
        import random
        output_buf = [ random.uniform(0, 255) for i in range(self.output_dim) ]
        return output_buf
    # end __middle_to_output
# end class TLP

if __name__ == '__main__':
    pass
