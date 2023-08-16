class Shape:
    def draw(self):
        pass 
class Circle(Shape):
    def draw(self):
        print("drawing a circle")

class Square(Shape):
    def draw(self):
        print("drawing a square")

class Color:
    def fill(self):
        pass 
    
class Red(Color):
    def fill(self):
        print("Filling with Red")
        
class Blue(Color):
    def fill(self):
        print("Filling with Blue")

class AbstractFactory:
    def create_shape(self):
        pass 
    def create_color(self):
        pass
    
class ColorShapeFactory(AbstractFactory):
    def create_shape(self,shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
    
    def create_color(self,color_type):
        if color_type == 'red':
            return Red()
        elif color_type == 'blue':
            return Blue()
      
def main():
    factory = ColorShapeFactory()
    shape = factory.create_shape('circle')
    shape.draw()
    colr = factory.create_color('red')
    colr.fill()
        
if __name__ == '__main__':
    main()
        