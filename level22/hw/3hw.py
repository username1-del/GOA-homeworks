# 3) მომხმარებელს შემოატანინეთ რიცხვი
#  შემდეგ კი ერთიდან ამ რიცხვამდე
#  დაბეჭდეთ ყველა რიცხვის კვადრატის ჯამი
num=int(input("sheiyvane ricxvi: "))
total=0

for i in range(1, num + 1):
    total += i**2
    print(total)