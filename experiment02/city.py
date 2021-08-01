# 字典里嵌套字典
cities = {'chengdu': {'country': 'China', 'population': '600万', 'fact': '被誉为天府之国'},
          'Kunming': {'country': 'China', 'population': '400万', 'fact': '被誉为植物王国'},
          'shanghai': {'country': 'China', 'population': '300万', 'fact': '被誉为东方明珠'}}
for cityName, information in cities.items():
    country_information = information['country']
    population_information = information['population']
    fact_information = information['fact']
    print("\n" + cityName.title() + "属于：" + country_information + ", 拥有的人口数量为：" + population_information
          + ", 并且被" + fact_information)
