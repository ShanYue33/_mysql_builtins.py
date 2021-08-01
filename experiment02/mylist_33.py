# 第一阶段练习（第一章-第三章）的最后一个综合性练习
fruits_list = ['apple', 'banana', 'orange', 'pear', 'mango', 'strawberry']
# 访问列表元素
print(fruits_list[0])
# 使用方法title(),单词首字母大写
print(fruits_list[3].title())
# 返回列表最后一个元素的两种方法
print(fruits_list[5])
print(fruits_list[-1])
# 使用列表中的各值
message = "33喜欢吃的水果是" + fruits_list[2].title()
print(message)
message = "阿冰喜欢吃的水果是" + fruits_list[4].title() + "和" + fruits_list[5].title()
print(message)
# 修改添加删除元素
# 修改元素
fruits_list[0] = 'cherry'
print(fruits_list)
# 在列表末尾添加元素
fruits_list.append('apple')
print(fruits_list)
# 用insort()在列表任意位置添加元素
fruits_list.insert(3, 'peach')
print(fruits_list)
# 使用del语句删除元素
del fruits_list[4]
print(fruits_list)
# 使用pop()删除元素 删除列表的元素并且用户还能够使用它
new_list = fruits_list.pop()
print(new_list)
print(fruits_list)
# 根据值删除元素，用remove（）
fruits_list.remove('apple')
print(fruits_list)
# 使用sort（）对列表进行永久性排序
fruits_list.sort()
print(fruits_list)
fruits_list.sort(reverse=True)
print(fruits_list)
# 确定列表的长度
len(fruits_list)
