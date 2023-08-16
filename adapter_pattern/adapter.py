class Human:
    def __init__(self,name):
        self.name = name 
        
    def __str__(self):
        return f"{self.name} human"
    
    def speak(self):
        return "Say hello"
    
    
class Synthesizer:
    def __init__(self,name):
        self.name = name 
        
    def __str__(self):
        return f"{self.name} Synthesizer"
    
    def play(self):
        return "Play a song"
    
class Computer:
    def __init__(self,name):
        self.name = name 
    def __str__(self):
        return f"the {self.name} computer"
    
    def execute(self):
        return "execute program"
    
class Adapter:
    def __init__(self,obj,adapt_methods):
        self.obj = obj 
        self.__dict__.update(adapt_methods)
    def __str__(self):
        return str(self.obj)
    

def main():
    objects = [Human('Asus')]
    comp = Computer("zac")
    player = Synthesizer("mac")
    
    objects.append(Adapter(comp,dict(speak = comp.execute)))
    objects.append(Adapter(player,dict(speak = player.play)))
    print("".join(
        [
            f"{str(o)}:{o.speak()}\n" 
            for o in objects
            ]
        )   
    )
if __name__ == "__main__":
    main()