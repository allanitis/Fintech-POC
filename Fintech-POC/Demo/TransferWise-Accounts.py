from botocore.vendored import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://api.sandbox.transferwise.tech/personal",
            params={},
            headers={"Accept":"application/json"}
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        raise(e)
    
    return {"message": "Successfully executed"}
