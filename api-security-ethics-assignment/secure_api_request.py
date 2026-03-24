import os 
import requests
url="https://api.example.com/data"
API_KEY=os.environ.get("API_KEY")
if not API_KEY:
        raise EnvironmentError("API_KEY environment variable is not set.")
headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
try:
  response=requests.get(url,headers=headers)
  if(response.status_code==200):
        print(response.json())
  elif(response.status_code==429):
        print("Rate limit reached. Try again later.")
  else:
        print("Request Failed")
except requests.exceptions.ConnectionError:
      print("Could not connect to API")
      print("The given URL is a dummy URL")