import csv

# When to use class methods and when to use static methods

class Item:
    @staticmethod 
    def is_integer():
        '''this should do something that has a relationship with the class, 
        but not something that must be unique per instance!
        '''
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship 
        with the class, but usually, those are used to
        manipulate different structures of data to instantiate 
        objects, like we have done with the csv
        '''
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f: #reading the parameters as dictionary
            reader = csv.DictReader(f) #reading the content as a list of dictionaries
            items = list(reader) #converting the dictionary to list

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

