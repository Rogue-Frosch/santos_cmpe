
student1_name = "Diego"
Student1_grade = 1.5
Student1_subject = ["Algebra", "Physiscs"]

student2_name = "Jhon"
Student2_grade = 1.0
Student2_subject = ["Biology", "Physiscs"]

student3_name = "Mark"
Student3_grade = 2.5
Student3_subject = ["Calculus", "Chemistry"]

def print_student_info_function(name, grade, course):
    print(f"{name} grade{grade} course{course}")

if __name__ == "__main__":
    print_student_info(student1_name, Student1_grade, Student1_subject)
    print_student_info(student2_name, Student2_grade, Student2_subject)
    print_student_info(student3_name, Student3_grade, Student3_subject)


class Student:
    DEFAULT_SUBJECT = ["Algebra", "Physiscs"]

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info_method(self):
        print(f"{self.name} grade{self.grade} course{self.subject}")

    @classmethod
    def create_default_student(cls, name, grade):
        print(f"{name}, grade: {grade}, course: {cls.DEFAULT_SUBJECT}")
        return cls(name, grade, cls.DEFAULT_SUBJECT)

    @staticmethod
    def is_grade_passing(grade):
        return grade <= 3.0



if __name__ == "__main__":
    student1 = Student("Unique", 1.5, ["Biology", "Chemistry"])
    student1.print_student_info_method()
    if Student.is_grade_passing(student1.grade):
        print("pass")
    else:
        print("failed")

    student2 = Student("Zild", 3.5, ["Electronics", "Chemistry"])
    student2.print_student_info_method()
    if Student.is_grade_passing(student2.grade):
        print("pass")
    else:
        print("failed")

    student3 = Student("Blaster", 2.5, ["Physics", "Calculus"])
    student3.print_student_info_method()
    if Student.is_grade_passing(student3.grade):
        print("pass")
    else:
        print("failed")

    student4 = Student("Badjao", 2.75, subject=Student.DEFAULT_SUBJECT)
    student4.print_student_info_method()
    if Student.is_grade_passing(student4.grade):
        print("pass")
    else:
        print("failed")