from telegram import Update , ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from services.weather import get_weather
from services.currency import get_currency

# ------------------ /start ------------------

async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["آیدا"],
        ["وضعیت هوا"],
        ["نرخ ارز"],
        ["راهنما"]

    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard = True 
    )

    user_first_name = update.effective_user.first_name
    massage = f"سلام {user_first_name} آیدا جونم! یکی از گزینه‌ها رو انتخاب کن."

    await update.message.reply_text(massage , reply_markup = reply_markup)

# ------------------ /help ------------------

async def help_commend(update : Update  , context: ContextTypes.DEFAULT_TYPE):

    message = (
              "📌 راهنمای ربات امید\n\n"
        "من می‌تونم این کارها رو انجام بدم:\n"
        "1️⃣ وضعیت هوا:\n"
        "   مثال: هوا تهران چطوره؟\n\n"
        "2️⃣ نرخ ارز:\n"
        "   مثال: دلار به یورو\n"
        "   مثال: یورو به دلار\n"
        "   مثال: پوند چنده؟\n\n"
        "3️⃣ پیام‌های معمولی:\n"
        "   مثال: سلام\n\n"
        "برای هر سوالی همینجا بنویس 🌟"
    )

    await update.message.reply_text(message)

# ------------------ /weather ------------------

async def weather_command(update: Update , context : ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text("لطفاً نام شهر را بعد از دستور بنویس. مثال:\n/weather tehran")

    city = " ".join(context.args)
    result = get_weather(city)

    await update.message.reply_text(result)

# ------------------ /currency ------------------

async def currency_command(update: Update , context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("لطفاً دو ارز را وارد کن. مثال:\n/currency usd eur")

    base = context.args[0].upper()
    target = context.args[1].upper()

    result = get_currency(base , target)

    await update.message.reply_text(result)


# ------------------ /message ------------------

async def handler_message(update: Update , context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    if user_text == "سلام":
        reply = "سلام خوشحالم که با من حرف میزنی"

    elif user_text == "راهنما":
        reply = (
            "📌 راهنمای ربات:\n"
            "/weather tehran\n"
            "/currency usd eur\n"
            "یا از دکمه‌ها استفاده کن 🌟"
        )

    elif user_text == "وضعیت هوا":
        reply = "اسم شهر رو بگو. مثال: تهران"

    elif user_text == "نرخ ارز":
        reply = "دو ارز رو بگو. مثال: دلار به یورو"

    elif "هوا" in user_text:

        cities = ["tehran" , "mashhad" , "isfahan" , "shiraz" , "tabriz"]
        found_city = None
        
        for city in cities:
            if city in user_text:
                found_city = city
                break
        if found_city:
            reply = get_weather(found_city)
        else:
            reply = "لطفا اسم شهر رو بگو تا بتونم وضعیت هوا رو بگم"

    elif "دلار" in user_text or "یورو" in user_text or "پوند" in user_text or "ین" in user_text:
        map_fa_to_iso = {
            "دلار" : "USD",
            "یورو" : "EUR",
            "پوند" : "GBP",
            "ین" : "JPY",
        }
        base , target = None , None

        for far_word , iso_code in map_fa_to_iso.items():
            if far_word in user_text:
                if "به" in user_text:
                    
                    parts = user_text.split("به")
                    if len(parts) == 2:
                        src_text = parts[0].strip()
                        dst_text = parts[1].strip()

                        for far_src ,iso_src in map_fa_to_iso.items():
                            if far_src in src_text:
                                base = iso_src
                                break
                        
                        for far_dst , iso_dst in map_fa_to_iso.items():
                            if far_dst in dst_text:
                                target = iso_dst
                                break

                else:
                    base = iso_code
                    target = "USD" if iso_code != "USD" else "EUR"
        
        if base and target:
            reply = get_currency(base , target)
        else:
            reply =  "لطفاً تبدیل ارزی رو دقیق‌تر بگو (مثلاً دلار به یورو)."


    else:
        reply = f" تو نوشتی {user_text} و من یه ربات ساده هستمم ولی قراره هوشمند شم"

    await update.message.reply_text(reply)


    



