num1 = int(input("diga o primeiro numero: "))
num2 = int(input("diga o segundo numero: "))
while num1 == num2 :
    num2 = int(input("erro, diga o segundo numero:"))
if num1 < num2 :
    print (f" {num1} > {num2}")
else:
    print (f"{num2} > {num1}")