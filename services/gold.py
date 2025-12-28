import requests
import os

def get_gold_price():
    API_KEY = os.getenv("NAVASAN_API_KEY")
    url = f"https://api.navasan.tech/latest/?api_key={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if "gold_18k" not in data:
            return "نتونستم قیمت طلا رو پیدا کنم."

        price = data["gold_18k"]["value"]

        return f"قیمت هر گرم طلای ۱۸ عیار: {price:,} تومان"
    except Exception:
        return "خطایی رخ داده است ، لطفا بعدا تلاش کنید."
    

