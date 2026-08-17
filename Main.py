def get_student_data():
    name=input("enter the name:")
    attendence=float(input("Enter attendence(%):"))
    internal_marks=float(input("Enter marks(%):"))
    study_hours=float(input("Enter hours(%):"))
    assignment_completion=float(input("Enter assignment marks(%):"))
    return name,attendence,internal_marks,study_hours,assignment_completion
def calculate_average(attendence,internal_marks,study_hours,assignment_completion):
    average=(attendence+internal_marks+study_hours+assignment_completion)/4
    return average
def calculate_performance(attendence,internal_marks,study_hours,assignment_completion):
    performance_score=attendence*0.20+internal_marks*0.40+study_hours*0.20+assignment_completion*0.20
    return performance_score
def calculate_study_hours_score(study_hours):
    if study_hours>=5:
        return 100
    elif study_hours>=3:
        return 50
    else:
        return 25
def performance_level(score):
    if score>=90:
        return "Good"
    elif score>=60:
        return "Average"
    else:
        return "Poor"
def get_recommendation(level):
    if level=="Good":
        return "Keep it up!Great Work"
    elif level=="Average":
        return "Continue regular class and improve study hours"
    else:
        return "Do hard work,need more improvement"
def display_result(name,average,performance_score,level,recommendation):
    print("Student name:",name)
    print("Average score:",round(average,2))
    print("Performance score:",round(performance_score,2))
    print("Performance level:",level)
    print("Recommendation:",recommendation)
def main():
    name,attendence,internal_marks,study_hours,assignment_completion=(get_student_data())
    study_hours_score=calculate_study_hours_score(study_hours)
    average=calculate_average(attendence,internal_marks,study_hours,assignment_completion)
    performance_score=calculate_performance(attendence,internal_marks,study_hours_score,assignment_completion)
    level=performance_level(performance_score)
    recommendation=get_recommendation(level)
    display_result(name,average,performance_score,level,recommendation)
if __name__== "__main__":
    main()
