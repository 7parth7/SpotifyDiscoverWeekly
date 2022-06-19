import requests
import base64
from pprint import pprint
import json

#clientID = "21e7bf05b9e34b8b9193cd132e238353"
#clientSecret = "59cbbf7ccef840b38b3b77411049d04a"

base_uri = "https://api.spotify.com/v1"
token = "Bearer BQDQkzd1vunbE-kMFGT0gRkWGcrPTK1X42N6oCMe71Z0ZmjKAU4vAq1_6b2PRVVEe3yCsxTWdNRjH8z_F1j4V4JzaIadHgV1wxeOx8taSR8wIEQAsKWqk0S3W9mZsjPzU_3eQixCc3QTZfYMzR1NKyywaMwPX7gB5uJnJqzyjaO8SWgu2-G0QDNGF83K-ceUAVvbGuO1ZA3FZFbapMSAzzRYPUyb1JxR0WoD9BVUGxYJVo7fahYz663Psvs5mbBYfIvNXAg"

def authorize():
    auth_header = {'Authorization' : "Basic MjFlN2JmMDViOWUzNGI4YjkxOTNjZDEzMmUyMzgzNTM6NTljYmJmN2NjZWY4NDBiMzhiM2I3NzQxMTA0OWQwNGE=",
                    'Content-Type':'application/x-www-form-urlencoded'
                    }
    params = {'grant_type':'client_credentials'}
    url = base_uri + "/api/token"
    response = requests.post(url,headers=auth_header,params=params)
    print(response.text)

def discover_weekly():

    track_list = []

    auth_header = {'Authorization' : token,
                    'Content-Type':'application/json',
                    'Accept': 'application/json'}
    url = base_uri + "/playlists/37i9dQZEVXcGC5dYZXQeb1/tracks"
    response = requests.get(url,headers=auth_header)
    resp = json.loads(response.text)
    #print(resp)
    
    for i in resp["items"]:
        track_list.append((i["track"]["uri"]))#.split(":"))[2])
    return(track_list)

def addToArchive(track_list):
    
    tracks = ",".join(track_list)

    auth_header = {'Authorization' : token,
                    'Content-Type':'application/json',
                    'Accept': 'application/json'}
    url = base_uri + "/playlists/2QhTgrWeLP4HMU1Ovq8QGa/tracks"
    params = {'uris':tracks}
    response = requests.post(url,headers=auth_header,params=params)
    resp = json.loads(response.text)
    print(resp)

def test():

    sec = ("21e7bf05b9e34b8b9193cd132e238353:59cbbf7ccef840b38b3b77411049d04a")
    sec = sec.encode('ascii')
    sec = base64.b64encode(sec)
    sec = sec.decode('ascii')
    print(sec)

def main():
    x = discover_weekly()
    #test()
    #authorize()
    addToArchive(x)

if __name__ == "__main__":
    main()
