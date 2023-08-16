class Shape:
    def draw(self):
        pass
    
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
        
class Square(Shape):
    def draw(self):
        print("Drawiing a square")
        
class ShapeFactory:
    def create_shape(self,shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Type {shape_type} is not supported yet.")
def main():
    factory = ShapeFactory()
    circle = factory.create_shape('circle')
    circle.draw()
    square = factory.create_shape('square')
    square.draw()
    
    
if __name__ == "__main__":
    main()