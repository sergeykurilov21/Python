#Найдите сумму цифр трехзначного числа.


c = int(input("Введите целочисленное число 3-х значное :" ))
b=int(c/100)
print(b)
d=int(c%100/10)
print(d)
a = c%10
print(a)

print("Сумма чисел равна :" ,a+b+d)