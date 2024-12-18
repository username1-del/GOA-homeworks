#  5) მომხმარებელს შემოატანინეთ რიცხვი
#  შემდეგ კი ერთიდან ამ
#  რიცხვამდე დაბეჭდეთ
#  ყველა რიცხვის ნამრავლი

num=int(input("shemoitane ricxvi: "))
namravli = 1

for i in range(1, num + 1):
    namravli *= i
    print(namravli)


