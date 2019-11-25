import requests

def handler(event, context):
    try:
        res = requests.post(
            "https://devapi.currencycloud.com/v2/authenticate/api",
            params={},
            headers={"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
            data="login_id=matt%40fintechsandpit.com&api_key=e48a2102f918bab738e327af297f5f335231ffb0803d4d513a6b7a808f0d2c19"
        )
        print(res.json())

    except BaseException as e:
        # error handling goes here
        raise(e)
    