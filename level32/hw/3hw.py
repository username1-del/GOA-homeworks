# 4) გააკეთეთ Find Maximum და გამოიყენეთ for loop. მიზანი: სიაში უნდა იპოვოთ მაქსიმუმი ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [546]
num=[1,546,456,123]
num2= num[0]

for i in num:
    if i > num2:
        num2 = i

print(num2)