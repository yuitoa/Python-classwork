maxAge = 0
AgeList = input()
array AgeList[4]
for index = 0 to 3
AgeList[index] = input ()
	if AgeList[index] > maxAge: #then
		maxAge = AgeList[index]
		position = index
	#endif
#next index
        print(AgeList[position], position)
