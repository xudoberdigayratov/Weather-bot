"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

from func import pogoda
from keyboard import menu, back

API_TOKEN = 'TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum OB-HAVO botga hush kelibsiz!", reply_markup=menu())


@dp.callback_query_handler(lambda call: call.data.startswith('pogoda_'))
async def pogoda_callback(call: types.CallbackQuery):
    infolist = call.data.split('_')
    if infolist[1] == 'Toshkent':
        result = await pogoda('погода-ташкент')
        if result:
            await call.message.edit_text(f"MIN: {result['min']}\nMAX: {result['max']}", reply_markup=back)
        else:
            await call.answer("Qandaydir xatolik yuz berdi!", show_alert=True)
    if infolist[1] == 'Fargona':
        result = await pogoda('погода-фергана')
        if result:
            await call.message.edit_text(f"MIN: {result['min']}\nMAX: {result['max']}", reply_markup=back)
        else:
            await call.answer("Qandaydir xatolik yuz berdi!", show_alert=True)
    else:
        await call.answer("BU viloyat ishlov jararyonida")


@dp.callback_query_handler(text='back')
async def pogoda_callback(call: types.CallbackQuery):
    await call.message.edit_text("Assalomu alaykum OB-HAVO botga hush kelibsiz!", reply_markup=menu())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
