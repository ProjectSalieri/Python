# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file AIUtil.py
# @note 

import os
import sys

#
# 初期化
#
def initialize():
    # .tmpフォルダを設定
    tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".tmp")
    os.environ["TOOL_TMP"] = tmp_dir
    ## python3 tempfileモジュール用
    os.environ["TMPDIR"] = tmp_dir
    os.environ["TEMP"] = tmp_dir
    os.environ["TMP"] = tmp_dir

    
# def initialize

# test code
if __name__ == '__main__':
    import AIUtil
    AIUtil.initialize()

    print(os.environ.get("TOOL_TMP"))
