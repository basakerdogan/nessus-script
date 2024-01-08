import requests
import json

#This function takes the Nessus username and password to create an access token.
def get_access_token(username, password): 
    url = "https://localhost:8834/session" #Nessus API link
    post_data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=post_data, verify=False) #The argument "verify=False" is required because Nessus connection has no SSL cert.
    if response.status_code == 200:
        data = json.loads(response.text)
        return data["token"]
    else:
        print("Token cannot be received. Please check username and password again.")