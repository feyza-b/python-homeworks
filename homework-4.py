print("Bu program polinom hesaplayıcıdır.")
print("ax^2 + bx + c şeklinde olan polinomların sonucunu hesaplar.")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

x = int(input("x: "))

print("Polinom: " + str(a) + "x^2 + " + str(b) + "x + " + str(c))

result= a * x**2 + b * x + c 


print("Result: " + str(result))

