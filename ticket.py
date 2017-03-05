class Ticket:
    def __init__(self,isweekday=False,ischild=False):
        self.price = 100
        if isweekday:
            self.i = 1.2
        else:
            self.i = 1
        if ischild:
            self.discount = 0.5
        else:
            self.discount = 1

    def  calculate(self,num=1):
        self.ticket_price = self.price*self.i*self.discount*num
        return self.ticket_price
adult = Ticket()
child = Ticket(ischild=True)
print(adult.calculate(num=2)+child.calculate(num=3))



