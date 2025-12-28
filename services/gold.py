import requests
import os

def get_gold_price():
    API_KEY = os.getenv("NAVASAN_API_KEY")
    url = f"https://api.navasan.tech/latest/?api_key={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        if "18ayar" not in data:
            return "نتونستم قیمت طلا رو پیدا کنم."

        price = data["18ayar"]["value"]

        return f"قیمت هر گرم طلای ۱۸ عیار: {price:,} تومان"
    except Exception:
        return "خطایی رخ داده است ، لطفا بعدا تلاش کنید."
    

