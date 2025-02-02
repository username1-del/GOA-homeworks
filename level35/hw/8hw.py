from turtle import *

#      8) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიღხვს შემდეგ კი დაბეჭდავს დადებითია თუ უარყოფითი
def num():
    num1 = (int(input("sheiyvane ricxvi: ")))
    if num1 < 0:
        print("es ricxvi uaryofiti")
    else:
        print("es ricxvi dadebiti")

num()