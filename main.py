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
from kivy.uix.popup import Popup

from itemlist import ItemList

__author__ = "Diraj Ravikumar"

num_lines = sum(1 for line in open('items.csv'))

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
                temp_button = Button(text = name, background_color=(1,0,0,1))
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
                temp_button = Button(text=name, background_color=(1, 0, 0, 1))
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
                temp_button = Button(text=name, background_color=(1, 0, 0, 1))
            temp_button.bind(on_press=self.item_press)
            self.root.ids.item_buttons.add_widget(temp_button)


    def item_press(self, instance):
        item_count = 0
        for line in self.list_item:
            name, desc, price, hire = line.split(',')
            if instance.text == name:
                if self.root.ids.list_item.background_color == [0, 0.99, 0.99, 1]:
                    self.root.ids.main_label.text = "{} ({}), ${:,.2f} is {}".format(name, desc, float(price), hire)

                elif self.root.ids.hire_item.background_color == [0, 0.99, 0.99, 1]:
                    part = self.items[item_count].split(",")
                    if "in" in hire:
                        if part[4] == "False":
                            part[4] = "True"
                            self.items[item_count] = "{},{},{},{},{}".format(str(part[0]).strip("[]").replace("'", ""), str(part[1]).strip("[]").replace("'", ""), str(part[2]).strip("[]").replace("'", ""), part[3].replace("'", ""), str(part[4]).strip("[]").replace("'", ""))
                            self.root.ids.main_label.text = "Hiring: {} for ${:,.2f}.".format(name, float(price))
                    else:
                        self.root.ids.main_label.text = "Hiring nothing."

                elif self.root.ids.return_item.background_color == [0, 0.99, 0.99, 1]:
                    part = self.items[item_count].split(",")
                    if "out" in hire:
                        if part[4] == "False":
                            part[4] = "True"
                            self.items[item_count] = "{},{},{},{},{}".format(str(part[0]).strip("[]").replace("'", ""), str(part[1]).strip("[]").replace("'", ""), str(part[2]).strip("[]").replace("'", ""), part[3].replace("'", ""), str(part[4]).strip("[]").replace("'", ""))
                            self.root.ids.main_label.text = "Returning: {}.".format(name)
                    else:
                        self.root.ids.main_label.text = "Returning nothing."
            item_count += 1

    def confirming_items(self):
        with open("items.csv") as file:
            item_lines_list = file.readlines()
        for instance in self.root.ids.item_buttons.children:
            for item_count in range(len(self.items)):
                self.part = self.items[item_count].split(',')
                if instance.text in self.part:
                    if (self.part)[3] == 'in\n' and (self.part)[4] == 'True':
                        (self.part)[3] = 'out\n'
                        (self.part)[4] = "False"
                        self.items[item_count] = "{},{},{},{},{}".format(str(self.part[0]).strip("[]").replace("'", ""), str(self.part[1]).strip("[]").replace("'", ""), str(self.part[2]).strip("[]").replace("'", ""), self.part[3].replace("'", ""), str(self.part[4]).strip("[]").replace("'", ""))
                        item_lines_list[item_count] = item_lines_list[item_count].replace('in', 'out')
                        self.list_item.clear()
                        for line in item_lines_list:
                            self.list_item.store(line)
                        with open("items.csv", "w") as file:
                            file.writelines(item_lines_list)
                        self.listing_items()
                    elif (self.part) [3] == 'out\n' and (self.part)[4] == 'True':
                        (self.part) [3] = 'in\n'
                        (self.part) [4] = "False"
                        self.items[item_count] = "{},{},{},{},{}".format(str(self.part[0]).strip("[]").replace("'", ""), str(self.part[1]).strip("[]").replace("'", ""), str(self.part[2]).strip("[]").replace("'", ""), self.part[3].replace("'", ""), str(self.part[4]).strip("[]").replace("'", ""))
                        item_lines_list[item_count] = item_lines_list[item_count].replace('out', 'in')
                        self.list_item.clear()
                        for line in item_lines_list:
                            self.list_item.store(line)
                        with open("items.csv", "w") as file:
                            file.writelines(item_lines_list)
                        self.listing_items()

    def adding_new_items(self):
        self.root.ids.item_buttons.clear_widgets()
        self.root.ids.list_item.background_color = (1, 1, 1, 1)
        self.root.ids.hire_item.background_color = (1, 1, 1, 1)
        self.root.ids.return_item.background_color = (1, 1, 1, 1)
        self.root.ids.confirm_item.background_color = (1, 1, 1, 1)
        self.root.ids.new_item.background_color = (0, 0.99, 0.99, 1)

        new_item = Builder.load_file('new_item.kv')
        self.pop_up = Popup(title="Add New Item",content=new_item)
        self.pop_up.open()

    def saving_new(self, name, desc, price, label):

        def price_validity(price):
            try:
                float(price)
                return True
            except ValueError:
                return False

        if len(name.strip()) == 0 or len(desc.strip()) == 0 or len(price.strip()) == 0:
            label.text = "All fields must be completed"
        elif price_validity(price) == False:
            label.text = "Price must be valid number"
        elif price_validity(price) == True and float(price) < 0:
            label.text = "Price cannot be negative"
        else:
            item_new = "{},{},{},in".format(name, desc, float(price))
            with open("items.csv", "a") as file:
                file.writelines(item_new)
            self.list_item.store(item_new)
            self.cancel_new()
            self.listing_items()

    def cancelling_new(self):
        self.pop_up.dismiss()
        self.listing_items()

    def on_stop(self):
        print("{} items saved to items.csv".format(num_lines))

ItemsForHire().run()


