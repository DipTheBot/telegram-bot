from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


YOUR_USER_ID = 6679923300 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != YOUR_USER_ID:
        await update.message.reply_text("This bot is currently under maintenance ⚠️")
        return
    await update.message.reply_text("Hello Master How Can I Help You ?")
app = ApplicationBuilder().token("8072776107:AAG-m1sHhuCK_Lpoj4pSlKn0MStcghuLOqk").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
