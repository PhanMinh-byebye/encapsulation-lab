class Mammal:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
        self.kingdom = "animal"
    def make_sound(self):
        return f"{self.name} is of make sound {self.sound}"
    def get_kingdom(self):
        return self.kingdom 
    def info(self):
        return f"{self.name} is of type {self.type}"
mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
