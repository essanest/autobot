import random

# شبیه‌سازی تحلیل توکن‌ها – در نسخه واقعی به API های زنجیره‌ای متصل می‌شویم
async def analyze_top_tokens():
    mock_tokens = [
        {"symbol": "ABC", "score": random.randint(70, 95), "volume": 320000, "price": 0.002, "comment": "🔍 رشد طبیعی، حجم ورودی نهنگ"},
        {"symbol": "XYZ", "score": random.randint(60, 90), "volume": 410000, "price": 0.0009, "comment": "🚀 پامپ اولیه آغاز شده"},
    ]
    sorted_tokens = sorted(mock_tokens, key=lambda x: x["score"], reverse=True)
    return sorted_tokens
