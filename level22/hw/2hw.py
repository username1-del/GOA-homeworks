# 2) მომხმარებელს შემოატანინეთ რიცხვი
#  შემდეგ კი ერთიდან ამ რიცხვამდე
#  დაბეჭდეთ რიცხვების საშუალო
#  არითმეტიკული
num=int(input("sheiyvane ricxvi: "))
total=0
count=0

for i in range(1, num+1):

    total+=i
    count+=1

num3= total / count
print (num3)