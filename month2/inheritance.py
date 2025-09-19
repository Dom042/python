class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname + " " + self.lastname)



me = Person("majesty", "chibuike")
me.printname()
class Student(Person):
    pass


santus = Student("Santus", "Cisco")
santus.printname()
santus.printname()


