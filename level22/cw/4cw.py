# 4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ 5 ის ჯერადი რიცხვების ჯამი
#  ცალკე და მხოლოდ 3ის ჯერადი რიცხვების ჯამი ცალკე, გამოიყენეთ while loop

num=int(input("sheiyvane ricxvi: "))

num1=0
num2=0
i=0

while i < num:
    if i % 5 == 0:
        num1 = num1 + i
    elif i % 3 == 0:
        num2= num2 + i
    i=i+1

print(num1)
print(num2)
