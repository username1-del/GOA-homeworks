# 5) გააკეთეთ Find Minimum და გამოიყენეთ for loop. მიზანი: სიაში უნდა იპოვოთ მინიმალური ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [1]
num=[1,546,456,123]
num2 = num[0]

for i in num:
    if i < num2:
        num2 = i

print(num2)