#Se dau trei numere naturale a b x. Să se verifice dacă numărul x aparține intervalului [a,b].
a=int(input("a: "))
b=int(input("b: "))
x=int(input("x: "))
if x>=a and x<=b:
    print(" Numarul x apartine intervalului[a,b] ")
else:
    print(" Numarul x NU apartine intervalului[a,b] ")