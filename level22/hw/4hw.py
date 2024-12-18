#4) მომხმარებელს შემოატანინეთ რიცხვი
#  შემდეგ კი ერთიდან ამ რიცხვამდე
#  დაბეჭდეთ ყველა რიცხვის ორზე
#  ნამრავლების ჯამი

num=int(input("sheiyvane ricxvi: "))
jami=0
for i in range(1, num + 1):
    jami += i * 2
    print(jami)