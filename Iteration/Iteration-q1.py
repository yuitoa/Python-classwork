x = int(input ("Enter the first integer: "))
y = int(input ("Enter the second integer: "))
z = 0
while x > 0:
    if x % 2 == 1 :
        z = z + y
    #endif
    x = x / 2
    y = y * 2
#endwhile
print ("Answer =", z)