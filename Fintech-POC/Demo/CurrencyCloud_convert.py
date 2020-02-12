import boto3
s3 = boto3.client("s3")
from botocore.vendored import requests
import CC_Auth

def handler(event, context):
    cc_key = CC_Auth.getAuthToken()['auth_token']
    try:
        res = requests.post(
            "https://devapi.currencycloud.com/v2/conversions/create",
            params={},
            headers={"X-Auth-Token":cc_key,"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
            data="buy_currency=USD&sell_currency=EUR&fixed_side=buy&amount=12000&term_agreement=true"
        )
        return res.json()
    except BaseException as e:
        # error handling goes here
        raise(e)

    


    
    return {"message": "Successfully executed"}
