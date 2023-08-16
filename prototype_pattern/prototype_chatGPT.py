import copy  
class Shape:
    def __init__(self):
        self.color = self.x = self.y = None 
    
    def clone(self):
        return copy.copy(self)
    
    
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.type = "Circle"   
    
    def draw(self):
        print(f"Drawing a {self.color}, {self.type} at {self.x} and {self.y}")
        
def main():
    circle_proto = Circle()
    circle_proto.color = "Red"
    circle_proto.x = 10
    circle_proto.y = 11
    new_circle = circle_proto.clone()
    new_circle.draw()
    new_circle.color = "Blue"
    new_circle.x = 100
    new_circle.y = 200
    new_circle.draw()
        
if __name__ == "__main__":
    main()
        
