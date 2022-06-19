import requests
import base64
from pprint import pprint
import json

clientID = "21e7bf05b9e34b8b9193cd132e238353"
clientSecret = "59cbbf7ccef840b38b3b77411049d04a"

base_uri = "https://api.spotify.com/v1"

def discover_weekly():

    track_list = []
    #auth_params = {"grant_type" : "client_credentials"}
    auth_header = {'Authorization' : "Bearer BQD5G30pAIw1qCEV7hDCTJRbp9p9xV5MAr6puobwGUgixZhytLZbGuiS0vKiyZf8Geez2l28QQRufQTozvQBYmgpIw_aOvLP0726hiVus0dCiAC8pG4lEf5DndFy41hbCqw_iLtMiG98J1ieRJEVEROdGhQ6E-mqhaO8TzrB-RIcrYq7Ug4KZGRwxTL-T1DXDWuOKH_lsXHI",
                    'Content-Type':'application/json',
                    'Accept': 'application/json'}
    url = base_uri + "/playlists/37i9dQZEVXcGC5dYZXQeb1/tracks"
    response = requests.get(url,headers=auth_header)
    #print(type(response.text))
    resp = json.loads(response.text)
    #print(type(resp["items"]))
    #print(resp["items"][0]["track"]["uri"])

    for i in resp["items"]:
        track_list.append(((i["track"]["uri"]).split(":"))[2])
    print(len(track_list))



def test():

    sec = ("21e7bf05b9e34b8b9193cd132e238353:59cbbf7ccef840b38b3b77411049d04a")
    sec = sec.encode('ascii')
    sec = base64.b64encode(sec)
    sec = sec.decode('ascii')
    print(sec)

def main():
    authorize()
    #test()
    

if __name__ == "__main__":
    main()
