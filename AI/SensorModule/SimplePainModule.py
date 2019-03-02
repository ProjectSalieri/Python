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
        inter = 5
        
        cpu_percent = psutil.cpu_percent(interval=inter)
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

        process = filter(lambda p: p.name() == "Python", psutil.process_iter())
        import time
        # プロセスごとの情報取得
        for i in process:
            print("Python" in i.name())
            retval = [time.time(),i.name,i.pid,i.cpu_percent(interval=inter),i.memory_percent()]
            print(retval)
        
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
