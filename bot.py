from telegram.ext import ApplicationBuilder , CommandHandler , MessageHandler , filters 
from handlers import start , handler_message , help_commend , weather_command , currency_command 

def main():
    BOT_TOKEN = "8021508877:AAHcWcLKv_F7A3YaNMX7qQ7ue711jl1r-YM"

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start" , start))
    application.add_handler(CommandHandler("help" , help_commend))
    application.add_handler(CommandHandler("weather" , weather_command))
    application.add_handler(CommandHandler("currency" , currency_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND , handler_message))

    print("ربات در حال اجرا است")
    application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
