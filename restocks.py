import requests as req
import json
from bs4 import BeautifulSoup

#SKU = "FZ5823"
def restocks(SKU):
    try:
        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "en-GB,en;q=0.6",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Brave\";v=\"110\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "cookie": "cookieconsent_status=dismiss; _slvddv=true; _slvs=54cc9166-c1e1-4375-bb4b-7143ae5c7fb7; __cf_bm=k9HY8JegURwt6BEyVwhGz.HrKDabct6cPxrIFQ3gbNc-1677413267-0-AV1WZdVWl3lankqHSl738Bnre3+A8ATAFRiFxAyb0Y2kA/3NMyIzF7LLwDh3KbZuAI3yRSwjUFXqUwwiXm1OwLazwkZodneu+eD4glywxD/aeUQEdyXbrJUpknY6h+a6mojaAWVoQ8QvsTjdsnZgNHM=; locale=eyJpdiI6InBuMHlnR3NoT3pqUm81akptQjZsMmc9PSIsInZhbHVlIjoiSnZqVEViL1ZhU3pLTVoyZVJkRlRqQnF0U2d2SzdhQnhqRWMvV2dmbWdaTXBIaWh3c2FRK1p1MVBORW1CalRzcSIsIm1hYyI6ImE3OWI0NDVhZDczMDRjZWE4MmNiNTMwYWM5MjgxMjVjODk5NGRlZDdiZjMzMmIzZmUyMzkzOGI0ZGU4YWYxNDMiLCJ0YWciOiIifQ%3D%3D; XSRF-TOKEN=eyJpdiI6Ill5SHRLbUU5YS9XZDNBUW04UWFNOFE9PSIsInZhbHVlIjoiSGg2VHFmNW9aNHVzVVdUU3JOVUtXNGFsbDlmQUV1bjhqSDlBMU9wNGFHQW01Q1hpWXlBMkFtYXBWR3poL1QxZVBxWjQ1UzNsclRyNGhDeENDVUQzVU4wQzZlRzlrbWhLMUZCVEJwV2ZXWGZmQkR0L1lHU1dqUC9kV1FqV1VsYXUiLCJtYWMiOiJiYTAwNWE2NmMxM2E5MDJmNjIwMjYzZWY2MTQ2ZDE1MTEzNDczZTAzNWMxMmUyODQzOWNjZDYxZGRhNDc0YmYxIiwidGFnIjoiIn0%3D; restocks_session=eyJpdiI6ImJob0Z3K1pzQlFDM0F5NHU0aENuZ3c9PSIsInZhbHVlIjoiaDhIbFZ4cjJDYTZGTXNHZzdsK0VhQ2dnRWFCNCtGclVVQkgwN0lFZWlNclFWVFFYM1VDbnlwSURqclg0M1JyNmNXY1VlbVM0OERSdlFRSGtMMnRpNUpYU3h6UlQ5M3FNTVBKT3ZlMTkzZXZYeHNJYlhuV0g5RVdjUGl2Wk4rdVUiLCJtYWMiOiIzODNhMTk2YTcyMzFjOGI2NTc1YjBjZTU4M2Y3YmI1OGYzNDcwNzgxNzA0ZTY1YmJkOGI4N2YwOTE1YzNmZTA0IiwidGFnIjoiIn0%3D; country=eyJpdiI6IitXZ2hKMzRyR21XdXRlbHY4a0JnK3c9PSIsInZhbHVlIjoiYzAvemFteHNFZHF0TWlCRjYxZ0FKZWFCc1J4dTl5a09xdkprZmt4S0JTcFpNUUZCOHUzQjlaLy9CMEtId1lGMCIsIm1hYyI6IjBmMmM3NGY3M2M4Y2UwZDQ5MjkwYWNkNTk2NzI0ZjFkNDhkZjhkNDIwOWM1OWEzOTYwM2UzZTU2NGViNjlmYTkiLCJ0YWciOiIifQ%3D%3D; valuta=eyJpdiI6IkNELzFCNURIRjMrem5CL1ordlVjelE9PSIsInZhbHVlIjoibG80d1hGMHlRd2VrUkQ2TmNoZlNLWHlDOHZxZ3pWcE9jVC81THdSVXQ3dUxlZGxOa2lROGlTcWN6YmlvR050eSIsIm1hYyI6IjZhMTAzOTQ1NmNiYjNhYTgyMGM0MjJhMGMzMDQ1NmU2YmI0ZDAxYmU1MjYxZTllNjVhZjY3MmY1NTI4YThlODkiLCJ0YWciOiIifQ%3D%3D",
        "Referrer-Policy": "strict-origin-when-cross-origin"
  } 
        print('Fetching Restocks product...')
        url = f'https://restocks.net/en/shop/search?q={SKU}'
        res = req.get(url)
        url2 = res.json().get('data')[0].get('slug')
        res2 = req.get(url2, headers= headers)
        soup = BeautifulSoup(res2.content, 'lxml')
        payouts = {}
        for child in soup.find_all('ul', class_='select__size__list'):
            for x in child.find_all('span', class_='text'):
                size = x.text.replace(' ½', '.5')
                if x.parent.find('span', class_='float-right price').text != 'Notify me':
                    if x.parent.find('span', class_='sell__method__value').text == 'resale':
                        price = x.parent.find('span', class_='').text[1:]
                        if '.' in price:
                            price = int(x.parent.find('span', class_='').text[1:].split('.')[0])*1000+int(x.parent.find('span', class_='').text[1:].split('.')[1])
                        else:
                            price = int(price)
                        payouts[size] = round(price*.9-20,2)
        return [url2, payouts]
    except:
        print('Error fetching the product...')
        return None
#restocks(SKU)