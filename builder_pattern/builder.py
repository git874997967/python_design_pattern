from enum import Enum 
import time 

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauces = Enum('PizzaSauces', 'tomato creme_fraiche')
PizzaToppings = Enum('PizzaToppings','mozzarella double_mozzarella bacon ham oregano red_onion mushrooms')
STEP_DELY = 3

class Pizza:
    def __init__(self,name):
        self.name = name 
        self.dough = None 
        self.sauce = None 
        self.topping = []
        
    def __str__(self):
        return self.name 
    
    def prepare_dough(self,dough):
        self.dough = dough 
        print(f"preparing {self.dough.name} for your {self.name}")
        time.sleep(STEP_DELY)
        print(f"done with {self.dough.name} dough")
        
class MargaritaBuilder(Pizza):
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progess  = PizzaProgress.queued
        self.baking_time = 5
        
    def prepare_dough(self):
        self.progess = PizzaProgress.preparation 
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_source(self):
        print('adding the tomato sauce to your margarita ...')
        self.pizza.sauce = PizzaSauces.tomato
        print('done with tomato sauce')       

    def add_topping(self):
        print("add the topping (double_mozzarella, oregano) to your margarita")
        self.pizza.topping.append([i for i in (PizzaToppings.double_mozzarella, PizzaToppings.oregano)])
        time.sleep(STEP_DELY)
        print('done with double_mozzarella and oregano')
        
    def baking(self):
        self.progess = PizzaProgress.baking 
        print(f"baking your margarita for {self.baking_time} seconds")
        time.sleep(self.baking_time)
        self.progess = PizzaProgress.ready 
        print(f"done with your margarita")
        
        
class CreamyBaconBuilder(Pizza):
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progess  = PizzaProgress.queued
        self.baking_time = 7
        
    def prepare_dough(self):
        self.progess = PizzaProgress.preparation 
        self.pizza.prepare_dough(PizzaDough.thick)
    
    def add_source(self):
        print("adding the cremey fraiche sauce to your creamy bacon...")
        self.pizza.sauce = PizzaSauces.creme_fraiche
        time.sleep(STEP_DELY)
        print('done with cremey fraiche sauce')
    
    def add_topping(self):
        print("add the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon")
        self.pizza.topping.append([i for i in (PizzaToppings.mozzarella, PizzaToppings.bacon, PizzaToppings.ham, PizzaToppings.mushrooms, PizzaToppings.red_onion, PizzaToppings.oregano)])
        time.sleep(STEP_DELY)
        print('done with mozzarella, bacon, ham, mushrooms, red onion')
        
    def baking(self):
        self.progess = PizzaProgress.baking 
        print(f"baking your creamy bacon for {self.baking_time} seconds")
        time.sleep(self.baking_time)
        self.progess = PizzaProgress.ready 
        print(f"done with your creamy bacon")
        
class Waiter:
    def __init__(self):
        self.builder = None 
        
    def construct_pizza(self,builder):
        self.builder = builder 
        [step() for step in (builder.prepare_dough, builder.add_source, builder.add_topping, builder.baking)]
        
    @property
    def pizza(self):
        return self.builder.pizza

def validate_stype(builders):
    validate_input = False
    try:
        pizza_style = input("What pizza style would you like to order? [m]arilla, [c]reamy bacon")
        builder = builders[pizza_style]()
        validate_input = True 
    except KeyError :
        print("Sorry, only [m]argarita and [c]reamy bacon are available at the moment")
        return (validate_input,None)
    return (validate_input,builder)
        
def main():
    builders = dict(m = MargaritaBuilder, c = CreamyBaconBuilder)
    validate_input = False 
    while not validate_input:
        validate_input,builder = validate_stype(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    
    print(f"Enjoy your {pizza} pizza!")
    pass

if __name__ == "__main__":
    main()