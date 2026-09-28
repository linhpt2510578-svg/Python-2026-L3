students = []
courses = {}
mark = {}

def input_students():
    count_student = int(input("Enter the number of students in a class:"))
    return count_student

def student_information(count_student):
    for i in range(count_student):
        print("Student number", i + 1)

        student_id = int(input("Enter student ID:"))
        name = input("Enter student name:")
        dob = input("Enter date of birth:")

        student = (student_id, name, dob)
        students.append(student)
count_student = input_students()
student_information(count_student)
print(students)

def input_courses():
    count_course = int(input("Enter number of courses:"))

    for i in range (count_course):
        print("Course number:", i + 1)

        course_id = (input("Enter course ID:"))
        course_name = input("Enter course's name:")

        courses[course_id] = course_name
    return courses

courses = input_courses()
print("Course list: ", courses)  

def marks(courses, students, mark):

    ID_selected = (input("Enter the course ID to input marks for: "))

    found = False
    for i in courses:
        if i == ID_selected:
            found = True
            break

    if not found:
        print("The course not found")
        return
    if ID_selected not in mark:
        mark[ID_selected] ={}

    for s in students:
        score = float(input(f"Enter the mark for {s[1]}: "))
        mark[ID_selected][s[0]] = score




while True:
    print("--------------MENU---------------")
    print("1. INPUT THE MARK FOR EACH COURSE")
    print("2. SHOW LIST STUDENTS")
    print("3. SHOW LIST COURSES")
    print("4. SHOW STUDENT MARKS FOR COURSE")
    print("5. EXIT")

    selected = int(input("Enter your select:"))

    match selected:
        case 1:
            marks(courses, students, mark)
            
        case 2:
            print("Students: ", students)

        case 3:
            print("Courses: ", courses)
        case 4:
            print("The marks: ", mark)
        case 5:
            break
        case _:
            print("NOT EXIST")








