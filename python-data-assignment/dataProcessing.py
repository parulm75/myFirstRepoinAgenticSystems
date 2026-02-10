def avgCalculator(users):
    avg=[]
    
    for user in users:
        scores = user["scores"]
        avgs = sum(scores) / len(scores) if scores else 0
        avg.append(avgs)
    return avg
def checkAdminAccess(roles):
    if "admin" in roles:
        return True
    else:
        return False
def main():
    users = [
        {
            "name": "Parul",
            "scores": [85, 90, 88],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Aman",
            "scores": [70, 75, 80],
            "roles": {"viewer"}
        },
        {
            "name": "Riya",
            "scores": [92, 95, 91],
            "roles": {"editor"}
        }
    ]
    avg=avgCalculator(users)
    n=0
    for user in users:
        print("Name:", user["name"])
        print("Average Score:", avg[n])
        print("Admin Access:",checkAdminAccess(user["roles"]))
        n+=1
        
main()

