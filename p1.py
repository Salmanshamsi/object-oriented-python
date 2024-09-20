
# create class..
#  
class shop:

# define class values
    taxRate = 20
    amount = 0

# define constructor
    def __init__(self,amount, product):
        # validiation to recive args.
        assert amount >= 0
        self.amount = amount
        print(f"get the amount: {amount} and product: {product} in constructor !")

# define class method
    def calculateFinalResult(self,product):
        return f"you final amount is {self.amount - self.taxRate} !"
    


# create an instance of class A..

user1 = shop(0,"monitor")
user2 = shop(20,"TV")

print(user1.calculateFinalResult("abc"))
print(user2.calculateFinalResult("xyz"))



