from turtle import *
#      6) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გაყოფს ერთმანეთზე 

def ask_number():
    num1=int(input("sheiyvane cifri N1: "))
    num2=int(input("sheiyvane cifri N2: "))
    print(num1 / num2) #// თუ დამრგვალება გვინდა (ზუსტი ჯამისთვის ერთი სლეშია საჭირო)

ask_number()