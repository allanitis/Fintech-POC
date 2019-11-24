import requests

def handler(event, context):
    try:
        res = requests.post(
            "https://devapi.currencycloud.com/v2/conversions/create",
            params={},
            headers={"X-Auth-Token":auth,"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
            data="buy_currency=usd&sell_currency=eur&fixed_side=buy&amount=1000&term_agreement=true"
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        raise(e)
    
    return {"message": "Successfully executed"}
