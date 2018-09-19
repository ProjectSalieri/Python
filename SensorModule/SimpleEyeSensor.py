# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SimpleEyeSensor.py
# @note 画像情報を抽出

from PIL import Image

def clamp(v, min, max):
    if v < min:
        return min
    if v > max:
        return max
    return v
# def clamp

class SimpleEyeSensor:

    # コンストラクタ
    def __init__(self, width, height):
        pass
    # end __init__
    
    #
    # 実行
    # 画像を特徴量変換する
    #
    def execute(self, image_path):
        import tempfile
        feature = None
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=True) as fp:
            preprocessed_file = self._preprocess(image_path, fp.name)
            #print(fp.name)
            feature = self._execute(preprocessed_file)
        return feature
    #def execute

    #
    # 特徴量を視覚化
    #
    def visualize_feature(self,  feature):
        height = 64
        width = 64
        img = Image.new("RGB", (height, width))

        import math
        v_arr = [feature[3], feature[4], feature[5]]
        diff_arr = list(map(lambda v: 2.0*math.sqrt(v), v_arr)) # 2*sigmaが95%におさまる

        half_h = height / 2
        half_w = width / 2
        dist_max = half_h #math.sqrt(half_h*half_h + half_w*half_w)

        # 上から正規分布でグラーデーション
        for w in range(width):
            for h in range(height):
                pix_arr = [0, 0, 0]
                pos_y = -half_h + h
                r = pos_y / dist_max
                for c in range(3):
                    pix_arr[c] = (int)(clamp(feature[c] + r*diff_arr[c], 0, 255))
                # for c
                img.putpixel((w, h), (pix_arr[0], pix_arr[1], pix_arr[2]))
            # for h
        # for w
        img.show()
    # def visualize_feature

    # private
    
    #
    def _execute(self, image_path):
        # RGBの平均、分散の順番
        # @note 垂直方向の分散と横方向の分散で分けても面白そうだった(ex. キノコ)
        feature = [255, 0, 0, 1.0, 1.0, 1.0] # dummy

        img = Image.open(image_path)
        mean_arr = [0.0, 0.0, 0.0]
        variance_arr = [0.0, 0.0, 0.0]
        size = img.width * img.height
        # 平均計算
        for w in range(img.width):
            for h in range(img.height):
                pix = img.getpixel((w, h))
                for c in range(3):
                    mean_arr[c] += pix[c]
                # for c
            # for h
        # for w
        mean_arr = list(map(lambda p: p/size, mean_arr))

        # 分散計算
        for w in range(img.width):
            for h in range(img.height):
                pix = img.getpixel((w, h))
                for c in range(3):
                    diff = mean_arr[c] - pix[c]
                    variance_arr[c] += diff*diff
                # for c
            # for h
        # for w
        variance_arr = list(map(lambda v: v/size, variance_arr))

        for c in range(3):
            feature[c] = mean_arr[c]
            feature[c+3] = variance_arr[c]
        # for c
    	
        return feature
    # def _execute

    def _resize_image(self, image_file, output_file, size_tuple):
        img = Image.open(image_file)
        resize_image = img.resize(size_tuple)
        resize_image.save(output_file)
    # def _resize_image

    #
    # 前処理
    #
    def _preprocess(self, image_file, preprocessed_img_path):

        # 規格統一のために256x256などにリサイズ
        self._resize_image(image_file, preprocessed_img_path, (256, 256))
 
        return preprocessed_img_path
    #def _preprocess
    	

# Class SimpleEyeSensor


# SampleCode
if __name__ == '__main__':
    import os, sys
    sys.path.append(os.path.dirname(__file__) + "/..")
    sys.dont_write_bytecode = True
    import AIUtil
    AIUtil.initialize()
    
    eye_sensor = SimpleEyeSensor(256, 256)

    import os
    sample_images = [
        "../EyeSensor/SampleImage/Apple.jpg",
        "../EyeSensor/SampleImage/Chris.jpg",
        "../EyeSensor/SampleImage/Forest.jpg",
        "../EyeSensor/SampleImage/HiroseSuzu.jpg",
        "../EyeSensor/SampleImage/Orange.jpg",
    ]
    sample_images = map(lambda f: os.path.join(os.path.dirname(os.path.abspath(__file__)), f), sample_images)

    for img_file in sample_images:
        print(img_file)
        feature = eye_sensor.execute(img_file)
        # 
        eye_sensor.visualize_feature(feature)
    # for img_file

