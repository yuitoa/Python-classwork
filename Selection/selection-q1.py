Grade1 = 80
Grade2 = 67
if (Grade1>=80) and (Grade2 >=80): #Then
   print("True")
else:
   print("False")
#end if 
Grade1 = 82
Grade2 = 80
if (Grade1>=80) or (Grade2>=80):
    print("True")
else:
    print("False")

Grade1 = 35
Grade2 = 50
if (Grade1>30) or (Grade1<50):
    print("True")
else:
    print("False")

Grade1 = 65
Grade2 = 0
if (Grade1<30) or (Grade1 >80):
    print("True")
else:
    print("False")

Grade1 = 0
Grade2 = 75
if not(Grade1>50) and (Grade2>50):
    print("True")
else:
    print("False")

Grade1 = 65
Grade2 = 85
if not(Grade1<80) and not (Grade2<80):
    print("True")
else:
    print("False")

