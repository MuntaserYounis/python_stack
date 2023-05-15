class store:
    def __init__(self,name):
        self.name = name
        self.list = []
    def add_product(self,new_product):
        self.list.append(new_product)
    def sell_product(self,id):
        self.list.pop(id)
        

class product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            self.price*=(1+percent_change)
        else:
            self.price*=(1-percent_change)
    def print_info(self):
        print(self.name,self.category,self.price)

apple= product('apple',10,'fruits')
apple.print_info()

my_market = store('myMarket')
my_market.add_product(apple)
print(my_market.list[0].name,my_market.list[0].category)
my_market.sell_product(0)
