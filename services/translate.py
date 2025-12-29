import requests

def translate_text(text : str , target_lang : str = "en"):

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client" : "gtx",
        "sl" : "auto",
        "tl" : target_lang ,
        "dt" : "t" ,
        "q" : text
    }

    try:
        response = requests.get(url , params = params)
        data = response.json()

        translated = data[0][0][0]

        return f"ترجمه: {translated}"
    
    except Exception:
        return "خطایی رخ داد، لطفاً بعداً تلاش کنید."
