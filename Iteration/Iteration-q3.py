total = 0
total_old = 0
partno = ''
while partno != '9999':
    partno = str(input("Enter partno:"))
    if len(partno) == 4:
        if partno[3] == '6' or partno[3] == '7' or partno[3] == '8':
            total_old = total_old + 1
        else:
            total = total + 1
    else:
         print("Error:enter again")
        #endif
    #endif
else:
    print(total-1,total_old)
#end while



     
