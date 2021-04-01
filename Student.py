class Student():

    def __init__(self, rno, name, marks):
        self.rno = rno
        self.name = name
        self.marks = marks

    def information(self):
        print("Roll no:",self.rno)
        print("Name:",self.name)
        print("Marks:",self.marks)


class College():
    
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def show_student_list(self):
        for stu in self.students:
            stu.information()

    def enroll_new_student(self, stu):
        self.students.append(stu)
        print("New student is Enrolled")        


s1 = Student(1, "A", 80) 
s2 = Student(2, "B", 50)
s3 = Student(3, "C", 70)
s4 = Student(4, "D", 75)

c1 = College("Abcd", [s1, s2, s3])
c1.show_student_list()
c1.enroll_new_student(s4)

c1.show_student_list()