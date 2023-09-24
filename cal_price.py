URL = "https://production.api.coindesk.com/v2/tb/metrics/list?assets=all&metrics=all" 

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Microsoft Edge\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://www.coindesk.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

FILE_PATH = 'calculation_price.csv'

COLUMNS = 'data'

