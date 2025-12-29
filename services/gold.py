import requests
from bs4 import BeautifulSoup

def get_gold_price():
    url = "https://www.tgju.org/profile/geram18"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.txt , "html.parser")

        price_tag = soup.find("span" , {"id" : "info-price"})
        if not price_tag:
            return "نتونستم قیمت طلا رو پیدا کنم."

        price = price_tag.text.stip()
        
        return f"قیمت هر گرم طلای ۱۸ عیار: {price:,} تومان"

    except Exception:
        return "خطایی رخ داده است ، لطفا بعدا تلاش کنید."
    

