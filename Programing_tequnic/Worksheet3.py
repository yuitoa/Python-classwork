School = ["AAAA", "BBBB","CCCC","DDDD"]	
Medal = [4,7,1,3]
i = int(input("school_number"))
if 0 < i <= 4:
    Medal[i - 1] = int(input("new_result"))
    print(i, School[i - 1], Medal[i - 1])
elif i == -1:
	for a, (x, y) in enumerate(zip(School, Medal)):
         print(a + 1, x, y)
else:
	print("Error")

	