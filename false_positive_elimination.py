# Answer of question 2.BONUS

import requests
from auth import get_access_token

plugin_id = "50686" #Your false positive plugin id
host_id = "192.168.23.128" #Your host id
username = "USERNAME" #Your username
password = "PASSWORD" #Your password

#This function send post request to Nessus plugin rule API and eliminates false positive vulnerability.
def eliminate_vulnerability(plugin_id, host_id, username, password):
    url = "https://localhost:8834/plugin-rules" #Nessus plugin rule API link
    token = get_access_token(username, password) #Get access token for authentication.
    if token:
        #Auth keys for successful request
        header = {"X-Cookie":"token={}".format(token),
                  "Content-Type": "application/json"}
        
        #Payload for spesific process 
        data = {"host":host_id,
                "plugin_id":plugin_id,
                "type":"exclude",
                "date": None} 
        
        requests.post(url, headers=header, json=data, verify=False)

eliminate_vulnerability(plugin_id, host_id, username, password)
