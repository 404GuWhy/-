import telebot
import random
from telebot import types

# import TOKEN from config - если в визуал коде

# вставьте сюда токен вашего бота
TOKEN = 'ваш токен'
bot = telebot.TeleBot(TOKEN)

# короткие факты
facts = [
    "Меньше мяса — меньше выбросов. Попробуй заменить говядину курицей или овощами хотя бы раз в неделю.",
    "Ходи пешком или катайся на велосипеде. Короткие поездки без машины — большой плюс для планеты.",
    "Выключай свет и приборы, когда они не нужны. Это экономит энергию и снижает выбросы.",
    "Не покупай лишнего. Ремонтируй вещи вместо того, чтобы выбрасывать, и покупай с рук.",
    "Сажай деревья и зелень. Растения очищают воздух и поглощают CO₂.",
    "Сортируй мусор. Переработка алюминия экономит 95% энергии по сравнению с производством из сырья.",
    "Экономь воду. Меньше времени в душе — меньше энергии на нагрев и перекачку.",
    "Выбирай зелёную энергию, если есть возможность. Солнце и ветер не загрязняют воздух.",
    "Бери сумку из дома вместо пластикового пакета. Меньше пластика — меньше отходов.",
    "Отключай зарядку из розетки. Даже без телефона она продолжает тратить электричество."
]

def fact_keyboard():
    """Кнопка «Ещё факт» под каждым фактом."""
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔄 Ещё факт", callback_data="get_fact"))
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🌱 Получить факт", callback_data="get_fact"))
    bot.reply_to(message, "Привет! Нажми кнопку ниже — и я пришлю простой факт о том, как помочь планете.", reply_markup=markup)

@bot.message_handler(commands=['antiglobalwarmingfact'])
def send_fact(message):
    fact = random.choice(facts)
    bot.reply_to(message, fact, reply_markup=fact_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == "get_fact")
def callback_fact(call):
    fact = random.choice(facts)
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, fact, reply_markup=fact_keyboard())

bot.polling(none_stop=True)
