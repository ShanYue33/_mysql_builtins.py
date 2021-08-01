# 在字典中存储字典
city = {'小红': {'city1': '昆明', 'city2': '上海'},
        '小明': {'city1': '北京', 'city2': '成都'},
        '小董': {'city1': '石家庄', 'city2': '哈尔滨'}}
for name, cities in city.items():
    city_name = cities['city1'] + " 、" + cities['city2']
    print("\n" + name.title() + "喜欢的城市是：")
    print("\t" + city_name.title())
