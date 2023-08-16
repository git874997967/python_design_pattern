class Pizza:
    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese 
        
    def __str__(self):
        garlic = 'Yes' if self.garlic else 'No'
        extra_cheese = 'Yes' if self.extra_cheese else 'No'
        info = (f"Garlic: {garlic}",f"Extra Cheese: {extra_cheese}")
        return "\n".join(info)
    
    class PizzaBuilder:
        def __init__(self):
            self.garlic = False
            self.extra_cheese = False
        def add_cheese(self):
            self.extra_cheese = True
            return self 
        def add_garlic(self):
            self.garlic = True
            return self
        def build(self):
            return Pizza(self)

def main():
    pizza = Pizza.PizzaBuilder().add_cheese().add_garlic().build()
    print(pizza)
    
if __name__ == "__main__":
    main()