class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2-x1)**2 + (y2 - y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2-y1) / (x2 - x1)


C1 = (3, 2)
C2 = (8, 10)
myline = Line(C1, C2)
print(myline.distance())
print(myline.slope())

# Bankist Challenge
# Challange 2


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, addbalance):
        self.balance = self.balance + addbalance
        print(f"Added {addbalance} to the balance")

    def withdraw(self, wit_bala):
        if self.balance >= wit_bala:
            self.balance = self.balance - wit_bala
            print(f"Withdraw accepted!!")
        else:
            print("Sorry, Is not enough balance!!")

    def __str__(self):
        return f"Owner: {self.owner} \n Balance: {self.balance}"


a = Account('Miki', 1000)
print(a.owner)
print(a.balance)
print(a.deposite(2000))
print(a.withdraw(4000))
print(a)
