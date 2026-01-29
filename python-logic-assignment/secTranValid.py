balance=int(input("Please enter your balance: "))
withdraw=int(input("Please enter the amount you want to withdraw: "))
verifyStr=input("Verification status (True / False): ")
verify= True
if(verifyStr!="True"):
    verify=False
if(balance>=withdraw and verify):
    print("Withdraw Successful")
else:
    print("Transaction denied")
