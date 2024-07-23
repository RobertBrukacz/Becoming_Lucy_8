class Menu:
    def __init__(self, name):
        self.name = name

    def create(self):
        return self.name

class Mainmenu(Menu):
    def __init__(self, name, breed):
        super().__init__(name)  # Aufruf der __init__-Methode der Basisklasse
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

class Startgame(Menu):
    def __init__(self, name, color):
        super().__init__(name)  # Aufruf der __init__-Methode der Basisklasse
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

class RobotDog(Mainmenu):
    def __init__(self, name, breed, model):
        super().__init__(name, breed)  # Aufruf der __init__-Methode der Basisklasse Dog
        self.model = model

    def speak(self):
        # Aufruf der speak-Methode der Klasse Dog und Erweiterung der Funktionalität
        original_sound = super().speak()
        return f"{original_sound} (Robot model {self.model})"

# Instanziierung und Verwendung der Klassen
mainmenu = Menu("Generic Animal")
dog = Mainmenu("Buddy", "Golden Retriever")
cat = Startgame("Whiskers", "Black")
robot_dog = RobotDog("RoboBuddy", "RoboBreed", "RX100")

print(mainmenu.create())      # Ausgabe: Some generic sound
print(dog.speak())         # Ausgabe: Buddy says Woof!
print(cat.speak())         # Ausgabe: Whiskers says Meow!
print(robot_dog.speak())   # Ausgabe: RoboBuddy says Woof! (Robot model RX100)
