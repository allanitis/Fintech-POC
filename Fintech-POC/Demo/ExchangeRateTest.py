from botocore.vendored import requests
import os

def handler(event, context):
    try:
        res = requests.get(
            "https://api.exchangerate-api.com/v4/latest/{}".format("usd"),
            params={},
            headers={"Accept":"application/json"}
        )
        # print(res.json())
        return res.json()['rates']['EUR']
    except BaseException as e:
        # error handling goes here
        raise(e)

    
    return {"message": "Successfully executed"}
