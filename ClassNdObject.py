class MyClass():
    name = ""
    rno = ""

    def display(self):
        print("Name:", self.name)
        print("Roll number:",self.rno)

p1 = MyClass()
p1.name = "A"
p1.rno = 1
p1.display()

p1.name = "B"
p1.rno = 2
p1.display()