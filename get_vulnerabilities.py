# Answer of question 2.C

import requests
import json
from auth import get_access_token

scan_id = 21 #Your scan id
host_id = 2 # Your host id
username = "USERNAME" #Your username
password = "PASSWORD" #Your password

#This function send get request to Nessus vulnerability API and export the vulnerability json to scripts path.
def get_vulnerabilities_json(scan_id, host_id, username, password):
    url = "https://localhost:8834/scans/{}/hosts/{}".format(str(scan_id), str(host_id)) #Nessus vulnerability API link
    token = get_access_token(username, password) #Get access token for authentication.
    if token:
        header = {
            "X-Cookie":"token={}".format(token),
            "Content-Type":"application/json"
        }
        response = requests.get(url, headers=header, verify=False)
        result = json.loads(response.text)
        vulnerability_json = {"vulnerabilities": result["vulnerabilities"]} #Select only vulnerability part from json.
        with open("metasploitable3_vulnerabilities_C_output.json", "w") as outfile: #Json export
            json.dump(vulnerability_json, outfile, indent=4)

get_vulnerabilities_json(scan_id, host_id, username, password)
