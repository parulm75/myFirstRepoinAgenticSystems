import json
line='''{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}'''
dict=json.loads(line)
print("Request ID:",dict["id"])
print("Status: ",dict["status"])
print("Text: ",dict["result"]["text"])
if dict["result"]["confidence"]>=0.9:
    print("Confidence: ",dict["result"]["confidence"])
else:
    print("Confidence is low!")
new_dict={
    "id":5,
    "name": "Parul",
    "University": "York University",
    "results": {
        "firstYear": "Pass",
        "SecondYear": "inProgress"
    }
}
json_Str=json.dumps(new_dict)
with open("response.json","a") as js:
    js.write(json_Str)