class Employee:

    def __init__(self, id, name, salary, raise_in_salary):
        self.id = id
        self.name = name
        self.salary = salary
        self.raise_in_salary = raise_in_salary

    def display(self):
        print("Id: ", self.id) 
        print("Name: ", self.name) 
        print("Salary: ", self.salary)

    def increment_salary(self):
        self.salary = self.salary * self.raise_in_salary    

class Manager(Employee):

    def __init__(self, id, name, salary, raise_in_salary, cabin_id):
        Employee.__init__(self, id, name, salary, raise_in_salary)
        self.cabin_id = cabin_id

    def display(self):
        Employee.display(self)
        print("Cabin Id: ", self.cabin_id)

class Developer(Employee):

    def __init__(self, id, name, salary, raise_in_salary, desk_id):
        Employee.__init__(self, id, name, salary, raise_in_salary)
        self.desk_id = desk_id

    def display(self):
        Employee.display(self)
        print("Desk id: ",self.desk_id)       

class Tester(Employee):

    def __init__(self, id, name, salary, raise_in_salary, tester_id):
        Employee.__init__(self, id, name, salary, raise_in_salary)
        self.tester_id = tester_id

    def display(self):
        Employee.display(self)
        print("Tester id:", self.tester_id)    

class Company:

    def __init__(self, id, name, employees):
        self.id = id
        self.name = name
        self.employees = employees

    def display(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Employee count:", len(self.employees))


    def show_employee_list(self):
        for emp in self.employees:
            emp.display()    

    def hire(self, emp):
        self.employees.append(emp)
        print("Employee added: ")

    def fire(self, emp):
        self.employees.remove(emp)
        print("Employee fired:")

    def get_employee(self, id):
        for emp in self.employees:
            if emp.id == id: 
                return emp
        return None           

    def increment(self):
        for emp in self.employees:
            emp.increment_salary()
            print("Salary incremented:")    

m1 = Manager(1, "ABC", 10000, 1.3, 101)
#m1.display()        

d1 = Developer(2, "XYZ", 7000, 1.2, 110)
#d1.display()

d2 = Developer(3, "LMN", 8000, 1.1, 120)
d2.display()

c1 = Company(123, "PQR", [m1, d1])
c1.display()

c1.hire(d2)
c1.show_employee_list()

emp = c1.get_employee(2)
if emp != None:
    c1.fire(emp)

else:
    print("Employee not found")    

c1.show_employee_list()
t1 = Tester(9, "UVW", 5000, 0.8, 666)
c1.hire(t1)
c1.show_employee_list()
c1.increment()
c1.show_employee_list()