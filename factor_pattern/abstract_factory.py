class Actor:
    def __init__(self):
        pass 
    def __str__(self):
        pass 
    def interact_with(self):
        pass

class Obstacle:
    def __str__(self):
        pass 
    def action(self):
        pass 
    
class Frog(Actor):
    def __init__(self,name):
        self.name = name 
    def __str__(self):
        return self.name 
    
    def interact_with(self,obstacle):
        print(f"{self} the Frog encounters {obstacle} and {obstacle.action()}")
        
class Bug(Obstacle):
    def __str__(self):
        return "a bug"
    def action(self):
        return "eats it"

class Frog_World:
    def __init__(self,name):
        print(self)
        self.player_name = name 
    
    def __str__(self):
        return "\n\n\t------Frog World------"
    
    def make_characters(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()
        
class Wizard(Actor):
    def __init__(self,name):
        self.name = name 
    def __str__(self):
        return self.name 
    
    def interact_with(self,obstacle):
        print(f"{self} the Wizard battles against {obstacle} and {obstacle.action()}")    
        
class Ork(Obstacle):
    def __str__(self):
        return " an evil ork"
    def action(self):
        return "kills it"
        
    
class WizardWorld:
    def __init__(self,name):
        print(self)
        self.player_name = name 
    
    def __str__(self):
        return "\n\n\t ------Wizard World------"
    
    def make_characters(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()
        

class AbstractFactory:
    def __init__(self):
        pass 
    def play(self):
        pass
    
class GameEnvironmentFactory(AbstractFactory):
    def __init__(self,name,age):
        factory = Frog_World(name) if age < 18 else WizardWorld(name)
        self.hero = factory.make_characters()
        self.obstacle = factory.make_obstacle()
    
    def play(self):
        self.hero.interact_with(self.obstacle)
    
def validate_age(name):
    try:
        age = input(f"Welcome {name} how old are you?")
        age = int(age)
    except ValueError as ve:
        print(f"Age{age} is invalid. Please try again")
        return (False,age)
    return (True, age)

def main():
    name = input("Hello what's your name?")
    validate_input = False
    while not validate_input:
        validate_input,age = validate_age(name)
    env = GameEnvironmentFactory(name,age)
    env.play()   
    
if __name__ == "__main__":
    main()