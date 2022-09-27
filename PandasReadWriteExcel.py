# -*- coding: utf-8 -*-

""" 
@Author  : qiuhanqiu
@Time    : 2022/1/15 15:17
"""

import os

import pandas as pd

from GetFileLIst import GetFileList


class PandasReadWriteExcel(object):
    def __init__(self, new_file):
        self.new_file = new_file

    pd.set_option("display.max_columns", None)

    # 读取多个Excel的数据,写入同一个Excel的不同sheet
    def writedifsheet(self, path):
        writer = pd.ExcelWriter(self.new_file)
        i = 0
        for file in path:
            if file != self.new_file:
                i += 1
                sheetname = "sheet{}".format(i)
                df = pd.read_excel(file)
                df.to_excel(writer, sheetname)
                # print(df)
        writer.save()

    # 读取多个Excel的数据,写入同一个Excel的一个sheet
    def writedonesheet(self, path):
        writer = pd.ExcelWriter(self.new_file)
        start_line = 0
        for file in path:
            if file != self.new_file:
                df = pd.read_excel(file)
                # print(df)
                # 写入同一个sheet，确定每次写入的起始行
                df.to_excel(writer, startrow=start_line)
                # print(start_line)
                # dataframe的行数不包含表头。需要+1
                start_line += (len(df) + 1)
        writer.save()

    # 读取多个Excel的数据,写入同一个Excel的一个sheet.只保留第一个表头，其余只写入数据
    def writedonesheetdistinct(self, path):
        writer = pd.ExcelWriter(self.new_file)
        start_line = 0
        for file in path:
            if file != self.new_file:
                if start_line == 0:
                    df = pd.read_excel(file)
                else:
                    # 如果不是第一个表格从第三行开始读数据
                    df = pd.read_excel(file, header=2)
                # print(df)
                # 写入同一个sheet，确定每次写入的起始行
                df.to_excel(writer, startrow=start_line)
                # print(start_line)
                # dataframe的行数不包含表头。需要+1
                start_line += (len(df) + 1)
        writer.save()


if __name__ == '__main__':
    dir_path = r'C:\Users\81477\Desktop\test\冷知识测试题 （2021-2022年）'
    file_path = GetFileList().getfilelist(dir_path)
    new_file_name = os.path.join(dir_path, 'all_data.xls')
    # PandasReadWriteExcel(new_file_name).writedifsheet(file_path)
    # PandasReadWriteExcel(new_file_name).writedonesheet(file_path)
    PandasReadWriteExcel(new_file_name).writedonesheetdistinct(file_path)
