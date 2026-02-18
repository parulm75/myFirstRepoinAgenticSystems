numList=[]
with open("results.log","a") as log:
  with open("numbers.txt","r") as num:
    log.write("File opened successfully\n")
    for i in num:
        numList.append(int(i.strip()))
  length=len(numList)
  sum=sum(numList)
  avg=sum/length
  log.write(f"Read {length} numbers\n")
  log.write(f"Sum: {sum}\n")
  log.write(f"Average: {avg}\n")
  log.write("Process completed")

