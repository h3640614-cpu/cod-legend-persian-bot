from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import TOKEN, CHANNEL, ADMIN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")],
        [InlineKeyboardButton("✅ بررسی عضویت", callback_data="check")]
    ]

    await update.message.reply_text(
        "🇮🇷 COD LEGEND PERSIAN 🇮🇷\n\n"
        "سلام 👋\n"
        "برای استفاده از ربات ابتدا عضو کانال شوید.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "check":
        keyboard = [
            [
                InlineKeyboardButton("🎁 اکانت رایگان", callback_data="account"),
                InlineKeyboardButton("📰 اخبار کالاف", callback_data="news")
            ],
            [
                InlineKeyboardButton("🔫 اتچمنت‌ها", callback_data="guns"),
                InlineKeyboardButton("🎮 آموزش", callback_data="learn")
            ],
            [
                InlineKeyboardButton("📞 پشتیبانی", url=f"https://t.me/{ADMIN}")
            ]
        ]

        await query.edit_message_text(
            "✅ خوش آمدید به COD LEGEND PERSIAN\n\n"
            "یکی از گزینه‌ها را انتخاب کنید:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "account":
        await query.edit_message_text(
            "🎁 اکانت رایگان\n\n"
            "در حال حاضر اکانت جدید موجود نیست.\n"
            "منتظر اطلاعیه‌های بعدی باشید."
        )

    elif query.data == "news":
        await query.edit_message_text(
            "📰 آخرین اخبار کالاف در کانال منتشر می‌شود."
        )

    elif query.data == "guns":
        await query.edit_message_text(
            "🔫 اتچمنت‌های حرفه‌ای به زودی اضافه می‌شوند."
        )

    elif query.data == "learn":
        await query.edit_message_text(
            "🎮 آموزش‌های کالاف به زودی قرار می‌گیرند."
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()
