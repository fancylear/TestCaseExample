#!/usr/bin/python
from uiautomator import device as d
import time

# 开关屏幕
for i in range(1,50):
    d.screen.on()
    time.sleep(0.5)
    d.screen.off()
