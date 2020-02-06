from botocore.vendored import requests
import os

def handler(event, context):
    rates = {}
    try:
        tw_res = requests.get(
            "https://api.sandbox.transferwise.tech/v1/rates",
            params={"source":"usd","target":"eur"},
            headers={"Accept":"application/json", "Authorization": "Bearer {}".format(os.environ["TRANSFERWISE_KEY"])}
        )
        rates['transferwise'] = tw_res.json()[0]['rate']

        er_res = requests.get(
            "https://api.exchangerate-api.com/v4/latest/{}".format("usd"),
            params={},
            headers={"Accept":"application/json"}
        )
        # print(res.json())
        rates['exchange_rate_api'] = er_res.json()['rates']['EUR']

    except BaseException as e:
        # error handling goes here
        raise(e)
    
    return {"message": "Successfully executed", "rates": rates, "best": max(rates.items(), key= lambda x:x[1])}
