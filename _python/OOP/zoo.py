class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self,animal):
        self.animals.append(animal)
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name,age):
        self.animals.append( Tiger(name,age) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
class animal:
    def __init__(self,name,age,health_level,happiness_level):
        self.name = name
        self.age= age
        self.health_level= health_level
        self.happiness_level = happiness_level
    def display_info(self):
        print(self.name,self.age,self.health_level,self.happiness_level)
    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
        return self
class Lion(animal):
    def __init__(self, name, age=10, health_level=30, happiness_level=40):
        super().__init__(name, age, health_level, happiness_level)

    def speak(self):
        print("Roar")
class Tiger(animal):
    def __init__(self, name, age, health_level=45, happiness_level=55):
        super().__init__(name, age, health_level, happiness_level)
        
class Bear(animal):
    def __init__(self, name, age, health_level= 35, happiness_level=20):
        super().__init__(name, age, health_level, happiness_level)

zoo1 = Zoo("John's Zoo")
Lion1 = Lion("Nala",15,35,65)
zoo1.add_animal(Lion1)
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah",16)
zoo1.add_tiger("Shere Khan",22)
zoo1.print_all_info()
Simba = Lion("Simba",22)
Simba.speak()
Simba.feed()
print(Simba.health_level)
