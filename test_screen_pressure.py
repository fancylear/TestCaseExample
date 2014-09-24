#!/usr/bin/python
from uiautomator import device as d

import time

# 开关屏幕50次
for i in range(1,50):
    d.sleep()
    time.sleep(0.2)
    d.wakeup()
    time.sleep(0.2)
    # 新增wrapper，检查屏幕是否开启
    # 若没有开启则不正常
    if not d.screen.ison()
        print("第" + i + "次没有正常开启屏幕")
