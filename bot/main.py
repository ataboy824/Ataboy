import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from bot.database import init_db
from bot.handlers import start, orders, inventory, debts, reports

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN topilmadi!")
    
    init_db()
    
    app = Application.builder().token(token).build()
    
    # Handlerlar
    app.add_handler(CommandHandler("start", start.start_command))
    app.add_handler(CallbackQueryHandler(orders.handle_orders, pattern="^orders"))
    app.add_handler(CallbackQueryHandler(inventory.handle_inventory, pattern="^inventory"))
    app.add_handler(CallbackQueryHandler(debts.handle_debts, pattern="^debts"))
    app.add_handler(CallbackQueryHandler(reports.handle_reports, pattern="^reports"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, orders.handle_text))
    
    app.run_polling()

if __name__ == '__main__':
    main()
