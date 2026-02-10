contact={"Ravi": 78739,"Anita":83938, "Sunita": 838747, "Kavish": 928298, "Pankaj": 988288}
print(contact)
name=input("Please enter a name to search: ")
check=False
for i in contact:
    if(i==name):
        check=True
if(check):
    print("Phone number is ",contact[name])
else:
    print("Contact not found")