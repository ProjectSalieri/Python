# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file EyeSensor.py
# @note 画像情報を抽出

from PIL import Image

class EyeSensor:

    # コンストラクタ
    def __init__(self):
        pass
    # end __init__

    # 実行関数
    def execute(self, img_file):
        img = Image.open(img_file)

        width, height = img.size

        col_ave = [0.0, 0.0, 0.0]
        pix_num = 0
        for x in range(width):
            for y in range(height):
                pix_col = img.getpixel((x, y))
                col_ave[0] += pix_col[0]
                col_ave[1] += pix_col[1]
                col_ave[2] += pix_col[2]
                pix_num += 1

        for i in range(3):
            col_ave[i] = (float)(col_ave[i]) / pix_num
        for x in range(width):
            img.putpixel((x, 0), ((int)(col_ave[0]), 0, 0))
            img.putpixel((x, 1), (0, (int)(col_ave[1]), 0))
            img.putpixel((x, 2), (0, 0, (int)(col_ave[2])))
            for i in range(10):
                img.putpixel((x, 3+i), ((int)(col_ave[0]), (int)(col_ave[1]), (int)(col_ave[2])))

        img.show()
        pass
    # end execute

# end Class EyeSensor

def preprocess(image_file):
    preprocessed_file = "./Test.jpg"

    # 規格統一のために256x256などにリサイズ
    import subprocess
    cmd = "convert -scale 256x256! " + image_file + " " + preprocessed_file
    subprocess.call(cmd, shell=True)

    # 計算リソースが足りないので当面は16x16ずつの平均カラーを計算して32x32の画像に落とし込むとかする
    img = Image.open(preprocessed_file)
    width, height = img.size
    
    # 256x256 -> 16x16
    new_size = (32, 32)
    new_img = Image.new("RGB", new_size)
    for x in range(new_size[0]):
        for y in range(new_size[1]):
            ave = [0, 0, 0]
            blocks = (256/new_size[0], 256/new_size[1])
            ranges = (range(blocks[0]), range(blocks[1]))
            for i in ranges[0]:
                for j in ranges[1]:
                    pix_col = img.getpixel((x*blocks[0]+i, y*blocks[1]+j))
                    for c in range(3): ave[c] += pix_col[c]
            for c in range(3): ave[c] = (int)((float)(ave[c])/64)
            new_img.putpixel((x, y), tuple(ave))
    new_img.save(preprocessed_file)

    new_img.show()
 
    return preprocessed_file
#end def preprocess

if __name__ == '__main__':
    eye_sensor = EyeSensor()

    input_file = "./SampleImage/HiroseSuzu.jpg"

    test_file = preprocess(input_file)

#    eye_sensor.execute(test_file)
