# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


a = int(input("Введите общее количество сделанных поделок : "))

b =int( a/3 * 2) 
c= int(b/4)

print("Катя сделала" ,b, "поделок")
print("Петя сделал" ,c, "поделок")
print("Сережа сделала",c ,"поделок")
