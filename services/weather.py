import requests
import os

def get_weather(city: str):
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fa"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return "متاسفم ، نتونستم اطلاعات هواشناسی رو پیدا کنم"
        city_name = data["name"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"هوای {city_name} الان {temp} درجه سانتی‌گراد و وضعیت: {description}"

    
    except Exception as e:
        return "خطایی رخ داده ، لطفا بعدا تلاش کنید"