from telegram import  Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import httpx
import asyncio
import json

URL = "http://127.0.0.1:5000/message"

async def post(chat_id, message_text, bot):
    async with httpx.AsyncClient(timeout=httpx.Timeout(120.0)) as client:
        response = await client.post(
        URL,
        json={
            "chat_id": chat_id,
            "text": message_text,
            "source": "telegram"
        })
        data = response.json()
        print(data['content'])
        await bot.send_message(chat_id=chat_id, text=data['content'])

async def handleMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    message_text = update.message.text

    asyncio.create_task(post(chat_id, message_text, context.bot))



def main() -> None:
    application = Application.builder().token("TOKEN").build()
    
    application.add_handler(MessageHandler(filters.ALL, handleMessage))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()