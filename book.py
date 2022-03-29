from functools import total_ordering
import pandas as pd
@total_ordering
class Order:
    def __init__(self,quantity,price,priority,id,buy=True):
        self.quantity = quantity
        self.price = price
        self.priority = priority
        self.id=id
    def is_sell(self):
        return not self.buy
    def __repr__(self):
        return "Order(%s, %s)" % (self.quantity, self.price)
    def __str__(self):
        return "%s @ %s" % (self.quantity, self.price)
    def __eq__(self, other):
        return other and self.quantity == other.quantity and self.price == other.price
    def __lt__(self, other):
        return other and self.price < other.price
    def is_priority(self,other):
        return other and self.priority < other.priority

class Book:
    def __init__(self, name):
        self.name=name
        self.buy_orders = []
        self.sell_orders = []
        self.executed_order = []
        self.counter = 1

    def insert_order(self, quantity, price, buy =True):
        if buy:
            priority = len(self.buy_orders) + 1
            id = self.counter
            new_order = Order(quantity, price, priority, id, buy)
            if len(self.buy_orders) == 0:
                self.buy_orders.append(new_order)
            else:
                for i in range(len(self.buy_orders)):
                    order_iter = self.buy_orders[i]
                    if new_order.price > order_iter.price:
                        self.buy_orders.insert(i,new_order)
                        break
                    elif i == len(self.buy_orders) - 1:
                        self.buy_orders.append(new_order)
            print("---Insert BUY",new_order,"id=",new_order.id,"on",self.name,'\n')
        else:
            priority = len(self.sell_orders)+1
            id=self.counter
            new_order=Order(quantity,price,priority,id,buy)
            if len(self.sell_orders)==0:
                self.sell_orders.append(new_order)
            else:
                for i in range(len(self.sell_orders)):
                    order_iter=self.sell_orders[i]
                    if new_order.price < order_iter.price:
                        self.sell_orders.insert(i,new_order)
                        break
                    elif i==len(self.sell_orders)-1:
                        self.sell_orders.append(new_order)
            print("---Insert SELL", new_order,"id", new_order.id,"on",self.name,'\n')
        self.executed()
        print("Book on",self.name,'\n')
        for sell_order_iter in self.sell_orders:
            print("SELL",sell_order_iter,"id=",sell_order_iter.id,'\n')
        for buy_order_iter in self.buy_orders:
            print("BUY", buy_order_iter,"id=",buy_order_iter.id,'\n')
        print("---------------------------------------------------------",'\n')
        self.counter +=1
    def executed(self):
        while((self.buy_orders !=[] and self.sell_orders!=[]) and (self.buy_orders[0]>=self.sell_orders[0])):
            if self.buy_orders[0].quantity < self.sell_orders[0].quantity:
                self.executed_orders.append([self.buy_orders[0].quantity, self.buy_orders[0].price])
                print("Execute", self.buy_orders[0].quantity, "at", self.buy_orders[0].price, "on", self.name, '\n')
                self.sell_orders[0].quantity = self.sell_orders[0].quantity - self.buy_orders[0].quantity
                del self.buy_orders[0]
            elif self.buy_orders[0].quantity > self.sell_orders[0].quantity:
                self.executed_orders.append([self.sell_orders[0].quantity, self.buy_orders[0].price])
                print("Execute", self.sell_orders[0].quantity, "at", self.buy_orders[0].price, "on", self.name, '\n')
                self.buy_orders[0].quantity = self.buy_orders[0].quantity - self.sell_orders[0].quantity
                del self.sell_orders[0]
            else:
                self.executed_orders.append([self.sell_orders[0].quantity, self.buy_orders[0].price])
                print("Execute", self.sell_orders[0].quantity, "at", self.buy_orders[0].price, "on", self.name, '\n')
                del self.sell_orders[0]
                del self.buy_orders[0]



def data(self):
    datasell = {'QUANTITY':[1,120,10],'PRICE' :[10,12,10]}
    databuy = {'QUANTITY' : [2,10,5],'PRICE' : [11,10,10]}
    df1 = pd.DataFrame(datasell, comlums = ['QUANTITY', 'PRICE'])
    df2 = pd.DataFrame(databuy, comlums = ['QUANTITY', 'PRICE'])
    print("SELL ORDERS :",  '\n', df1)
    print("BUY ORDERS :",  '\n', df2)
test_book=Book('A')
    
print(test_book.sell_orders)
test_book.insert_order(5, 10, False)
print(test_book.sell_orders)
test_book.insert_order(5, 15, False)
print(test_book.sell_orders)
test_book.insert_order(5, 14, False)
print(test_book.sell_orders)
test_book.insert_order(3, 14, False)
print(test_book.sell_orders)
test_book.insert_order(40, 14, False)
print(test_book.sell_orders)
test_book.insert_order(5, 5, False)
print(test_book.sell_orders)

print(test_book.sell_orders)
print(test_book.buy_orders)
test_book.executed()
print(test_book.sell_orders)
print(test_book.buy_orders)
print(test_book.executed_orders)
print(test_book.buy_orders[0].price)
print(test_book.sell_orders[0].price)

    
test_book2 = Book('B')

test_book2.insert_order(10, 10)
print("liste des ordres d'achats :")
print(test_book2.buy_orders)
test_book2.insert_order(5, 11, False)
print("liste des ordres de ventes :")
print(test_book2.sell_orders)
print("liste des transactions :")
print(test_book2.executed_orders)
print(test_book2.buy_orders[0])
print(test_book2.sell_orders[0])
test_book2.executed()
print('\n')

test_book2.insert_order(123, 10.5)
print("liste des ordres d'achats :")
print(test_book2.buy_orders)
print("liste des ordres de ventes :")
print(test_book2.sell_orders)
print("liste des transactions :")
print(test_book2.executed_orders)
test_book2.executed()
print('\n')

test_book2.insert_order(62, 11, False)
print("liste des ordres d'achats :")
print(test_book2.buy_orders)
print("liste des ordres de ventes :")
print(test_book2.sell_orders)
print("liste des transactions :")
print(test_book2.executed_orders)
test_book2.executed()
print('\n')

test_book2.insert_order(16, 10.6, False)
print("liste des ordres d'achats :")
print(test_book2.buy_orders)
print("liste des ordres de ventes :")
print(test_book2.sell_orders)
print("liste des transactions :")
print(test_book2.executed_orders)
test_book2.executed()
print('\n')

test_book2.insert_order(2, 10.6)
print("liste des ordres d'achats :")
print(test_book2.buy_orders)
print("liste des ordres de ventes :")
print(test_book2.sell_orders)
print("liste des transactions :")
print(test_book2.executed_orders)
test_book2.executed()
print('\n')

print("liste des ordres d'achats finaux :")
print(test_book2.buy_orders)
print("liste des ordres de ventes finaux:")
print(test_book2.sell_orders)
print("liste des transactions finaux:")
print(test_book2.executed_orders)

