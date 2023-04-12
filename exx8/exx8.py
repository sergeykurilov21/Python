n = int(input("Input number first : "))
m = int(input("Input number second : "))
k = int(input("Input number third : "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Yes")
else:
    print("No")