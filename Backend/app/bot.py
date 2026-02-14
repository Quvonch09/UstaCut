from aiogram import Bot
from config import BOT_TOKEN, ADMIN_ID  # ✅ oldin: from app.config ...

bot = Bot(token=BOT_TOKEN)

async def send_to_admin(data):
    text = f"""
✂️ *Yangi bron*
Mijoz: {data.client_name}
Tel: {data.phone}
Barber: {data.barber}
Sana: {data.date}
⏰ Vaqt: {data.time}
Xizmat: {data.service}
Izoh: {data.comment or '-'}
"""
    await bot.send_message(
        chat_id=ADMIN_ID,
        text=text,
        parse_mode="Markdown",
    )
