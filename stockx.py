import json
import requests
from config import SIZES
from math import floor

#SKU = "55508-063"


def stockx(SKU):
    try:
        print("Fetching stockx product...")
        url1 = f"https://stockx.com/api/browse?_search={SKU}&currency=EUR&country=PL"

        headers = {
            "accept": "*/*",
            "accept-encoding": "utf-8",
            "accept-language": "en-gb,gzip,deflate",
            "alt-used": "stockx.com",
            "app-platform": "Iron",
            "appos": "web",
            "appversion": "0.1",
            "authorization": "",
            "connection": "keep-alive",
            "host": "stockx.com",
            "referer": "https://stockx.com/en-gb",
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "te": "trailers",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }

        urlKey = str(
            json.loads(requests.get(url1, headers=headers).text)["Products"][0][
                "urlKey"
            ]
        )
        url2 = f"https://stockx.com/api/products/{urlKey}?includes=market,360&currency=EUR&country=PL"
        res = requests.get(url2, headers=headers)

        product = dict(res.json().get("Product"))

        payouts = {}
        info = [product['media']['imageUrl'],f"https://stockx.com/en-gb/{urlKey}", product['title']]
        for uuid, child in product.get("children").items():
            size = SIZES[child.get("shoeSize")]
            lowest_ask = child.get("market").get("lowestAsk")
            payouts[size] = round(floor(int(lowest_ask) / 1.05 - 1) * 0.88 - 5, 2)

        info.append(payouts)
        return info

    except:
        print("Error fetching the product")

        return None

#stockx(SKU)