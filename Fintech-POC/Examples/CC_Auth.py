import requests
try:
    res = requests.post(
        "https://devapi.currencycloud.com/v2/authenticate/api",
        params={},
        headers={"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
        data="login_id=you%40youremail.com&api_key=e48a2102f318bab738e327s3f237f5g335231ffb0803d4d513a6b7a808f0d2c19"
    )
    print(res.json())
except BaseException as e:
    raise(e)
