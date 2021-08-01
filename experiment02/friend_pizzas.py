pizza = ['super pizza', 'seafood pizza', 'savory pizza']
friend_pizzas=pizza[:]
friend_pizzas.append('fruits pizza')
print(pizza)
print(friend_pizzas)
print("My favorite piazzas are:")
for favorite_pizzas in pizza:
    print(favorite_pizzas)
print("My friend's favorite pizzas are:")
for favorite_pizzas in friend_pizzas:
    print(favorite_pizzas)