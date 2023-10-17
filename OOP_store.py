from item import Item
from phone import Phone

Phone.instantiate_from_csv('phone.csv')
print(Phone.all)