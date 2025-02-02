from turtle import *
# 13) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია შემდეგ კი დაბეჭდავს ამ სიაში არსებული რიცხვების ჯამს
def num_list():
    num = [1,2,4,5,6,11,14,25]
    num2 = 0
    for i in range (len(num)):
        num2 += num[i]

    print(num2)
num_list()