#Дано пятизначное целое число.Напишите алгоритм,который возведёт количество десятков в степень количества единиц.
#Затем умножит это число на количество сотен.И делит получившееся число на разность количества десятков тысяч и количества тысяч
#Например,есть число 46275 Необходимо возвести 7(десятки) в степень5(единицы),умножить получившееся число на 2(сотни),
#и разделить наразность между 4(десятки тысяч) и 6(тысячи) то есть(4-6)
#В результате необходимо получить вещественное число.В нашем примере это будет:-16807.




a=int(input("Введите пятизначное число:  ")) #введите пятизначное целое число
b=a%10 #получим остаток количество единиц (остаток)
c=(a//10)%10 #получим количество десятков (остаток)
d=c**b #возедем количество десятков в степень количества единиц
e=(a//100)%10 #получим количество сотен (остаток)
u=(d*e) #умножаем на количество сотен
n=(a//1000)%10 #получим количество тысяч (остаток)
m=(a//10000)%10 #получим количество десятков тысяч (остаток)
k=m-n #разница между кол-вом десятков тысяч и кол-вом тысяч
r=float(u/k)
print(r)
