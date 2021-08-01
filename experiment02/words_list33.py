words_list = {'print': '输出', 'input': '输入', 'for': '循环', 'else': '判断循环'}
words_list['items()'] = '打印字典内容'
words_list['title()'] = '标题化'
for key, value in words_list.items():
    print("\nkey:" + key)
    print("Value:" + value)
