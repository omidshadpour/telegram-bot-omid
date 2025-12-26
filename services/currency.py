import requests

def get_currency(base: str , target: str):
    url = f"https://api.frankfurter.app/latest?from={base}&to={target}"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "خطا در اتصال به سرویس نرخ ارز."

        data = response.json()

        if "rates" not in data or target not in data["rates"]:
            return "نرخ ارز مورد نظر پیدا نشد."
        rate = data["rates"][target]

        return f"هر 1 {base} برابر با {rate} {target} است."
    except Exception:
        return "خطایی رخ داده ، لطفا بعدا تلاش کنید"