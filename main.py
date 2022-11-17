# -*- coding:utf-8 -*-
import threading
import time
import test3

cancel_tmr = False


def start():
    # 具体任务执行内容
    print("hello world")


def heart_beat():
    # 打印当前时间
    test3.TT();
    threading.Timer(3, heart_beat).start()
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    heart_beat()
    # 15秒后停止定时器
    cancel_tmr = True
