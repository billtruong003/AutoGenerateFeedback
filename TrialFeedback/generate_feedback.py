import random
from DataTrial import *

# Combine the feedback dictionaries into a single dictionary
Test_Feedback = {"Induct": Induct, "Diagram": Diagram, "Critic": Critic, "Deduct": Deduct}

def check_test():
    """Function to take user input for test values and return as a list."""
    print("Nhập điểm bài test tư duy (.../4)")
    inductive = int(input("Tư Duy Quy Nạp: "))
    diagrammatic = int(input("Tư Duy Sơ Đồ: "))
    critical = int(input("Tư Duy Phản Biện: "))
    deductive = int(input("Tư Duy Suy Diễn: "))
    attend = input("Thời gian tham dự (a: Good | b: Average): ")
    talent = input("Thiên phú với bộ môn (a: Good | b: Average): ")
    practice = input("Bài thực hành (a: Good | b: Average): ")
    return [inductive, diagrammatic, critical, deductive, attend, talent, practice]

def get_test_results(test_values):
    """Function to calculate the test feedback values and return as a tuple."""
    total = sum(test_values[:4])
    feedback_values = []
    for i, value in enumerate(test_values[:4]):
        result = "Good" if value >= 3 else "Average"
        feedback_values.append(random.choice(Test_Feedback[list(Test_Feedback.keys())[i]][result]))
    return tuple(feedback_values) + (total,)

def get_feedback_results(test_values):
    """Function to calculate the feedback values and return as a tuple."""
    attend = "Good" if test_values[4].lower() == "a" else "Average"
    talent = "Good" if test_values[5].lower() == "a" else "Average"
    practice = "Good" if test_values[6].lower() == "a" else "Average"
    return (random.choice(TrialClass_Feedback[attend]), 
            random.choice(TrialClass_Talent_Feedback[talent]), 
            random.choice(TrialClass_Project_Feedback[practice]))

def send_result():
    """Function to print the test and feedback results for a given student."""
    # Get the student's name as input
    student_name = input("Tên học sinh: ")
    subject = input("Bộ môn tham dự: ")
    course = input("Chương trình phù hợp: ")
    # Call the check_test() function to get a list of test values
    test_values = check_test()
    
    # Call the get_test_results() function to get the result strings
    feedback_values = get_test_results(test_values)
    
    # Call the get_feedback_results() function to get the feedback strings
    feedback_values += get_feedback_results(test_values)
    
    # Print the results for the student

    print("Kết quả cho học sinh: ", student_name)
    print("Chương trình phù hợp:", course)
    print("Bộ môn tham gia:", subject)
    print("=======================================")
    print("Tư duy quy nạp:", feedback_values[0])
    print("Tư duy sơ đồ:", feedback_values[1])
    print("Tư duy phản biện:", feedback_values[2])
    print("Tư duy suy diễn:", feedback_values[3])
    print("Tổng điểm:", feedback_values[4])
    print("Phản hồi về thời gian tham dự:", feedback_values[5])
    print("Phản hồi về thiên phú với bộ môn:", feedback_values[6])
    print("Phản hồi về bài thực hành:", feedback_values[7])
    advice = input("Khuyến khích: ")
    
send_result()