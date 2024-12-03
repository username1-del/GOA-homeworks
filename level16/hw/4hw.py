# 4) გიორგიმ შექმნა ზოოპარკი სადაც შესვლა მხოლოდ კონკრეტული აღნაგობის ხალხს შეუძლიათ. გიორგი ზოოპარკში უშვებს
#  ხალხს რომელიც 180 სანტიმეტრზე მაღლები არიან და 50-90 კილოს შორის არიან წონით.
#  თქვენი მისიაა რომ მომხმარებელს შემოატანინოთ წონა და სიმაღლე და გაარკვიოთ შეუძლია თუ არა მომხმარებელს
#  ზოოპარკის მონახულება.


height = int(input("Enter your height: "))
kg = int(input("Enter your kg: "))

if height == 180 and 50 <= kg <= 90:
    print("You can enter")
elif height > 180 and 50 <= kg <= 90:
    print("You can enter")
else:
    print("You can't enter see you next year")
