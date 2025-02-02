from turtle import *
#     11) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა ლუწ რიცხვს
def num():
    
    num1 = int(input("chawere ricxvi: "))
    for i in range(2, num1 + 1, 2):
        print(i)

num()