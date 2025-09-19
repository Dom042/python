class Human:
    def __init__(self, eyes, hair_color, legs, gender, height):
        self.eyes = eyes
        self.hair_color = hair_color
        self.legs = legs
        self.gender = gender
        self.height = height

    def walking(self):
        print("I am walking")

    def speaking(self):
        print("I am talking")

    def breathing(self):
        print("I am breathing")


# Example usage:
person1 = Human(2, "black", 2, "Male", "5.9ft")
print(f"Gender: {person1.gender}, Height: {person1.height}, Hair: {person1.hair_color}")

person1.walking()
person1.speaking()
person1.breathing()




class User:
    def __init__(self, firstname, lastname, age, sex, nationality, email, phone):
        self.name = firstname
        self.email = lastname
        self.age = age
        self.sex = sex
        self.nationality = nationality
        self.email = email
        self.phone = phone

        
