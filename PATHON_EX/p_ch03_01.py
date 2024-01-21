class Fruit():
    
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __str__(self):
        return 'Fruit food name {}, price {}'.format(self._name, self._price)
    
    def __add__(self, x):
        return self._price + x._price
    
    
food1 = Fruit('apple',1000)
food2 = Fruit('bananan', 500)

print(food1)

foodadd = food1 + food2

print(foodadd)