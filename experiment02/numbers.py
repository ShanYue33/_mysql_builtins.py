#字典中套用列表
favorite_numbers = {
    'ken': ['1', '2','3'], 'sher': ['3', '5', '9'], 'mary': ['1', '33', '66']
}
for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "最喜欢的数字是：")
    for number in numbers:
        print("\t" + number.title())
