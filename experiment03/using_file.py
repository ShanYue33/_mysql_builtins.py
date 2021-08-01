# -*- coding:utf-8 -*-
# @Project Name:_mysql_builtins.py
# @FileName          :using_file.py
# @Create Date       :2021/7/27 22:45
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
poem = '''
Programming is fun
When the work is done
If you wanna make your work also fun
Use Python!
'''
f = open('poem.text', 'w')  # open for 'w'riting
f.write(poem)  # write text to file
f.close()

f = open('poem.text')  # 如果没有指定文件打开模式，则默认为读的模式
while True:
    line = f.readline()
    if len(line) == 0:  # 当空的字符串被返回时
        break
    print(line)
f.close()  # 文件使用结束后，必须进行关闭
