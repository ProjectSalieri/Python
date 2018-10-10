# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file AIUtil.py
# @note 

import os
import sys
import glob
import datetime

#
# 初期化
#
def initialize():
    # .tmpフォルダを設定
    tmp_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".tmp")
    )
    os.environ["TOOL_TMP"] = tmp_dir
    ## python3 tempfileモジュール用
    os.environ["TMPDIR"] = tmp_dir
    os.environ["TEMP"] = tmp_dir
    os.environ["TMP"] = tmp_dir

    if os.path.exists(ai_image_memory_path()) == False:
        os.makedirs(ai_image_memory_path())
    
# def initialize

#
# AIインスタンスの生成
#
def create_ai_by_name(ai_name):
    if ai_name == "MockAI":
        from . import MockAI
        return MockAI.MockAI.create() # MockAIモジュールのMockAIクラスのクラススタテイック関数呼び出し
    elif ai_name == "Salieri":
        print("Salieriは未実装")
        return None
    elif ai_name == "Amadeus":
        print("Amadeusは未実装")
        return None
    else:
        print("未定義のAI")
        return None
# def create_ai_by_name

def ai_image_memory_dirname():
    return "AIImageMemory"
# def ai_image_memory_dirname

def ai_image_memory_path():
    return os.path.join(os.environ["TMP"], ai_image_memory_dirname())
# def ai_image_memory_path

#
# AIが使う一時画像ファイルをリフレッシュ
# @note 一定時刻より前
# @note 一定容量以下になるように
#
def refresh_old_ai_image_memory():
    #    for root, dir, files in os.walk(ai_image_memory_path()):
    #        for f in files:
    # 新しいファイル順
    files = sorted(glob.glob(ai_image_memory_path() + "/**", recursive=True), key=os.path.getmtime, reverse=True)
    sum_size = 0
    memory_size = 50*1024*1024 # 50MB
    time_limit = 60*60*6 # 6時間
    now_time = datetime.datetime.now()
    for f in files:
        if os.path.isdir(f):
            continue

        if (now_time - datetime.datetime.fromtimestamp(os.path.getmtime(f))).total_seconds() > time_limit:
            print("refresh memory by time:" + f)
            os.remove(f)
            continue

        # 新しいファイル優先で容量制限
        sum_size = os.path.getsize(f)
        if sum_size > memory_size:
            print("refresh memory by size:" + f)
            os.remove(f)
# def refresh_ai_image_memory

def create_paste_img_h(img1, img2):
    from PIL import Image
    blank_color = (255, 255, 255)
    border_width = 4
    img = Image.new("RGB",
                    (img1.width + img2.width + border_width, max(img1.height, img2.height)),
                        blank_color
        )
    img.paste(img1, (0, 0))
    img.paste(Image.new("RGB", (border_width, img.height), (0, 0, 0)), (img1.width, 0)) # ボーダー
    img.paste(img2, (img1.width + border_width, 0)) # 特徴量可視化
    return img
# def create_paste_img_h
    

# test code
if __name__ == '__main__':
    import AIUtil
    AIUtil.initialize()

    print(os.environ.get("TOOL_TMP"))
    refresh_old_ai_image_memory()
