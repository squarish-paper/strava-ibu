import requests, json

def oauth(code,state, app) :
    url = app.config.get("OAUTH_URL")
    print("[API] | Calling " + url)

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_id\"\r\n\r\n14681\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_secret\"\r\n\r\n11a7876f133ab52f30681e1b97e271153b18fa2f\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"code\"\r\n\r\n"+code+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "028c29a5-4486-f665-2ec5-96ec926e86cd"
        }
    #TODO: Error Handle this
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()

def get_athlete_activities(bearer, lastLogon, app):

    url = app.config.get("BASE_URL") + "/athlete/activities?after=" + str(lastLogon)
    print("[API] | Calling " + url)
    headers = {'Authorization': 'Bearer ' + bearer}
    response = requests.get(url, headers=headers)

    return response.json()


def get_activity(bearer,activity_id,app):

    url = app.config.get("BASE_URL") + "/activities/" + str(activity_id)
    print("[API] | Calling " + url)
    headers = {'Authorization': 'Bearer ' + bearer}
    response = requests.get(url, headers=headers)
    return response.json()

def get_segment(bearer,segment_id,app):
    url = app.config.get("BASE_URL") + "/segments/" + str(segment_id)
    print("[API] | Calling " + url)
    headers = {'Authorization': 'Bearer ' + bearer}
    response = requests.get(url, headers=headers)
    return response.json()
