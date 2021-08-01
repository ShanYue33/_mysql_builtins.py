river = {'nile': 'egypt', 'yellow river': 'China', 'Yangest river': 'China'}
river_name = ['nile', 'yellow river', 'Yangest river']
for name in river.keys():
    print(name.title())
    if name in river_name:
        print("The " + name.title() + " through " + river[name].title())
for river_name in river.keys():
    print("\n" + river_name)
for country_name in river.values():
    print("\n" + country_name)
