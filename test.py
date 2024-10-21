import serial
import time
import asyncio
from telegram import Bot

async def send_message(token, chat_id, message):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message)
def check_water_level_and_send_alert():
 
    ser = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2) 

    
    TOKEN = '7701423940:AAHM6rAyOhXSV_iCdb4DZeUVLmJDFGqju-I'
    CHAT_ID = '7162488936' 
    WATER_LEVEL_THRESHOLD = 15  

    while True:
        if ser.in_waiting > 0: 
            try:
               
                arduino_data = ser.readline().decode('utf-8').strip()
                print("Arduino Output:", arduino_data)

          
                if "Water Level" in arduino_data:
                    water_level = int(arduino_data.split()[2]) 

                    if water_level > WATER_LEVEL_THRESHOLD:
                        print(f"Water level ({water_level} cm) is high! Sending alert...")

                        message = f"Warning: Water level is high"
                        asyncio.run(send_message(TOKEN, CHAT_ID, message))

            except Exception as e:
                print(f"Error reading Arduino data: {e}")

if __name__ == "__main__":
    check_water_level_and_send_alert()