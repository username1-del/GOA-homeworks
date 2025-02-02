from turtle import *
#     12) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა კენტ რიცხვს
def odd_numbers():
    n = int(input("შეიყვანეთ რიცხვი: "))
    for i in range(1, n + 1, 2):
        print(i)

odd_numbers()