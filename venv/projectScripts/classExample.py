class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def renderName(self):
    print("Hello my name is " + self.name)

  def renderAge(self):
    print("\nMy age is ", self.age)

p1 = Person("John", 36)
p1.renderName()
p1.age = 40
p1.renderAge()
del p1.age
p1.age = 50
p1.renderAge()
test = list()
test.append([0,1,1])
print("Test List", test)
