class Car:
    def __init__(self,color,make,model,registration):
        self.color=color
        self.make=make
        self.model=model
        self.registration=registration
        
    def hoot(self):
        print(f"Hooot....Hooot!!!!")
    def start(self):
        print(f"I am {self.color},{self.make},{self.model} model,my plate is {self.registration}")
