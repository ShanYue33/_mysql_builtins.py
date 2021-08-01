# -*- coding:utf-8 -*-
# @Project Name:selfStudyProject
# @FileName          :backup_v2.py
# @Create Date       :2021/7/22 23:01
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""@Functions.

    1.To backup important documents/directory in my computer
    2.Notes:
        Changed backup directory structure!
        Command lines programs with parameters assignment
        Using zipfile package to zip documents
"""
import os
import time
import zipfile

source = ['C:\\Users\\ys\\Desktop\\项管\\优干推荐 岳姗',
          'C:\\Users\\ys\\Desktop\\项管\\优干申请 郝成昊']
backup_dir = 'D:\\backup\\'
today = backup_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):  # 用os.exists函数检验在主备份目录中是否有以当前日期作为名称的目录，如果没有，则使用os.mkdir函数创建
    os.mkdir(today)
    '''
    os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
    如果目录有多级，则创建最后一级，如果最后一级目录的上级目录有不存在的，则会抛出一个 OSError。
    os.mkdir(path)
    其参数path 为要创建目录的路径。
    '''
    print('Successfully created directory', today)
else:
    print('Directory %s is already existed.' % today)

print('\nBegin zipping...')
target = today + os.sep + now + '.zip'
'''
主要用于系统路径中的分隔符
根据你的操作系统给出目录分隔符，使程序更具有移植性
'''
zipfs = zipfile.ZipFile(target, 'w')
for doc in source:
    print('Adding backup file:', doc)
    fn = os.path.basename(doc)
    '''
    os.path.basename()
    返回path最后的文件名
    '''
    zipfs.write(doc, arcname=fn)
    '''
    zipfile 内置提供的将文件压缩存储在.zip文件中，arcname 即zip文件中存入文件的名称
    给予的归档名为 arcname 默认情况下将与filename一致，但是不带驱动器盘符并会移除开头的路径分隔符
    '''

print('\nFollowing files are backed up in the zip file:', target)
print(zipfs.namelist())
zipfs.close()
