ages = [1, 3, 3, 9, 16, 23, 40, 80]
for age in ages:
    if age < 2:
        print("该人是婴儿！")
    elif 2 < age < 4:
        print("该人是儿童！")
    elif 13 < age < 20:
        print("该人是青少年！")
    elif 20 < age < 65:
        print("该人是成年人！")
    else:
        print("该人是老年人！")
