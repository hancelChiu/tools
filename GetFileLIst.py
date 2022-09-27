# -*- coding: utf-8 -*-

""" 
@Author  : qiuhanqiu
@Time    : 2022/1/15 15:02
"""

import os


class GetFileList():

    def getfilelist(self,path):
        files_path = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(path, file)
                files_path.append(file_path)
            return files_path


if __name__ == '__main__':
    dir_path = r'C:\Users\81477\Desktop\test\冷知识测试题 （2021-2022年）'
    file_list = GetFileList().getfilelist(dir_path)
    # print(file_list)


