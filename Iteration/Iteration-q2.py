temp = 0
fever = 0
total = 0
hour = 0
while hour < 6 :
	hour = hour + 1
	temp = float(input("Enter temperature:"))
	if temp > 37:
		fever = fever + 1
	#endif
	total = total + temp
#endwhile
average = round(total/hour,1) #round to 1 decimal place
print("Average temperature:", average)
print("Incidents of fever:", fever)
