"""
Name: Diraj Ravikumar
Student ID: 13255244
GitHub Link: https://github.com/dirajravikumar/DirajRavikumarA2


Date: 08 June 2016
Program Details: This program is used to hire or return items, also allows new items to be added with the use of Python and Kivy.
"""

from kivy.app import App
from kivy.lang import Builder


from itemlist import ItemList

class ItemsForHire(App):

    def __init__(self, **kwargs):

        super(ItemsForHire, self).__init__(**kwargs)
        self.list_item = ItemList()
        item_lines_list = open("items.csv","r+")
        self.items = []
        for line in item_lines_list:
            self.items.append(line + ",False")
            self.list_item.store(line)
        self.names = []
        self.price = 0.00

    def build(self):

        self.title = "Equipment Hire"
        self.root = Builder.load_file('main.kv')
        self.listing_items()
        return self.root

    def listing_items(self):
        pass


    def hiring_items(self):
        pass

    def returning_items(self):
        pass

    def confirming_items(self):
        pass

    def adding_new_items(self):
        pass

ItemsForHire().run()


