from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits_helper(credits_sum, course):
  return credits_sum + course.credits


def sum_of_all_credits(attempts: list):

    return reduce(sum_of_all_credits_helper,attempts,0)


def sum_of_passed_credits(attempts: list):


    lista1 = list(filter(lambda t: t.grade >= 1, attempts))

    return reduce(sum_of_all_credits_helper,lista1,0)



def sum_of_all_grade_helper(grade_sum, course):
  return grade_sum + course.grade

def average(attempts: list):

    lista1 = list(filter(lambda t: t.grade >= 1, attempts))

    suma = reduce(sum_of_all_grade_helper,lista1,0)

    return suma/len(lista1)





if __name__ == "__main__":

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)