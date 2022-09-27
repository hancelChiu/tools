# -*- coding: utf-8 -*-

""" 
@Author  : qiuhanqiu
@Time    : 2022/9/27 22:01
"""

import jieba

# with open('沉默的羔羊.txt', 'r', encoding='utf-8') as f:
#     txt = f.read()
#     words = jieba.lcut(txt)
#     counts = {}
#     for word in words:
#         if len(word) > 2:
#             counts[word] = counts.get(word, 0) + 1
#     items = list(counts.items())
#     items.sort(key=lambda x: x[1], reverse=True)
# print(items[0][0], items[0][1])
# print(items)


# 读取Excel文件
import openpyxl

# 打开工作簿
workbook = openpyxl.load_workbook('test.xlsx')
# 获取表单
sheet = workbook['test']
temp = ''
for row in sheet.rows:
    for cell in row:
        # print(cell.value, type(cell.value))
        temp += str(cell.value)
words = jieba.lcut(temp)
counts = {}
for word in words:
    if len(word) > 2:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
print(items[0][0], items[0][1])
print(items)