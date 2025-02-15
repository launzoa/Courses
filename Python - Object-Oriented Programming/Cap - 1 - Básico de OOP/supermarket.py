class Product:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity
        
    def __str__(self):
        return f"Product, title: {self.title}, quantity: {self.quantity}"
    
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity
        
    
class Supermarket:
    def __init__(self, title):
        self.title = title
        self.items = []
        
    def __str__(self):
        return f"Shopping List, Item: {self.title}, Quantidade de itens: {len(self.items)}"
    
    def add(self, new_item):
        if isinstance(new_item, Product):
            self.items.append(new_item)
            print("Novo item adicionado!")

        else: 
            print("O novo item não é um produto")
        
    def show(self):
        print(f"Número de itens {len(self.items)}")
        for item in self.items:
            print(item.title, item.quantity)
            
