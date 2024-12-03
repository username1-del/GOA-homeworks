# შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.
number=int(input("enter your number: "))
if number>=10 and number<=50:
    print("your number is more than 10 or less than 50")
else:
    print("your number is less than 10 or more than 50")
# აქ კოდი თუ რიცხვი არის 10-50 მდე მაგ შემთვევაში გამოიტანს if ს ხოლო სხვა დანარჩენ შემთხვევაში else ს