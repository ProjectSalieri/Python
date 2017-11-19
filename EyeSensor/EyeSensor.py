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

if __name__ == '__main__':
    eye_sensor = EyeSensor()

    # 規格統一のために256x256などにリサイズ

    # 計算リソースが足りないので当面は16x16ずつの平均カラーを計算して32x32の画像に落とし込むとかする

    eye_sensor.execute("./Apple.jpg")
