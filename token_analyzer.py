from analyzer import analyze_top_tokens

async def analyze_tokens_and_generate_report():
    try:
        top_tokens = await analyze_top_tokens()
        if not top_tokens:
            return "❌ توکنی با شرایط مناسب یافت نشد."
        message = "📈 گزارش تحلیلی بازار:\n"
        for token in top_tokens:
            message += f"\n🔹 {token['symbol']} - امتیاز: {token['score']}%\n"
            message += f"📊 حجم: {token['volume']} - قیمت: {token['price']}\n"
            message += f"🧠 تحلیل: {token['comment']}\n"
        return message
    except Exception as e:
        return f"خطا در تولید گزارش: {str(e)}"
