# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file EyeSensor.py
# @note 画像情報を抽出

from PIL import Image

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
    def __init__(self):
        pass
    # end __init__

    # 実行関数
    def execute(self, img_file):
        img = Image.open(img_file)

        width, height = img.size
        
        image_dim = width*height*3
        middle_layer_num = width*height
        import TLP
        tlp = TLP.TLP(image_dim, middle_layer_num, image_dim)
        input_buf = self._create_input_from_img(img)

        # 学習Start
        answer_buf = self._create_input_from_img(img)
        for i in range(20):
            for j in range(1):
                tlp.backpropagation(input_buf, answer_buf)
            output_buf = tlp.output(input_buf)
            error = 0.0
            for o in range(len(output_buf)):
                error += (output_buf[o] - answer_buf[o])*(output_buf[o] - answer_buf[o])
            print(error)
        # 学習End

        output_buf = tlp.output(self._create_input_from_img(img))

        new_img = Image.new("RGB", (width, height))
        for x in range(width):
            for y in range(height):
                buf_offset = (y*width + x)*3
                new_img.putpixel( (x, y), 
                                  (round_value(output_buf[buf_offset]), round_value(output_buf[buf_offset+1]), round_value(output_buf[buf_offset+2])) )
        new_img.show()
        
    # end execute

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
    #new_size = (32, 32)
    new_size = (16, 16)
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

    input_file = "./SampleImage/Apple.jpg"

    test_file = preprocess(input_file)

    eye_sensor.execute(test_file)
