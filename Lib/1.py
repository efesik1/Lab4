class CustomList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} not found in the list.")

    def get_length(self):
        return len(self.items)

    def display_items(self):
        if self.is_empty():
            print("The list is empty.")
        else:
            print("List items:")
            for item in self.items:
                print(item)

my_list = CustomList()

my_list.add_item(1)
my_list.add_item(2)
my_list.add_item(3)

my_list.display_items()

print(f"Length of the list: {my_list.get_length()}")

my_list.remove_item(2)

my_list.display_items()
