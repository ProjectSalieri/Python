# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SimplePainModule.py

def bytesize(size):
    kb = 1024
    mb = 1024**2
    gb = 1024**3

    if size > gb:
        return "%.1fGB" % (size / gb)
    elif size > mb:
        return "%.1fMB" % (size / mb)
    else:
        return "%fKB" % (size / kb)
# bytesize

class SimplePainModule:

    def __init__(self):
        pass
    # def __init__

    def regression(self):
        pass
    # def calc

    def classify(self):
        pass
    # def calc_classifycation

    def print_raw(self):
        import psutil # pip install psutil
        import shutil
        
        cpu_percent = psutil.cpu_percent(interval=0)
        print("CPU使用率:%.1f" % (cpu_percent))

        memory_info = psutil.virtual_memory()
        print("メモリ情報")
        print("\t総量:%s" % (bytesize(memory_info.total)))
        print("\t使用率:%.1f" % (memory_info.percent))
        print("\t空き:%s" % (bytesize(memory_info.available)))
        print("\t使用中:%s" % (bytesize(memory_info.used)))

        disk_usage = shutil.disk_usage("/")
        print("ストレージ情報")
        print("\t総量:%s" % (bytesize(disk_usage.total)))
        print("\t空き:%s" % (bytesize(disk_usage.free)))
        print("\t使用中:%s" % (bytesize(disk_usage.used)))
    # def print_raw

    # private method
    
    def raw_pain_input(self):
        pass
    # def raw_pain_input

# class SimplePainModule

# test code
if __name__ == '__main__':

    pain_module = SimplePainModule()
    pain_module.print_raw()
    
    pass
