import requests as req
from bs4 import BeautifulSoup

#SKU = "555088-063"
def hypeboost(SKU):
    try:
        print('Fetching Hypeboost product...')
        url = f'https://hypeboost.com/en/search/shop?keyword={SKU}'
        res = req.get(url)
        url2 = BeautifulSoup(res.content, 'lxml').a['href']
        res2 = req.get(url2)
        soup = BeautifulSoup(res2.text, 'lxml')
        payouts = {}
        for child in soup.select('.size'):
            if 'sold-out' in child['class']:
                payouts[child.select_one('.label').text.replace(' ½', '.5')] = 0
            else:
                payouts[child.select_one('.label').text.replace(' ½', '.5')] = round((int(child.select_one('.price span').text[:3])-1)*0.93-10,2)

        return [url2, payouts]
    except:
        print('Error fetching the product...')
        return None