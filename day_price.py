CRYPTO_LIST = [
    "BTC",
    "ETH",
    "XBC",
    "SOL",
    "binance coin",
    "xrp"

]

# Replace with your API endpoint URL
URL = 'https://api.intotheblock.com/BTC/financial/price'  # Replace with your API endpoint URL

# Define custom headers as needed
HEADERS = {
    "accept": "*/*",
    "accept-language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "if-none-match": "W/\"8fe1-sf8tyaTuird76r5dolW/bG2PkJ0\"",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Microsoft Edge\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-api-key": "OT9ln7Tw3Q2Q5ErqXt34c9dwlxED9tE738cEYz3W",
    "Referer": "https://www.coindesk.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

FILE_PATH = 'daily_price.csv'

COLUMNS = 'price'