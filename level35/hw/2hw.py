from turtle import *
#  2) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება სახელს შემდეგ კი მას მიესალმება
def hello_user():
    ask_name=(input("whats your name: "))
    print("hello " + ask_name)
hello_user()