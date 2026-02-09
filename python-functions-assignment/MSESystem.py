def greet(name):
    return "Hello, "+name+"!"  
def calculateNoAndAvg(marks):
    avg=0
    for i in marks:
        avg+=i
    avg/=len(marks)
    return len(marks),avg
def checkPass(avg):
    if(avg>=50):
        return "Pass"
    else:
        return "Fail"
def main():
    marks=[50.0,65.0,80.0]
    num,avg=calculateNoAndAvg(marks)
    print(greet("Parul"))
    print("Subject: ",num)
    print("Average Score: ",avg)
    print("Result: ",checkPass(avg))
main()