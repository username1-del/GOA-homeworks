# 5) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები, შეამოწმეთ
#  რიცხვი ლუწია თუ კენტი და თუ კენტია დაამატეთ ახალ ლისტში 
num=[0,1,2,3,4,5,6,7,8,9,10]
odd_num2=[]
for i in range(len(num)):
    if num[i] % 2 != 0:
        odd_num2.append(i)
print(odd_num2)