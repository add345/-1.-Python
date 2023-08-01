    #Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
    # Дано a, b, c - стороны предполагаемого треугольника.
    # Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
    # Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
    # Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
    
a = float(input("Введите сторону a: ")) 
b = float(input("Введите сторону b: ")) 
c = float(input("Введите сторону c: ")) 

if a < b+c and b < a+c and c < a+b: 
    print("Треугольник существует") 
else: 
    print("Треугольник не существует")
    

a = float(input("Введите сторону a: ")) 
b = float(input("Введите сторону b: ")) 
c = float(input("Введите сторону c: ")) 
 
if a == b and b == c: 
     print("Равносторонний треугольник") 
elif a == b or b == c  or c == a:
     print("Равнобедренный треугольник")