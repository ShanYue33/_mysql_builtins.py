# -*- coding:utf-8 -*-
# @Project Name:_mysql_builtins.py
# @FileName          :pickling.py
# @Create Date       :2021/8/1 15:19
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
import pickle as p

"""
Python 提供一个标准的模块，称为pickle。使用它可以在文件中存储任何Python 对象，之后又可以·把它完整无缺的取出来
称为对象持久化
"""
shopListFile = 'shoplift.data'  # filename where we will pickle data
shopList = ['apple', 'mango', 'carrot', 'litchi']  # list object

# write to the file
f = open(shopListFile, 'wb')  # wb means writing by bytes
p.dump(shopList, f)  # dump the object to a file
f.close()

del shopList  # remove the shoplift variable

# Read back from the storage
f = open(shopListFile, 'rb')  # rb:read file by byte
storedList = p.load(f)
print(storedList)
f.close()
