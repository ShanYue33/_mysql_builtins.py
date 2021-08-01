requested_topping = 'mushrooms'
if requested_topping == 'mushrooms':
    print(True)
if requested_topping != 'mushrooms':
    print(False)
print(requested_topping.lower())
number = 3
if number == 3:
    print("该数字是正确的！")
if number != 3:
    print("该数字不正确！")

age = 13
if age < 14:
    print(True)
if age > 6:
    print(True)
if age == 13:
    print(True)
if 6 < age < 20:
    print(True)
if age > 14 or age < 20:
    print(True)
fruits_list = ['apple', 'peer', 'orange']
if 'apple' in fruits_list:
    print(True)
if 'cherry' not in fruits_list:
    print(True)
