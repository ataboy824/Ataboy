from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🛒 Buyurtmalar", callback_data="orders_menu")],
        [InlineKeyboardButton("📦 Omborxona", callback_data="inventory_menu")],
        [InlineKeyboardButton("💰 Qarzlar", callback_data="debts_menu")],
        [InlineKeyboardButton("📊 Hisobot", callback_data="reports_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)

def back_button():
    keyboard = [[InlineKeyboardButton("🔙 Orqaga", callback_data="main_menu")]]
    return InlineKeyboardMarkup(keyboard)

def orders_menu():
    keyboard = [
        [InlineKeyboardButton("➕ Yangi buyurtma", callback_data="orders_new")],
        [InlineKeyboardButton("📋 Buyurtmalar ro'yxati", callback_data="orders_list")],
        [InlineKeyboardButton("🔙 Orqaga", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)

def inventory_menu():
    keyboard = [
        [InlineKeyboardButton("➕ Mahsulot qo'shish", callback_data="inventory_add")],
        [InlineKeyboardButton("📋 Mahsulotlar", callback_data="inventory_list")],
        [InlineKeyboardButton("🔙 Orqaga", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)

def debts_menu():
    keyboard = [
        [InlineKeyboardButton("➕ Qarz qo'shish", callback_data="debts_add")],
        [InlineKeyboardButton("📋 Qarzlar ro'yxati", callback_data="debts_list")],
        [InlineKeyboardButton("🔙 Orqaga", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)
