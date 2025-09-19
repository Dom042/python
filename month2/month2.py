#Constructor - name and breed
#Method bark - print "Woof! Woof!"

class Dog:
    def __init__(self, name, breed):
        self.name = name   # store the dog's name
        self.breed = breed # store the dog's breed

    # Example method - bark
    def bark(self):
        print("Woof! Woof!")

    # Method to print the dog's name
    def print_name(self):
        print("The dog's name is:", self.name)


# Example usage
my_dog = Dog("Buddy", "German Shepherd")
my_dog = Dog("Dominic", "German")
my_dog.bark()         # prints Woof! Woof!
my_dog.print_name()   # prints The dog's name is: Buddy











class Human:
    """
    Human class with attributes for senses and height.
    Attributes:
      - nose: description / sensitivity for smell
      - tongue: description / sensitivity for taste
      - eyes: description / visual acuity for sight
      - skin: description / sensitivity for touch
      - limb: description / mobility (arms/legs) used for movement
      - height: numeric (cm)
    """

    def __init__(self, name: str,
                 nose: str = "normal",
                 tongue: str = "normal",
                 eyes: str = "normal",
                 skin: str = "normal",
                 limb: str = "able",
                 height: float = 170.0):
        self.name = name
        self.nose = nose
        self.tongue = tongue
        self.eyes = eyes
        self.skin = skin
        self.limb = limb
        self.height = float(height)

    def smell(self, thing: str) -> str:
        """Simulate smelling something."""
        return f"{self.name} smells the {thing} with {self.nose} smell sensitivity."

    def taste(self, food: str) -> str:
        """Simulate tasting something."""
        return f"{self.name} tastes the {food} with {self.tongue} taste sensitivity."

    def see(self, obj: str) -> str:
        """Simulate seeing an object."""
        return f"{self.name} sees the {obj} with {self.eyes} vision."

    def touch(self, surface: str) -> str:
        """Simulate touching a surface."""
        return f"{self.name} touches the {surface} with {self.skin} touch sensitivity."

    def move(self, action: str) -> str:
        """Simulate movement using limbs (walk, run, grab...)."""
        return f"{self.name} uses their {self.limb} to {action}."

    def info(self) -> str:
        """Summary of the human's attributes."""
        return (f"{self.name}: height={self.height} cm, nose={self.nose}, "
                f"tongue={self.tongue}, eyes={self.eyes}, skin={self.skin}, limb={self.limb}")

    def __repr__(self):
        return f"Human(name={self.name!r}, height={self.height})"


# Example usage
if __name__ == "__main__":
    alice = Human(name="Alice",
                  nose="keen",
                  tongue="sensitive",
                  eyes="sharp",
                  skin="soft",
                  limb="agile",
                  height=165)

    print(alice.info())
    print(alice.smell("rose"))
    print(alice.taste("lemon"))
    print(alice.see("sunset"))
    print(alice.touch("silk"))
    print(alice.move("run"))



class Human:
    def __init__(self, name, eyes, ears, nose, tongue, skin, limbs, skintone, height):
        self.name = name
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.tongue = tongue
        self.skin = skin
        self.limbs = limbs
        self.skintone = skintone
        self.height = height
































        
