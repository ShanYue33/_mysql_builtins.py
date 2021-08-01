# -*- coding:utf-8 -*-
# @Project Name:selfStudyProject
# @FileName          :backup_v1.py
# @Create Date       :2021/7/22 22:07
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
# @Functions:

#   1.To backup important documents/directory in my computer
#   2.Notes:
#       Command lines programs with parameters assignment
#       Using zipfile package to zip documents
import time
import zipfile

source = ['C:\\Users\\ys\\Desktop\\项管\\优干推荐 岳姗',
          'C:\\Users\\ys\\Desktop\\项管\\优干申请 郝成昊']  # 要备份的文件
backup_dir = 'D:\\backup\\'  # 备份文件存放的目录
target = backup_dir + time.strftime('%y%m%d%H%M%S') + '.zip'  # 指定归档的zip文件目录和文件名
"""
Python time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定
time.strftime(format[, t])
format -- 格式字符串。
t -- 可选的参数t是一个struct_time对象
"""

zipfs = zipfile.ZipFile(target, 'w')  # 建立一个名为target的zip文件流(可写的）
for doc in source:
    print('Adding backup file:', doc)
    zipfs.write(doc)  # 往zip文件中加入一个备份

print('\nFollowing files are backed up in the zip file:', target)
print(zipfs.namelist())  # 检查zip备份包中文件列表
zipfs.close()  # 关闭zip文件流
