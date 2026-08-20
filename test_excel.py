from openpyxl import Workbook
import os
excel_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "student_prediction_data.xlsx"
)
workbook = Workbook()
sheet = workbook.active
sheet.title = "Student Data"
sheet.append([
    "Student ID",
    "Student Name",
    "Attendance",
    "Study Hours",
    "Internal Marks",
    "Assignment",
    "Previous Score"
])
sheet.append([
    101,
    "Sherin",
    90,
    6,
    85,
    90,
    88
])
workbook.save(excel_file)
print("EXCEL SAVED SUCCESSFULLY")
print("Location:")
print(excel_file)