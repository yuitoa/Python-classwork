from typing import Counter

Outlet1Sales = [10,12,15,10]
Outlet2Sales = [5,8,3,6]
Outlet3Sales = [10,12,15,10]

for count in range(0,4):
    TotalSales = Outlet1Sales[count] + Outlet2Sales[count] + Outlet3Sales[count]
    print('Total for quarter',count+1,TotalSales)