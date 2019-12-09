# from botocore.vendored import requests
import requests
import json

def handler(event, context):

    auth = "87f6488cdf52cb641fbd9002f148c48d"
    
    try:
        res = requests.post(
            "https://devapi.currencycloud.com/v2/conversions/create",
            params={},
            headers={"X-Auth-Token":auth,"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
            data="buy_currency=usd&sell_currency=eur&fixed_side=buy&amount=1000&term_agreement=true"
        )
        print(res.json())
    except BaseException as e:
        # error handling goes here
        raise(e)
    
    