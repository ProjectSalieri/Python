# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file EyeSensor.py
# @note 画像情報を抽出

from PIL import Image
import AutoEncoder

def round_value(value):
    value /= 10.0
    value *= 255
    value += 128.0
    if value < 0.0:
        return 0
    elif value > 255.0:
        return 255
    else:
        return (int)(value)

class EyeSensor:

    # コンストラクタ
    def __init__(self, width, height):
        self.width = width
        self.height = height

        image_dim = self.width*self.height*3
        middle_layer_num_array = [self.width*self.height*3*2, self.width*self.height/2, self.width*self.height*3*2]
        output_layer_middle_layer_num = self.width*self.height*3 + 10
        self.auto_encoder = AutoEncoder.AutoEncoder(image_dim, middle_layer_num_array, output_layer_middle_layer_num)
        self.param_path = "./AutoEncoder" + str(self.width) + "x" + str(self.height) + ".param"
        self.auto_encoder = self.auto_encoder.deserialize(self.param_path)
    # end __init__

    def learn(self, image_file):
        preprocessed_file = self._preprocess(image_file)
        return self._learn(preprocessed_file)

    def save(self):
        self.auto_encoder.serialize(self.param_path)

    def execute(self, image_file):
        preprocessed_file = self._preprocess(image_file)
        return self._execute(preprocessed_file)

    def _resize_image(self, image_file, output_file, size_tuple):
        img = Image.open(image_file)
        resize_image = img.resize(size_tuple)
        resize_image.save(output_file)

    def _preprocess(self, image_file):
        preprocessed_file = "./Test.jpg"

        # 規格統一のために256x256などにリサイズ
        self._resize_image(image_file, preprocessed_file, (256, 256))

        # 計算リソースが足りないので当面は16x16ずつの平均カラーを計算して32x32の画像に落とし込むとかする
        # 256x256 -> 16x16
        self._resize_image(preprocessed_file, preprocessed_file, (self.width, self.height))
 
        return preprocessed_file
    #end def preprocess

    # 学習関数
    def _learn(self, img_file):
        img = Image.open(img_file)
        input_buf = self._create_input_from_img(img)

        # 学習Start
        answer_buf = self._create_input_from_img(img)
        self.auto_encoder.pre_learn(input_buf)
        output_buf = self.auto_encoder.output(input_buf)
        error = 0.0
        for o in range(len(output_buf)):
            error += (output_buf[o] - answer_buf[o])*(output_buf[o] - answer_buf[o])
        # 学習End
        return error

    # 実行関数
    def _execute(self, img_file):
        img = Image.open(img_file)

        # 特徴量に変換
        input_buf = self._create_input_from_img(img)
        feature = self.auto_encoder.calc_feature(input_buf)

        return feature
    # end execute

    def reconstruct(self, feature):
        output_buf = self.auto_encoder.calc_feature_to_output(feature)

        new_img = Image.new("RGB", (self.width, self.height))
        for x in range(self.width):
            for y in range(self.height):
                buf_offset = (y*self.width + x)*3
                new_img.putpixel( (x, y), 
                                  (round_value(output_buf[buf_offset]), round_value(output_buf[buf_offset+1]), round_value(output_buf[buf_offset+2])) )
        new_img.show()

    def _create_input_from_img(self, img):
        width, height = img.size
        image_dim = width*height*3
        input_buf = [ 0.0 for i in range(image_dim) ]
        for h in range(height):
            for w in range(width):
                offset = h*width*3 + w*3
                pix = img.getpixel((w, h))
                for c in range(3):
                    input_buf[offset + c] = (pix[c] - 128.0)/ 255.0*10.0 # 正規化 + 左右対称に( -5 ~ 5)

        return input_buf

# end Class EyeSensor

if __name__ == '__main__':
    eye_sensor = EyeSensor(8, 8)

    learn_itr = 10

    input_files = [
        "./SampleImage/Apple.jpg",
        "./SampleImage/HiroseSuzu.jpg",
        "./SampleImage/Forest.jpg",
        "./SampleImage/Cat.jpg",
        "./SampleImage/Chris.jpg",
        "./SampleImage/Mushroom.jpg",
        "./SampleImage/Orange.jpg",
        "./SampleImage/Masu.jpg"
        ]

    for itr in range(learn_itr):
        import random
        random.shuffle(input_files)
        for input_file in input_files:
            error = eye_sensor.learn(input_file)
            print(str(error) + " : " + input_file)
            eye_sensor.save()

    for input_file in input_files:
        eye_sensor.reconstruct(eye_sensor.execute(input_file))
