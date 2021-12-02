total = 0
total_old = 0
partno = ''
while partno != '9999':
    partno = len(input("Enter partno:"))
    while int(partno) != 4:
        partno = input("Error:enter again")
    #end while
        total = total + 1
        if partno[3] == '6' or partno[3] == '7':
            total_old = total_old + 1
        #end if
#end while
print(total,total_old)



     
