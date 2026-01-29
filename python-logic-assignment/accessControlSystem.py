age=int(input("Please enter your age: "))
checkID=input("Whether they have an ID card (True or False): ")
if(age>=18 and checkID=="True"):
    print('Entry allowed')
elif(checkID!="False" and checkID!="True"):
    print("You have not correctly validated your id")
else:
    print("Entry not allowed")