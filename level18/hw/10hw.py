#  10) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვები

number=int(input("შეიყვანეთ რიცხვი: "))

for i in range(0, number + 1):
    if i%2==0:
        print(i)
