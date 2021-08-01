current_users = ['小明', '小红', '小董', '小贝', '33']
new_users = ['小华', '小明', '小猫', '33', '小狗']
for name in new_users:
    if name in current_users:
        print("该应户名已经被使用，请输入新的用户名！")
    else:
        print("该用户名暂未被使用！")
