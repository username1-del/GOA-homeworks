from turtle import *
#     10) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა რიცხვს

def num():
    n = 1
    num1 = int(input("sheiyvane ricxvi: "))
    while n != num1:
        print(n)
        n += 1

num()