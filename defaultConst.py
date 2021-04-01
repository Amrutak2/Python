class Const():

    def __init__(self, a="None"):
        self.a = ""
        self.b = "xyz"

    def print_cls(self):
        print("My class:", self.a)
        print("My class:", self.b)

obj1 = Const()
obj1.print_cls()        
