# -*- coding: utf-8 -*-
#
# @file AutoEncoder.py
# @brief 多層パーセプトロン

#
import TLP

class AutoEncoder:
    def __init__(self, input_dim, middle_layer_num_array, output_layer_middle_layer_num):
        self.tlp_array = []
        # auto encoder
        pre_middle_layer_num = input_dim
        for middle_layer_num in middle_layer_num_array:
            tlp = TLP.TLP(pre_middle_layer_num, middle_layer_num, pre_middle_layer_num)
            self.tlp_array.append(tlp)
            pre_middle_layer_num = middle_layer_num
        self.output_layer_tlp = TLP.TLP(middle_layer_num_array[-1], output_layer_middle_layer_num, input_dim)
    # end __init__

    def deserialize(self, param_file):
        import pickle
        import os
        if os.path.exists(param_file) == False:
            return self
        auto_encoder = self
        with open(param_file, "rb") as f:
            auto_encoder = pickle.load(f)
        return auto_encoder
    # end deserialize

    def serialize(self, param_file):
        import pickle
        with open(param_file, "wb") as f:
            pickle.dump(self, f)
    # end serialize

    def pre_learn(self, input_buf):
        is_test = False

        cur_input_buf = input_buf
        for tlp_idx in range(len(self.tlp_array)):
            cur_tlp = self.tlp_array[tlp_idx]
            # fixme テスト
            if is_test == True and tlp_idx != (int)(len(self.tlp_array) / 2):
                cur_input_buf = cur_tlp.middle_output(cur_input_buf)
                continue

            cur_tlp.backpropagation(cur_input_buf, cur_input_buf)
            cur_input_buf = cur_tlp.middle_output(cur_input_buf)

        # output_layer_tlpの学習
        if is_test == False:
            self.output_layer_tlp.backpropagation(cur_input_buf, input_buf)
    # end pre_learn

    # 単純出力
    def output(self, input_buf):
        cur_input_buf = input_buf
        for tlp_idx in range(len(self.tlp_array)):
            cur_tlp = self.tlp_array[tlp_idx]
            cur_input_buf = cur_tlp.middle_output(cur_input_buf)
        return self.output_layer_tlp.output(cur_input_buf)
    # end output

    # 特徴量層出力
    def calc_feature(self, input_buf):
        feature_idx = (int)(len(self.tlp_array) / 2) # 奇数層決め打ち(ex 3層(0, 1, 2) -> 1

        cur_input_buf = input_buf
        for tlp_idx in range(feature_idx):
            cur_tlp = self.tlp_array[tlp_idx]
            cur_input_buf = cur_tlp.middle_output(cur_input_buf)
        return self.tlp_array[feature_idx].middle_output(cur_input_buf)
    # end calc_feature

    # 特徴量層 -> 最終出力層
    def calc_feature_to_output(self, feature):
        feature_idx = (int)(len(self.tlp_array) / 2) # 奇数層決め打ち(ex 3層(0, 1, 2) -> 1
        cur_input_buf = feature
        for tlp_idx in range(len(self.tlp_array)):
            if tlp_idx <= feature_idx:
                continue
            cur_tlp = self.tlp_array[tlp_idx]
            cur_input_buf = cur_tlp.middle_output(cur_input_buf)
        return self.output_layer_tlp.output(cur_input_buf)
    # end calc_feature_to_output
        

if __name__ == '__main__':
    pass
