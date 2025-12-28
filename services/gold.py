import requests

def get_gold_price():
    url = "https://api.accessban.com/v1/market/indicator/price_gram_18k"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            return "نتونستم قیمت طلا رو پیدا کنم."

        price = int(data["data"]["price"])
        return f"قیمت هر گرم طلای ۱۸ عیار: {price:,} تومان"

    except Exception:
        return "خطایی رخ داده است ، لطفا بعدا تلاش کنید."
    

