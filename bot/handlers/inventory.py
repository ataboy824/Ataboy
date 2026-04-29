from telegram import Update
from telegram.ext import ContextTypes
from bot.database import get_conn, get_or_create_user
from bot.keyboards import inventory_menu, main_menu, back_button

async def handle_inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "inventory_menu":
        await query.edit_message_text(
            "📦 Omborxona:",
            reply_markup=inventory_menu()
        )
    
    elif query.data == "inventory_add":
        context.user_data['state'] = 'inv_name'
        await query.edit_message_text(
            "Mahsulot nomini kiriting:",
            reply_markup=back_button()
        )
    
    elif query.data == "inventory_list":
        user_id = get_or_create_user(
            update.effective_user.id,
            update.effective_user.full_name
        )
        conn = get_conn()
        c = conn.cursor()
        c.execute('SELECT name, quantity, price FROM products WHERE user_id = ?', (user_id,))
        items = c.fetchall()
        conn.close()
        
        if not items:
            text = "📦 Omborxona bo'sh."
        else:
            text = "📦 Mahsulotlar:\n\n"
            for item in items:
                text += f"• {item[0]}: {item[1]} dona — {item[2]:,.0f} so'm\n"
        
        await query.edit_message_text(text, reply_markup=back_button())
    
    elif query.data == "main_menu":
        await query.edit_message_text("Asosiy menyu:", reply_markup=main_menu())
