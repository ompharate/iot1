import asyncio
from telegram import Bot

async def send_message(token, chat_id, message):
   
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    TOKEN = '7701423940:AAHM6rAyOhXSV_iCdb4DZeUVLmJDFGqju-I'
    CHAT_ID = '7162488936' 
    MESSAGE = 'Your water level is high'

    asyncio.run(send_message(TOKEN, CHAT_ID, MESSAGE))