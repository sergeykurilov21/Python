c = int(input("Введите номер билетика : "))
a = c % 1000 
i = int(a / 100)
b = c % 10 
d = int (c % 100 / 10 )
y = int(c / 1000 )
g =  int (y / 100 )
f = y % 10
k = int(y % 100 / 10)
sum_First = i + b + d
sum_Second = g + f + k

if (sum_First == sum_Second):
    print("yes")
else:
    print("no")