from telegram.ext import ApplicationBuilder , CommandHandler , MessageHandler , ConversationHandler , ContextTypes ,filters 
from handlers import start , handler_message , help_command , ask_city ,weather_command , ask_currency , currency_command , gold_command , ask_translate , choose_lang ,translate_command , cancel , CHOOSING , WEATHER ,CURRENCY , TRANSLATE , CHOOSE_LANG
import os

def main():

    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        raise ValueError("❌ متغیر محیطی TOKEN تنظیم نشده است.")
    application = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler("start" , start)],
        states = {
            CHOOSING : [
                MessageHandler(filters.Regex("^🌤 هواشناسی$") , ask_city),
                MessageHandler(filters.Regex("^💱 نرخ ارز$") , ask_currency),
                MessageHandler(filters.Regex("^🥇 قیمت طلا") , gold_command),
                MessageHandler(filters.Regex("^🌍 ترجمه") , ask_translate),
                MessageHandler(filters.Regex("^ℹ️ راهنما"), help_command)
            ] ,
            WEATHER : [MessageHandler(filters.TEXT & ~filters.COMMAND , weather_command)],
            CURRENCY : [MessageHandler(filters.TEXT & ~filters.COMMAND , currency_command)],
            CHOOSE_LANG : [MessageHandler(filters.TEXT & ~filters.COMMAND , choose_lang)],
            TRANSLATE : [MessageHandler(filters.TEXT & ~filters.COMMAND , translate_command)]

        } ,
        fallbacks = [CommandHandler("cancel" , cancel)]
    )


    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("cancel", cancel))
    application.add_handler(
        MessageHandler(
            filters.Regex("^(سلام|hi|hello|مرسی|ممنون)$"),
            handler_message
        )
    )

    application.add_handler(conv_handler)

    
    print("ربات در حال اجرا است")
    application.run_polling()

if __name__ == "__main__":
    main()
