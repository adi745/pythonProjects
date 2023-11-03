from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than zero"
        # call to super function to have access to all attributes / methods
        # Assign to self objects
        self.broken_phones = broken_phones
        # Actions to execute
# Item.instantiate_from_csv()
# print(Item.all)
# print(Item.is_integer(7.0)) #static method call

# phone1 = Phone("IphoneAdi0110", 2000, 4, 2)
# # print(phone1.calculate_total_price())
# phone2 = Phone("GalaxyAdi0110", 300, 3, 1)
# print(Phone.all)
# print(Item.all)
item1 = Item("OtherItem", 750)
print(item1.name)
item1.__name = "Hello"
print(item1.name)