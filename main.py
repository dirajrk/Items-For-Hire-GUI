"""
Name: Diraj Ravikumar
Student ID: 13255244
GitHub Link: https://github.com/dirajravikumar/DirajRavikumarA2


Date: 08 June 2016
Program Details: This program is used to hire or return items, also allows new items to be added with the use of Python and Kivy.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from itemlist import ItemList

__author__ = "Diraj Ravikumar"

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

        self.root.ids.item_buttons.clear_widgets()
        self.root.ids.list_item.background_color = (0, 0.99, 0.99, 1)
        self.root.ids.hire_item.background_color = (1, 1, 1, 1)
        self.root.ids.return_item.background_color = (1, 1, 1, 1)
        self.root.ids.confirm_item.background_color = (1, 1, 1, 1)
        self.root.ids.new_item.background_color = (1, 1, 1, 1)
        item_count = 0
        for line in self.list_item:
            name, desc, price, hire = line.split(',')
            if "in" in hire:
                temp_button = Button(text = name, background_color=(0,1,0,1))
            else:
                temp_button = Button(text = name, background_color=(0.9,0.4,0.9,1))
            temp_button.bind(on_press=self.item_press)
            self.root.ids.item_buttons.add_widget(temp_button)
            item_count += 1


    def hiring_items(self):

        self.names = []
        self.price = 0.00
        for item_count, line in enumerate(self.items):
            part = line.split(',')
            part[4] = "False"
            self.items[item_count] = "{},{},{},{},{}".format(str(part[0]).strip("[]").replace("'", ""), str(part[1]).strip("[]").replace("'", ""), str(part[2]).strip("[]").replace("'", ""), part[3].replace("'", ""), str(part[4]).strip("[]").replace("'", ""))
        self.root.ids.item_buttons.clear_widgets()
        self.root.ids.list_item.background_color = (1, 1, 1, 1)
        self.root.ids.hire_item.background_color = (0, 0.99, 0.99, 1)
        self.root.ids.return_item.background_color = (1, 1, 1, 1)
        self.root.ids.confirm_item.background_color = (1, 1, 1, 1)
        self.root.ids.new_item.background_color = (1, 1, 1, 1)
        for line in self.list_item:
            name, desc, price, hire = line.split(',')
            if "in" in hire:
                temp_button = Button(text = name, background_color=(0,1,0,1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0.4, 0.9, 1))
            temp_button.bind(on_press=self.item_press)
            self.root.ids.item_buttons.add_widget(temp_button)


    def returning_items(self):

        self.names = []
        for item_count, line in enumerate(self.items):
            part = line.split(',')
            part[4] = "False"
            self.items[item_count] = "{},{},{},{},{}".format(str(part[0]).strip("[]").replace("'", ""), str(part[1]).strip("[]").replace("'", ""), str(part[2]).strip("[]").replace("'", ""), part[3].replace("'", ""), str(part[4]).strip("[]").replace("'", ""))
        self.names = []
        self.root.ids.item_buttons.clear_widgets()
        self.root.ids.list_item.background_color = (1, 1, 1, 1)
        self.root.ids.hire_item.background_color = (1, 1, 1, 1)
        self.root.ids.return_item.background_color = (0, 0.99, 0.99, 1)
        self.root.ids.confirm_item.background_color = (1, 1, 1, 1)
        self.root.ids.new_item.background_color = (1, 1, 1, 1)
        for line in self.list_item:
            name, desc, price, hire = line.split(',')
            if 'in' in hire:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0.4, 0.9, 1))
            temp_button.bind(on_press=self.item_press)
            self.root.ids.item_buttons.add_widget(temp_button)


    def item_press(self, instance):
        pass

    def confirming_items(self):
        pass

    def adding_new_items(self):
        self.root.ids.item_buttons.clear_widgets()
        self.root.ids.list_item.background_color = (1, 1, 1, 1)
        self.root.ids.hire_item.background_color = (1, 1, 1, 1)
        self.root.ids.return_item.background_color = (1, 1, 1, 1)
        self.root.ids.confirm_item.background_color = (1, 1, 1, 1)
        self.root.ids.new_item.background_color = (0, 0.99, 0.99, 1)

ItemsForHire().run()


