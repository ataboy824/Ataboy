from telegram import Update
from telegram.ext import ContextTypes
from bot.database import get_or_create_user
from bot.keyboards import main_menu

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    get_or_create_user(user.id, user.full_name)
    
    await update.message.reply_text(
        f"Assalomu alaykum, {user.first_name}! 👋\n\n"
        "SavdoChi botiga xush kelibsiz!\n"
        "Quyidagi bo'limlardan birini tanlang:",
        reply_markup=main_menu()
    )
