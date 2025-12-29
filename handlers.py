from telegram import Update , ReplyKeyboardMarkup
from telegram.ext import ContextTypes , ConversationHandler
from services.weather import get_weather
from services.currency import get_currency
from services.gold import get_gold_price
from services.translate import translate_text

CHOOSING , WEATHER , CURRENCY , CHOOSE_LANG , TRANSLATE= range(5)

# ------------------ /start ------------------

async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["هواشناسی"],
        ["نرخ ارز"],
        ["قیمت طلا"],
        ["ترجمه"],
        ["راهنما"]

    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard = True 
    )

    user_first_name = update.effective_user.first_name
    massage = f"سلام {user_first_name}! یکی از گزینه‌ها رو انتخاب کن 👇"

    await update.message.reply_text(massage , reply_markup = reply_markup)
    return CHOOSING


# ------------------ /weather ------------------

async def ask_city(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اسم شهر رو بگو . مثال : تهران")
    return WEATHER

async def weather_command(update: Update , context : ContextTypes.DEFAULT_TYPE):
    city = update.message.text.strip()
    result = get_weather(city)
    await update.message.reply_text(result)

    await start(update , context)
    return CHOOSING

# ------------------ /currency ------------------

async def ask_currency(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دو ارز رو بگو. مثال: دلار به یورو")
    return CURRENCY


async def currency_command(update: Update , context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    map_fa_to_iso = {
        "دلار" : "USD",
        "یورو" : "EUR",
        "پوند" : "GBP",
        "ین" : "JPY"
    }

    base , target = None , None

    if "به" in user_text:
        parts = user_text.split("به")
        if len(parts) == 2:
            src_text = parts[0].strip()
            dst_text = parts[1].strip()

            for fa , iso in map_fa_to_iso.items():
                if fa in src_text:
                    base = iso
                    break
            
            for fa , iso in map_fa_to_iso.items():
                if fa in dst_text:
                    target = iso
                    break
            
    else:
        for fa , iso in map_fa_to_iso.items():
            if fa in user_text:
                base = iso
                target = "USD" if iso != "USD" else "EUR"
                break
    
    if base and target:
        result = get_currency(base , target)
    else:
        result = "لطفاً تبدیل ارزی رو دقیق‌تر بگو (مثلاً دلار به یورو)."

    await update.message.reply_text(result)

    await start(update , context)
    return CHOOSING


# ------------------ /gold ------------------

async def gold_command(update: Update , context: ContextTypes.DEFAULT_TYPE):
    result = get_gold_price()
    await update.message.reply_text(result)
    return CHOOSING


# ------------------ /translate ------------------

async def ask_translate(update: Update , context : ContextTypes.DEFAULT_TYPE):
    keyboard =  [
        ["انگلیسی" , "فرانسوی"],
        ["عربی","آلمانی"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard , one_time_keyboard = True , resize_keyboard = True)
    await update.message.reply_text("لطفاً زبان مقصد رو انتخاب کن:" , reply_markup = reply_markup)
    return CHOOSE_LANG

async def choose_lang(update: Update , context : ContextTypes.DEFAULT_TYPE):
    lang_map = {
        "انگلیسی": "en",
        "فرانسوی": "fr",
        "عربی": "ar",
        "آلمانی": "de"

    }

    chosen = update.message.text
    context.user_data["target_lang"] = lang_map.get(chosen , "en")
    await update.message.reply_text("لطفاً متنی که می‌خوای ترجمه کنم رو وارد کن:")
    return TRANSLATE


async def translate_command(update: Update , context : ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    target_lang = context.user_data.get("target_lang" , "en")
    result = translate_text(text , target_lang = target_lang)

    await update.message.reply_text(result)
    return CHOOSING


# ------------------ /help ------------------

async def help_command(update : Update  , context: ContextTypes.DEFAULT_TYPE):

    message = (
        "📌 راهنمای ربات امید\n\n"
        "1️⃣ وضعیت هوا: /weather tehran\n"
        "2️⃣ نرخ ارز: /currency usd eur\n"
        "یا از دکمه‌های منو استفاده کن 🌟"
    )


    await update.message.reply_text(message)
    return CHOOSING

# ------------------ /end ------------------
async def cancel(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("گفتگو پایان یافت.")
    return ConversationHandler.END


# ------------------ /message ------------------

async def handler_message(update: Update , context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    if user_text == "سلام":
        reply = "سلام خوشحالم که با من حرف میزنی"

    elif user_text == "راهنما":
        reply = "از منو استفاده کن یا دستور /help رو بزن 🌟"
         
    elif user_text == "هواشناسی":
        return await ask_city(update , context)

    elif user_text == "نرخ ارز":
        return await ask_currency(update , context)

    elif user_text == "قیمت طلا":
        reply = " این قسمت به زودی اظافه میشه"

    else:
        reply = f"دستور نا شناخته است ، لطفا از منو استفاده کنید"                        

    await update.message.reply_text(reply)
