import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] #empty list to list all the items we have in the shop
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self) #appending each instance

    @property
    # property decorator - read only attribute
    def name(self):
        return self.__name
    
    @name.setter
    # one way to still apply new values is with setter
    def name(self, value):
        self.__name = value
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')" #best practice, this way we can copy from the console and create
    # the instance

    @classmethod
    def instantiate_from_csv(cls, filename): 
        with open(filename,'r') as f: #reading the parameters as dictionary
            reader = csv.DictReader(f) #reading the content as a list of dictionaries
            items = list(reader) #converting the dictionary to list
# 'items.csv'
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
            # now we are able to instantiate each object
            # print(item)
        
        # we need to pass at least 1 parameter from each method (if method of instance), 
        # this 
        # method is actually meant to instantiate the object so we can't use it inside the object


# for instance in Item.all:
#     print(f"name of instance is:{instance.name}")

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # i.e: 5.0, 2.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
