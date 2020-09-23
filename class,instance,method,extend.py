class Car():
    def __init__(self,*args,**kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color","jdlf;ka")
        self.price = kwargs.get("price","dkjf;l;")
           
    def __str__(self):
        return f"Car with {self.wheels}"
    

  
    
  
class Convertible(Car):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time",10)
        
    def take_off(self):
        return "taking off"
               
    def __str__(self):
        return "Car with no roof"
    
    
  
porche = Convertible(color = "green", price = "$20")
mini = Convertible()
print(porche.color)
print(mini.take_off())
