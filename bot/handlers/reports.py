from telegram import Update
from telegram.ext import ContextTypes
from bot.database import get_conn, get_or_create_user
from bot.keyboards import main_menu, back_button

async def handle_reports(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "reports_menu":
        user_id = get_or_create_user(
            update.effective_user.id,
            update.effective_user.full_name
        )
        conn = get_conn()
        c = conn.cursor()
        
        c.execute('''SELECT COUNT(*), COALESCE(SUM(total), 0) 
                     FROM orders WHERE user_id = ? 
                     AND date(created_at) = date("now")''', (user_id,))
        today = c.fetchone()
        
        c.execute('''SELECT COUNT(*), COALESCE(SUM(amount), 0) 
                     FROM debts WHERE user_id = ? AND is_paid = 0''', (user_id,))
        debts = c.fetchone()
        
        c.execute('''SELECT COUNT(*), COALESCE(SUM(quantity * price), 0) 
                     FROM products WHERE user_id = ?''', (user_id,))
        inventory = c.fetchone()
        
        conn.close()
        
        text = (
            "📊 Hisobot:\n\n"
            f"🛒 Bugungi buyurtmalar: {today[0]} ta\n"
            f"💵 Bugungi tushum: {today[1]:,.0f} so'm\n\n"
            f"💰 Joriy qarzlar: {debts[0]} ta\n"
            f"💸 Jami qarz: {debts[1]:,.0f} so'm\n\n"
            f"📦 Mahsulotlar: {inventory[0]} tur\n"
            f"🏪 Ombor qiymati: {inventory[1]:,.0f} so'm"
        )
        
        await query.edit_message_text(text, reply_markup=back_button())
    
    elif query.data == "main_menu":
        await query.edit_message_text("Asosiy menyu:", reply_markup=main_menu())
