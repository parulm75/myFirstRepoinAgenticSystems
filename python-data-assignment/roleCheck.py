employee=(102,"Parul","IT")
roles={"editor","viewes","management","admin"}
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])
if "admin" in roles:
    print("Admin access: Yes")
else:
    print("Admin Access: No")
