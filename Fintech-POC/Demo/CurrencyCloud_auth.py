from botocore.vendored import requests
import os

def handler(event, context):
    try:
        res = requests.post(
            "https://devapi.currencycloud.com/v2/authenticate/api",
            params={},
            headers={"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
            data="login_id={}&api_key={}".format(os.environ["CC_LOGIN"], os.environ["CC_KEY"])
        )
        print(res.json())
    except BaseException as e:
        # error handling goes here
        raise(e)
    
    return {"message": "Successfully executed"}
