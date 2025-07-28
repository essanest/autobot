import httpx
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from token_analyzer import analyze_tokens_and_generate_report

API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

async def handle_telegram_update(update):
    try:
        message = update.get("message", {}).get("text", "")
        chat_id = update.get("message", {}).get("chat", {}).get("id", TELEGRAM_CHAT_ID)

        if message.lower() in ["start", "/start", "سلام", "بیدار شو", "awake", "wake"]:
            await send_message(chat_id, "✅ بات فعال است و گزارش‌ها را ارسال خواهد کرد.")
        elif message.lower() in ["خواب", "sleep"]:
            await send_message(chat_id, "😴 بات به حالت خواب می‌رود.")
        elif message.lower() in ["گزارش", "report"]:
            report = await analyze_tokens_and_generate_report()
            await send_message(chat_id, report)
        else:
            await send_message(chat_id, "دستور نامشخص است. برای راهنما، «گزارش» یا «start» را ارسال کنید.")
    except Exception as e:
        print(f"Error in handle_telegram_update: {e}")
        return {"ok": False}
    return {"ok": True}

async def send_message(chat_id, text):
    async with httpx.AsyncClient() as client:
        await client.post(f"{API_URL}/sendMessage", json={"chat_id": chat_id, "text": text})
