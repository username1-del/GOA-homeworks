# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე
#  დაბეჭდეთ მხოლოდ ლუწი რიცხვების ჯამი, გამოიყენეთ for loop

usernum = int(input("enter number: "))

evensum = 0
for i in range(usernum):
    print(i)
    if i % 2 == 0:
        print(evensum + i)

print(evensum)