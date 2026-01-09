import newfunctionrunner

student1_name = "Zild"
student1_grade = 1.5
student1_course = ["Electronics", "Chemistry"]

newfunctionrunner.print_student_info_function(student1_name, student1_grade, student1_course)


student1 = newfunctionrunner.Student("Zild", 1.5, ["Electronics", "Chemistry"])
student1.print_student_info_method()