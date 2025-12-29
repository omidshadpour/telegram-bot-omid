# Telegram Multi-Feature Bot (Chat Project)

This project is a **multi-purpose Telegram bot** built with Python and the [python-telegram-bot](https://python-telegram-bot.org/) library.  
The bot provides various features to users and is designed in a modular structure.

---

## ✨ Features
- 🌤 **Weather**: Get weather information for different cities
- 💱 **Currency Exchange**: Convert currencies (USD, EUR, GBP, JPY)
- 🥇 **Gold Price**: Show real-time gold prices
- 🌍 **Multi-language Translation**: Translate text into different languages (English, French, Arabic, German)
- ℹ️ **Help**: Display available commands and bot features

---

## 📂 Project Structure


project/ 
│── bot.py              # نقطه‌ی شروع ربات 
│── handlers.py         # مدیریت منو و دستورات 
│── requirements.txt    # لیست کتابخانه‌های مورد نیاز 
│── Procfile            # تنظیمات دیپلوی (Heroku/Railway) 
│── runtime.txt         # نسخه‌ی پایتون برای دیپلوی 
│── README.md           # توضیحات پروژه 
│ ├── services/           # سرویس‌های اصلی 
│   ├── weather.py 
│   ├── currency.py 
│   ├── gold.py 
│   └── translate.py 
│ └── utils/              # ابزارهای جانبی 
└── logger.py


---

## 🚀 Installation & Usage

1. Clone the project:
```bash
git clone <repo-url>
cd <repo-folder>

2. Install dependencies:
pip install -r requirements.txt

3. Set environment variable TOKEN:
export TOKEN=<your-telegram-bot-token>

On Windows:
setx TOKEN "<your-telegram-bot-token>"

4. Run the bot:
python bot.py


🛠 Deployment on Railway/Heroku
- Procfile and runtime.txt are already prepared.
- Push the project to Railway or Heroku and set the environment variable TOKEN.
- The bot will run automatically.

👨‍💻 Developer
This project was created by Omid shadpour with the goal of learning and building a professional multi-feature Telegram bot.
