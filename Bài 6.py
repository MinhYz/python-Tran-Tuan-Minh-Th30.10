import math
a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
c=float(input("Nhap c:"))
delta=b*b-4*a*c
#B1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
#B2=(-b-math.sqrt(delta))/(2*a)
if delta<0:
    print("Bieu thuc khong co gia tri")
elif delta==0:
    B=-b/(2*a)
    print("B=",B)
else:
    B1=(-b+math.sqrt(delta))/(2*a)
    B2=(-b-math.sqrt(delta))/(2*a)
    print("B1=",B1)
    print("B2=",B2)
