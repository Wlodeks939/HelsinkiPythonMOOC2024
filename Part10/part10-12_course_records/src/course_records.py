class Course:
    def __init__(self,name,grade:int,credits:int):
        self.name_course = name
        self.grade_course = grade
        self.credits_course = credits

class CourseBook:
    def __init__(self):
        self.courses = {}  

    def add_course(self,course:Course):

        if not course.name_course in self.courses:
            self.courses[course.name_course] = [course.grade_course,course.credits_course]

    def all_entries(self):
        return self.courses        # {'mate': [10, 5], 'programacion': [8, 6]} 


class App:
    def __init__(self):
        self.courses = CourseBook()

    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course_name = input("course: ")
        course_grade = int(input("grade: "))
        course_credits = int(input("credits: "))

        if course_name in self.courses.all_entries() and course_grade > self.courses.all_entries()[course_name][0]:

            self.courses.all_entries()[course_name][0] = course_grade #actualiza grade

        elif not course_name in self.courses.all_entries():

            course = Course(course_name,course_grade,course_credits)
            self.courses.add_course(course) 

         

    def course_data(self):
        course_name = input("course: ")
        if course_name in self.courses.all_entries():
            return f"{course_name} ({self.courses.all_entries()[course_name][1]} cr) grade {self.courses.all_entries()[course_name][0]}"
        else:
            return "no entry for this course"  

    def statistics(self):
        
        dic = self.courses.all_entries()

        count = 0
        total_credits = 0
        mean = 0
        grade_1 = 0
        grade_2 = 0
        grade_3 = 0
        grade_4 = 0
        grade_5 = 0
        
        for key,value in dic.items():
            count += 1
            total_credits += value[1]
            mean += value[0]
            if value[0] == 1:
                grade_1 += 1
            elif value[0] == 2:
                grade_2 += 1
            elif value[0] == 3:
                grade_3 += 1
            elif value[0] == 4:
                grade_4 += 1
            elif value[0] == 5:
                grade_5 += 1            

        if count != 0:

            mean = mean/count    

        print(f"{count} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        print("5:","x"*grade_5)
        print("4:","x"*grade_4)
        print("3:","x"*grade_3)
        print("2:","x"*grade_2)
        print("1:","x"*grade_1)

        return

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()

            elif command == "2":
                print(self.course_data())

            elif command == "3":
                self.statistics()
         
            else:
                self.help()    


app = App()       
app.execute()         


"""
a = Course("mate",10,5)
b = Course("programacion",8,6)

courseBook = CourseBook()
courseBook.add_course(a)
courseBook.add_course(b)

print(courseBook.all_entries())

{'mate': [10, 5], 'programacion': [8, 6]}

"""