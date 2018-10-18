import requests, json

def oauth(code,state, app) :
    url = app.config.get("OAUTH_URL")
    print(url)

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_id\"\r\n\r\n14681\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_secret\"\r\n\r\n11a7876f133ab52f30681e1b97e271153b18fa2f\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"code\"\r\n\r\n"+code+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "028c29a5-4486-f665-2ec5-96ec926e86cd"
        }
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.json()['athlete']['username'])

    return response.json()
