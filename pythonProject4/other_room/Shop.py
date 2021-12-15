class Shop:
    def __init__(self,shop_name,items_list,Items_price,Available_list_items):
        self.items_price=Items_price
        self.items_list=items_list
        self.Available_list_items=Available_list_items
        self.shop_name=shop_name
    def display_items(self):
        return f"This store also has these {self.items_list} items and price is {self.items_price}man. the Available items is {self.Available_list_items}number"
    def Shop_detail(self):
        return f"This canteen's name is {self.shop_name}"


# shop1=Shop("Elsevar's shop",["pencil","book","copybook"],[1,3,2],[10,4,6])
# print(shop1.Shop_detail())
# print(shop1.display_items())
