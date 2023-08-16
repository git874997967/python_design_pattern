class Product:
    def __init__(self,name,price):
        self.name, self.price = name ,price 
        
class Order:
    def __init__(self):
        self.products = []
        
    def add_product(self,product):
        self.products.append(product)
        
    def show_order(self):
        
        total_price = sum(p.price for p in self.products)
        my_list = [
             f"{i.name}: {i.price}\n"
             for i in self.products
            ]
        print("".join(my_list))
        print(f"Total price: {total_price}")
        
class OrderBuilder:
    def __init__(self):
        self.order = Order()
    
    def add_product(self,product):
        self.order.add_product(product)
        return self 
    
    def build(self):
        return self.order

def main():
    product_prototype = Product("Prototype",100)
    order_builder = OrderBuilder()
    order_builder.add_product(product_prototype)
    order = order_builder.order
    for i in range(100,200,10):
        order.add_product(Product(f"Prototype_{i}",i))
    order.show_order()
        
   
    
    
if __name__ == "__main__":
    main()