# 一百万 用list()可以将range（）生成的数转换为列表
million_list = list(range(1, 1000001))
for count in million_list:
    print(count)
