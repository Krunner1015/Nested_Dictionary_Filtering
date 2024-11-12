import course_data

#gets the inputted student to show the grades of
student = input("Enter the student's name: ")

#runs only if the student's name is in the roster
if student in course_data.actual_data["roster"]:
    total_grade = 0

    #iterate through and print each assignment and the grade the student received for that assignment
    for assignment in course_data.actual_data["assignments"]:
        grade = 0

        #checks that the student has a grade for each assignment
        if student in course_data.actual_data["assignments"][assignment]["submissions"]:
            grade = course_data.actual_data["assignments"][assignment]["submissions"][student]
            print(f"{assignment}: {grade}%")
        else:
            print(f"{assignment}: 0%")

        # calculates the students total grade
        total_grade += ((grade / 100) * course_data.actual_data["assignments"][assignment]["weight"])

    print(f"Total grade: {total_grade:.1f}%")

#prints message if an invalid student name is inputted
else:
    print("Student not found.")