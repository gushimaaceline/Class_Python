class Dog:
    def __init__(self,name,breed,color):
        self.name=name
        self.breed=breed
        self.color=color
        

    def bark(self):
        print(f"{self.name},is {self.breed}")

    def bite(self):
        print(f"Most {self.breed} have {self.color} as color")