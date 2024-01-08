# Answer of question 2.D

import requests
import json
from auth import get_access_token

scan_id = 21 #Your scan id
username = "USERNAME" #Your username
password = "PASSWORD" #Your password

#This function send get request to Nessus scan info API and export the scan information json to scripts path.
def get_info_json(scan_id, username, password):
    url = "https://localhost:8834/scans/{}".format(str(scan_id)) #Nessus scan info API link
    token = get_access_token(username, password) #Get access token for authentication.
    if token:
        header = {
            "X-Cookie":"token={}".format(token),
            "Content-Type":"application/json"
        }
        response = requests.get(url, headers=header, verify=False)
        result = json.loads(response.text)
        info_json = {"info": result["info"]} #Select only vulnerability part from json.
        with open("metasploitable3_vulnerabilities_D_output.json", "w") as outfile: #Json export
            json.dump(info_json, outfile, indent=4)

get_info_json(scan_id, username, password)
