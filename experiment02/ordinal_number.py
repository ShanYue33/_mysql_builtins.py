number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in number_list:
    if number == '1':
        print(number + "st")
    elif number == '2':
        print(number + "nd")
    elif number == '3':
        print(number + "rd")
    else:
        print(number + "th")
