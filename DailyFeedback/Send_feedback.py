import random
from Data import *
def map_grade(grade):
    grades = {
        'a': 'Good',
        'b': 'Average',
        'c': 'Not good'
    }
    return grades.get(grade.lower(), 'Unknown')

def generate_feedback(attend, atti, focus, effort, s_name):
    attendanceF = random.choice(attendance_feedback[attend])
    attitudeF = random.choice(Attitude[atti])
    focusF = random.choice(Focusing[focus])
    effortF = random.choice(Effort[effort])


    print("-", attendanceF.format(s_name))
    print("-", attitudeF.format(s_name))
    print("-", focusF.format(s_name))
    print("-", effortF.format(s_name))
    advice = input("Lời khuyên: ")

def generate_feedback_for_class():
    student_number = int(input("Số lượng học sinh: "))
    class_name = input("Class(PTS, TP, ZTH, ROBOTIC, ME, TDE): ")
    time = input("Time: ")
    lesson = input("Bài học: ")
    print(class_name, time)
    for i in range(student_number):
        student_name = input("\nTên học sinh: ")
        attendanceR = input("Attendance(A|good|, B|average|, C|not good|): ")
        attitudeR = input("Attitude(A|good|, B|average|, C|not good|): ")
        focusingR = input("Focus(A|good|, B|average|, C|not good|): ")
        effortR = input("Effort(A|good|, B|average|, C|not good|): ")
        attendance_grade = map_grade(attendanceR)
        attitude_grade = map_grade(attitudeR)
        focusing_grade = map_grade(focusingR)
        effort_grade = map_grade(effortR)
        print("\nStudent: ", student_name)
        print("Bài học: ", lesson)
        generate_feedback(attendance_grade, attitude_grade, focusing_grade, effort_grade, student_name)

generate_feedback_for_class()