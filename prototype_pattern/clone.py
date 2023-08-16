import copy  
class A:
    def __init__(self):
        self.x  = 18
        self.msg = 'hello'
        
    def __str__(self):
        return f"{self.x}  and {self.msg}"
class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 34
        
    def __str__(self):
        return f"{self.x} and {self.y} and {self.msg}"
    
    

def main():
    b = B()
    c = copy.deepcopy(b)
    print([str(i) for i in (b,c)])
    print([i for i in (b,c)])
    
if __name__ == "__main__":
    main()