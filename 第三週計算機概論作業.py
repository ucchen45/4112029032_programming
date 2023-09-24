# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:31:25 2023

@author: youxi
"""

import os
import shutil
import time
os.mkdir("CS")
with open("CS/homework.txt","w") as file:
    file.write("4112029032_陳又晞")
with open("CS/homework.txt","r") as file:
    print(file.read())
file_size=os.path.getsize("CS/homework.txt")
print(f"文件大小：{file_size}字元")
modification_time=os.path.getmtime("CS/homework.txt")
print(f"最後修改時間：{modification_time}")
formatted_time=time.ctime(modification_time)
print(f"最後修改時間(人類可讀格式)：{formatted_time}")
shutil.rmtree("CS")