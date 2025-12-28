from telegram.ext import ApplicationBuilder , CommandHandler , MessageHandler , ConversationHandler , ContextTypes ,filters 
from handlers import start , handler_message , help_commend , ask_city ,weather_command , ask_currency , currency_command , CHOOSING , WEATHER ,CURRENCY
import os

def main():

    TOKEN = os.getenv("TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler("start" , start)],
        states = {
            CHOOSING : [
                MessageHandler(filters.Regex("^هواشناسی$") , ask_city),
                MessageHandler(filters.Regex("^نرخ ارز$") , ask_currency),
                MessageHandler(filters.Regex("^راهنما$"), help_commend)
            ] ,
            WEATHER : [MessageHandler(filters.TEXT & ~filters.COMMAND , weather_command)],
            CURRENCY : [MessageHandler(filters.TEXT & ~filters.COMMAND , currency_command)]
        } ,
        fallbacks = [CommandHandler("cancel" , help_commend)]
    )


    application.add_handler(CommandHandler("help" , help_commend))
    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND , handler_message))

    print("ربات در حال اجرا است")
    application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
