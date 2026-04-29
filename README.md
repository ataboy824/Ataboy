# SavdoChi — O'zbekistondagi kichik biznes uchun Telegram bot

SavdoChi is a Telegram bot in Uzbek that helps small businesses manage:

- 🛒 Orders (`Buyurtmalar`)
- 💰 Customer debts (`Qarzlar`)
- 📦 Inventory (`Omborxona`)
- 📊 Daily/weekly/monthly sales reports (`Hisobot`)

Each Telegram user has their own private inventory and ledger — multiple shop
owners can use the same bot instance.

## Tech stack

- Python 3.11
- [`python-telegram-bot`](https://docs.python-telegram-bot.org/) v21 (long polling)
- SQLite for storage

## Project layout

```
.
├── bot/
│   ├── main.py            # entry point, handler wiring
│   ├── database.py        # SQLite schema + queries
│   ├── keyboards.py       # reply / inline keyboards
│   ├── utils.py
│   ├── locales/
│   │   └── uz.py          # all user-facing strings (Uzbek)
│   └── handlers/
│       ├── start.py
│       ├── orders.py
│       ├── inventory.py
│       ├── debts.py
│       └── reports.py
├── requirements.txt
├── Procfile               # `worker: python -m bot.main`
├── railway.json           # Railway deployment config
├── nixpacks.toml          # Nixpacks build config (Railway)
├── runtime.txt            # Python version pin
└── .env.example
```

## Run locally

```bash
# 1. Create a virtualenv (optional but recommended)
python3.11 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your bot token
export TELEGRAM_BOT_TOKEN="<token from @BotFather>"

# 4. Start the bot
python -m bot.main
```

The SQLite database is created automatically at `data/savdochi.db` on first
run.

## Deploy on Railway

1. Push this repository to GitHub.
2. Go to [railway.app](https://railway.app) and click **New Project →
   Deploy from GitHub repo**.
3. Pick this repo. Railway auto-detects Python via `requirements.txt` and uses
   the start command from `railway.json` / `Procfile`:

   ```
   python -m bot.main
   ```

4. In **Variables**, add:

   | Key                   | Value                                  |
   | --------------------- | -------------------------------------- |
   | `TELEGRAM_BOT_TOKEN`  | The token from @BotFather              |
   | `SAVDOCHI_DB_PATH`    | `/data/savdochi.db` (if you mount a volume) |

5. **Add a Volume** (recommended) so your SQLite database survives redeploys:
   - In the service, open **Settings → Volumes → + New Volume**.
   - Mount path: `/data`
   - Then set `SAVDOCHI_DB_PATH=/data/savdochi.db` in Variables.

6. Click **Deploy**. Once the logs show
   `SavdoChi bot is starting (long polling)...`, message your bot on Telegram.

> ⚠️ Telegram only allows one polling client per bot token at a time. If you
> were running the bot somewhere else (e.g. locally), stop it before Railway
> takes over — otherwise you'll see `Conflict: terminated by other getUpdates
> request` errors.

## Bot commands

| Command   | What it does                       |
| --------- | ---------------------------------- |
| `/start`  | Show the main menu                 |
| `/menu`   | Same as `/start`                   |
| `/help`   | Help screen                        |
| `/cancel` | Cancel the current flow            |
| `/skip`   | Skip the customer name when adding an order |

## License

MIT — do whatever you want with it. Built for shops in Uzbekistan 🇺🇿
