# Write your solution here


count = 0
exam_points_sum = 0
exam_points_avg = 0
fail_count = 0
total_points_sum = 0

grade_0 = 0
grade_1 = 0
grade_2 = 0
grade_3 = 0
grade_4 = 0
grade_5 = 0

while True:

    
    entrada = input("Exam points and exercises completed:")
    if entrada == "":
        break

    # divide la entrada y tansforma a enteros    
    count += 1
    exam_points, exercises_completed = entrada.split(" ")    

    exam_points = int(exam_points)
    exercises_completed = int(exercises_completed)

  
    

    #exercise points

    exercice_points = int (exercises_completed // 10)

    # total points

    total_points = exam_points + exercice_points

    # calcula la suma de puntos para calcular el promedio despues

    total_points_sum += total_points



    # Pass percentage

    if total_points < 15 or exam_points < 10:
        fail_count += 1

    


    # Grade distribution

    if 0 <= total_points <= 14 or exam_points < 10:
        grade_0 += 1
    elif 15 <= total_points <= 17:
        grade_1 += 1    
    elif 18 <= total_points <= 20:
        grade_2 += 1  
    elif 21 <= total_points <= 23:
        grade_3 += 1
    elif 24 <= total_points <= 27:
        grade_4 += 1
    elif 28 <= total_points <= 30:
        grade_5 += 1                              


total_points_avg = float(total_points_sum / count)

# pass percentage
        
pass_count = count - fail_count
pass_percen = float(pass_count/count*100)  



print("Statistics:")
print(f"Points average: {total_points_avg:.1f}")
print(f"Pass percentage: {pass_percen:.1f}")
print("Grade distribution:")
print("  5:" + " " + "*" * grade_5)
print("  4:" + " " + "*" * grade_4)
print("  3:" + " " + "*" * grade_3)
print("  2:" + " " + "*" * grade_2)
print("  1:" + " " + "*" * grade_1)
print("  0:" + " " + "*" * grade_0)

#20 100
#10 10
#9 100
#15 75
#18 40