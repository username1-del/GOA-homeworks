# 4) შექმენით სია, სადაც გექნებათ 1-იდან 30-ის ჩათვლით რიცხვები. თქენი დავალებაა რომ ამ სიიდან აირჩიოთ
#  ერთი ინდექსი, მომხმარებელმა კი უნდა შეიყვანოს ის ინდექსი რომელიც თქვენ აირჩიეთ. გამოიყანეთ while loop-ი
#  იმისთვის რომ თუ მომხმარებელმა არ შეიყვანა ის ინდექსი რომელიც თქვენ აირჩიეთ, დაბეჭდოთ მესიჯი
#  "Incorrect, Please try again" და ახლიდან მოსთხოვოს რიცხვის შეყვანა. სხვა შემთხვევაში თუ მომხმარებელმა
#  შეიყვანა ინდექსი რომელიც თქვენ აირჩიეთ,  დაბეჭდეთ "You guessed the number!". სხვა შემთხვევაში თუ მომხმარებლის
#  შეყვანილი რიცხვი არის მეტი 30-ზე, ამოუგდოს მესიჯი "Incorrect, You must enter a number from 1 to 30"
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,]

my_number = 27



while True:
    
        user_number = int(input("enter number here:"))

        if user_number <1 or user_number > 30:
            print("Incorrect, You must enter a number from 1 to 30")

        elif user_number != my_number:
            print("Incorrect, Please try again")

        # elif user_number < str:
            # print("invalid input please try a number")

        else:
            print("You guessed the number!")