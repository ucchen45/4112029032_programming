# -*- coding: utf-8 -*-
"""4112029032第一周作業.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N-tAVIj0C8m_WreMpN085yjD37AMxJR5
"""

height = float(input("請輸入您的身高（公尺）："))
weight = float(input("請輸入您的體重（公斤）："))
bmi = weight/(height**2)
print("%.2f"%bmi)