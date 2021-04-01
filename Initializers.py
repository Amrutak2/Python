class MyClass():
    def __init__(self, obj):
        self.a = obj.a
        self.b = obj.b

    def display(self):
        print('value of a:',self.a)
        print('value of b:',self.b)

obj1 = MyClass()
obj1.a = 30
obj1.b = 100
obj1.display()

obj2 = MyClass(obj1)
obj2.display()