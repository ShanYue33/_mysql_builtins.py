# -*- coding:utf-8 -*-
# @Project Name:selfStudyProject
# @FileName          :backup_v4.py
# @Create Date       :2021/7/23 16:05
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""
Version:3.0.0
@Functions:
    1.To backup important documents/directory in my computer
    2.Notes:
        Employ function
        Revise directory backup
"""

import os
import time
import zipfile


def backup(zipfs, doc):
    """
    Putting document(doc) into zip file stream(zipfs)
    whatever the doc is a file or a directory
    """
    if os.path.isdir(doc):  # directory
        print(' Adding directory:, doc')
        sub_dir = doc.split('\\')[-2] + '\\'  # 备份最后一级目录名称
        for file in os.listdir(doc):
            print('   Adding backup file:', file)
            fn = os.path.basename(file)
            zipfs.write(file, arcname=sub_dir + fn)
        else:
            print('  Adding backup file:', doc)
            fn = os.path.basename(doc)
            zipfs.write(doc, arcname=fn)


source = ['C:\\Users\\ys\\Desktop\\项管\\优干推荐 岳姗\\2020年度“昆明理工大学优秀共青团干部”申报表 岳姗.docx',
          'C:\\Users\\ys\\Desktop\\项管\\优干申请 郝成昊\\郝成昊.docx']
backup_dir = 'D:\\backup\\'

today = backup_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)
else:
    print('Directory %s is already existed.' % today)

comment = input('Enter a comment -->')  # 增加备份标注信息
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + ".zip"

print('\nBegin zipping ...')
zipfs = zipfile.ZipFile(target, 'w')
for doc in source:
    backup(zipfs, doc)

print('\nFollowing files are backed up')
print(zipfs.namelist())
zipfs.close()
print('\nBACKUP ENDED in the file', target)
