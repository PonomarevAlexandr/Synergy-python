#Пользователь вводит стороны прямоугольника,выведите его площадь и периметр.
#На вход программе могут подаваться как целые числа,так и вещественные
#Площадь прямоугольника равна произведению длины прямоугольника на его ширину.
#Периметр прямоугольника равен удвоенной сумме длин его ширины и длины.
#1) 3*4=12 (см2)-площадь прямоугольника 
#2) 3*2+4*2=14 (см)-периметр прямоугольника.

a=float(input("Введите длинну прямоугольника:"))
b=float(input("Введите ширину прямоугольника:")) 
print ("Площадь прямоугольника =",a*b)
print("Периметр прямоугольника =",(a+b)*2)