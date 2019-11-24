import requests
import json

def handler(event, context):
    
    return {"message": "Successfully executed"}
    try:
        res = requests.post(
            "https://api.sandbox.transferwise.tech/accounts",
            params={},
            headers={"Accept":"application/json","Content-Type":"application/json"},
            data=json.dumps({"myreqest": "usd"})
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        raise(e)
