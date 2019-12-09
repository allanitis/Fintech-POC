from botocore.vendored import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://api.sandbox.transferwise.tech/v1/rates",
            params={},
            headers={"Authorization":"Bearer 10dfbb33-b207-4339-95a4-66193a761bc1","Accept":"application/json"}
        )
        print(res.json())
    except BaseException as e:
        # error handling goes here
        raise(e)
    
    return {"message": "Successfully executed"}
