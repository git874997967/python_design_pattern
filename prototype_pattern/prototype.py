import copy  
from collections import OrderedDict
class Book:
    def __init__(self,name,author,price,**rest):
        self.name = name
        self.author = author
        self.price = price 
        self.__dict__.update(rest)
        
    
    def __str__(self):
       
        ordered = OrderedDict(sorted(self.__dict__.items()))
        return ''.join(
                [
                    f'{i}: {ordered[i]}\n' 
                    if i != 'price' 
                    else f'{i}:${ordered[i]}\n' 
                   for i in ordered.keys()
                ]
            )
    
class Prototype:
    def __init__(self):
        self.objects = dict()
        
    def register(self,identifier,obj):
        self.objects[identifier] = obj 
        
    def unregister(self,identifier):
        del self.objects[identifier]
        
    def clone(self, identifier,**attr):
        
        found = self.objects.get(identifier)
        if not found:
            raise KeyError(f"{identifier} is not found, please search again")
        else:
            obj = copy.deepcopy(found)
            obj.__dict__.update(attr)
        return obj
            
def main():
    b1 = Book('Boo1',"author1",price = 116,length = 116,publication_date = '2020-01-01')
    prototype = Prototype()
    cid = 'K&r-first'
    prototype.register(cid,b1)
    b2 = prototype.clone(cid,name = "b2",price = 200, length = 300, width = 100)
    print(b1,"-----")
    print(b2,"-----------")
    print(f"b1:{id(b1)} != b2:{id(b2)}")
if __name__ == "__main__":
    main()