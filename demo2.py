# -*- coding: utf-8 -*-
# _author:"hancel"
# date:2019/12/30

'''
字典翻转输出
描述
读入一个字典类型的字符串，反转其中键值对输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬

即，读入字典key:value模式，输出value:key模式。
'''
# a = input()
# try:
#     a = eval(a)
#     print(dict(zip(a.values(), a.keys())))
# except:
#     print('输入错误')

import jieba

with open('沉默的羔羊.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) > 2:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
print(items[0][0], items[0][1])
print(items)
