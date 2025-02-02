# 8) შექმენით shopping სია სადაც მომხმარებელს შეეძლება რამე ნებისმიერი პროდუქტის დამატება და წაშლა,
#  როდესაც მორჩებიან შოპინგს დაუპრინტეთ საბოლოოდ რა შეიძინეს 
shopping=[]

while True:
    item = input("ra gnebavt?: ")
    shopping.append(item)
    print("ras daamatebt?")
    print("gaagrdzelebt? ki/ara")
    pasuxi= input()
    if pasuxi == "ara":
         break
print(shopping)