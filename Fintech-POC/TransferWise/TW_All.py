from botocore.vendored import requests
import os

def handler(event, context):
    try:
        res = requests.get(
            "https://api.sandbox.transferwise.tech/v1/rates",
            params={"source":"USD","target":"EUR"},
            headers={"Accept":"application/json","Authorization": "Bearer {}".format(os.environ['TRANSFERWISE_KEY'])}
        )
        j = res.json()
        print(j[0]['rate'])
        # print(res.json())
    except BaseException as e:
        # error handling goes here
        raise(e)
    
    return {"message": "Successfully executed", rate: j}
