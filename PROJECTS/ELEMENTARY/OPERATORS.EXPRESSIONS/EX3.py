'''Într-o clasă sunt F fete și B băieți.
Fiecare fată citește 3 pagini pe zi și fiecare băiat citește 2 pagini pe zi.
 Câte pagini vor citi copiii în n zile?'''
f=int(input("Numarul de fete este: "))
b=int(input("Numarul de baieti este: "))
n=int(input("Numarul de zile este: "))
total_pagini=f*3*n+b*2*n
print("Totalul de pagini este:", total_pagini)