guet_list=['33','小红','小丽']
messagge1=guet_list[0]+"你愿意和我共进晚餐吗？"
messagge2=guet_list[1]+"你愿意和我共进晚餐吗？"
messagge3=guet_list[2]+"你愿意和我共进晚餐吗？"
print(messagge1)
print(messagge2)
print(messagge3)
print(guet_list[2]+ "无法赴约")
guet_list[2]='小美'
messagge1=guet_list[0]+"你愿意和我共进晚餐吗？"
messagge2=guet_list[1]+"你愿意和我共进晚餐吗？"
messagge3=guet_list[2]+"你愿意和我共进晚餐吗？"
print(messagge1)
print(messagge2)
print(messagge3)
print("我找到了更大的餐桌，因此我能够邀请更多的人和我共进晚餐")
guet_list.insert(0,'冰冰')
guet_list.insert(3,'同桌')
#加入列表末尾
guet_list.append('丁香')
print("截至现在，我共邀请了"+str(len(guet_list))+"位嘉宾和我共进晚餐！")
print(guet_list[0]+"你愿意和我共进晚餐吗？")
print(guet_list[1]+"你愿意和我共进晚餐吗？")
print(guet_list[2]+"你愿意和我共进晚餐吗？")
print(guet_list[3]+"你愿意和我共进晚餐吗？")
print(guet_list[4]+"你愿意和我共进晚餐吗？")
print(guet_list[5]+"你愿意和我共进晚餐吗？")

#在上述基础进行删减列表
print("由于我新购买的餐桌无法及时送达，故只能邀请2位朋友和我共进晚餐。")
person1=guet_list.pop(0)
print(person1+"很抱歉由于个人的原因不能邀请你和我共进晚餐！")
person2=guet_list.pop(0)
print(person2+"很抱歉由于个人的原因不能邀请你和我共进晚餐！")
person3=guet_list.pop(0)
print(person3+"很抱歉由于个人的原因不能邀请你和我共进晚餐！")
person4=guet_list.pop(0)
print(person4+"很抱歉由于个人的原因不能邀请你和我共进晚餐！")


print(guet_list[0]+"你仍然在我的受邀人之列")
print(guet_list[1]+"你仍然在我的受邀人之列")
#删除列表中元素
del guet_list[1]
del  guet_list[0]
print(guet_list)




