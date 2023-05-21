
class Trading:
    a=10
    stocks={'amzn':100,'tsla':600,'msft':700}
    def __init__(self,n,e):
        self.name=n
        self.email=e
        print(self.name, 'is created')
        self.wallet=0
        self.portfolio=[]
    def add_money(self,money):
        self.wallet=self.wallet+money
        print('my current wallet balance is',self.wallet)
        
    def show_stocks(self):
        print(self.stocks)

    def buy(self,stock_name):
        p=self.stocks.get(stock_name)
        if p:
            self.portfolio.append(stock_name)
            self.wallet=self.wallet-p
        else:
            print("stock is not available")
    
    def sell(self,stock_name):
        p=self.stocks.get(stock_name)
        if p:
            self.portfolio.remove(stock_name)
            self.wallet=self.wallet+p
        else:
            print("stock is not available")


account1=Trading('akash','akash@gmail.com')
account2=Trading('ujval','ujval@gmail.com')
print(account1.show_stocks())
account1.add_money(1000)
account1.buy('amzn')
account1.buy('tsla')

account1.sell('amzn')
print(account2.wallet)
print(account1.portfolio,account1.wallet)

