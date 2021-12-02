Exam = int(input('Enter the number'))
Attendance = int(input('Enter the number'))
if Exam > 90 and Attendance > 90 :
    print('Grade = A')
elif Exam > 80 and Exam <= 90 and Attendance > 90:
    print('Grade = B')
elif Exam > 70 and Exam <= 80 and Attendance > 90:
    print('Grade = C')
else:
    print('Fail')
