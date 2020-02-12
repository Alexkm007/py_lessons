class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Plannet:
    """Класс планета, работа с классами"""
    count = 0
    def __init__(self,name, population=None):
        self.name = name
        self.population = population or []
        Plannet.count += 1
    def __repr__(self):
         return f"Plannet {self.name}"
    def add_human(self,human):
        print(f"Welcom to {self.name}, {human.name}")
        self.population.append(human)


mars  = Plannet("Mars")
bob = Human("Bob")
mars.add_human(bob)

print(Plannet.count)
print(mars.__dict__)
print(mars.__doc__)
print(mars.__class__)