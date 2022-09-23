print("Student Grading Program \n")
input("Student Name \t")
input("Student SCID \t")
A = int(input("Enter your percentage on Assignment Component of Grade Evaluation \t"))
L = int(input("Enter your percentage on Lab Component of Grade Evaluation \t"))
R = int(input("Enter your percentage on Reading Component of Grade Evaluation \t"))
Q = int(input("Enter your percentage on Quizzes Component of Grade Evaluation \t"))
M = int(input("Enter your percentage on Midterm Component of Grade Evaluation \t"))
P = int(input("Enter your percentage on Project Component of Grade Evaluation \t"))
print("Total is" ,A+L+R+Q+M+P)
if A+L+R+Q+M+P >= 94:
    print("Letter grade A")
    print("Grade points 4.00")
    print("Excellent performance")
elif A+L+R+Q+M+P >90:
    print("Letter grade A-")
    print("Grade points 3.667")
    print("Excellent performance")
elif A+L+R+Q+M+P >87:
    print("Letter grade B+")
    print("Grade points 3.333")
    print("Good performance")
elif A+L+R+Q+M+P >84:
    print("Letter grade B")
    print("Grade points 3.000")
    print("Good performance")
elif A+L+R+Q+M+P >80:
    print("Letter grade B-")
    print("Grade points 2.667")
    print("Good performance")
elif A+L+R+Q+M+P >77:
    print("Letter grade C+")
    print("Grade points 2.333")
    print("Average performance")
elif A+L+R+Q+M+P >74:
    print("Letter grade C")
    print("Grade points 2.000")
    print("Average performance")
elif A+L+R+Q+M+P >70:
    print("Letter garde C-")
    print("Grade points 1.667")
    print("Average performance")
elif A+L+R+Q+M+P >65:
    print("Letter grade D+")
    print("Grade points 1.333")
    print("Unsatisfactory performance")
elif A+L+R+Q+M+P >60:
    print("Letter grade D")
    print("Grade points 1.000")
    print("Unsatisfactory performance")
elif A+L+R+Q+M+P >55:
    print("Letter grade D-")
    print("Grade points 0.667")
    print("Unsatisfactory performance")
elif A+L+R+Q+M+P <54.99:
    print("Letter grade F")
    print("Grade points 0.000")
    print("Failing performance")











