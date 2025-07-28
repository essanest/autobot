from fastapi import FastAPI, Request
import uvicorn
from telegram_handler import handle_telegram_update

app = FastAPI()

@app.post("/")
async def telegram_webhook(request: Request):
    update = await request.json()
    return await handle_telegram_update(update)

@app.get("/")
async def root():
    return {"message": "Essanbot backend running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

