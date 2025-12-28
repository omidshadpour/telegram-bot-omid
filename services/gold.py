import requests
import os

def get_gold_price():
    API_KEY = os.getenv("NAVASAN_API_KEY")
    url = f"https://api.navasan.tech/latest/?api_key={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if "18ayar" in data:
            price = data["18ayar"]["value"]
            return f"قیمت هر گرم طلای ۱۸ عیار: {price:,} تومان"

        if "abshodeh" in data:
            price = int(data["abshodeh"]["value"])
            return f"قیمت هر مثقال طلای آبشده: {price:,} تومان"

        if "sekkeh" in data:
            price = int(data["sekkeh"]["value"])
            return f"قیمت سکه امامی: {price:,} تومان"

        return "متأسفم، هیچ اطلاعاتی درباره قیمت طلا پیدا نشد."

        
    except Exception:
        return "خطایی رخ داده است ، لطفا بعدا تلاش کنید."
    

