#  12)  მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე
#  დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტი
num=int(input("sheiyvane ricxvi: "))
for i in range (0, num + 1):
    if i%2==0:
        print(str(i) + " luwia")
    else:
        print(str(i) + " kentia")
