from typing import Counter

class_data = [[23,43,56],
              [34,56,45],
              [45,56,78]]

total1 = 0
total2 = 0
total3 = 0
for row in class_data:
    total1 = total1 + row[0]
    total2 = total2 + row[1]
    total3 = total3 + row[2]
#next row
print('avarage1',total1/3)
print('avarage2',total2/3)
print('avarage3',total3/3)
print('all_avarage',(total1 + total2 + total3)/9)

