for i in range(1,10,2):
    print(i)
age = 5
DOB=input("collect age")
while int(DOB) != age:
    print ("you're underage")
    DOB = input("collect age")
else:
    print("you're eligible")
    
