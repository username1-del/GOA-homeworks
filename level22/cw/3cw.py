# 3) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაბეჭდეთ ერთიდან ამ რიცხვამდე
# მხოლოდ ლუწი რიცხვების ჯამი ცალკე და მხოლოდ კენტი რიცვხების ჯამი ცალკე, გამოიყენეთ for loop
usernum = int(input("shemoitane ricxvi: "))

evennum=0 

oddnum=0
for i in range(1, usernum):
    if i % 2 ==0:
        evennum += i
    elif i % 3==0:
        oddnum += i
print(evennum)
print(oddnum)

