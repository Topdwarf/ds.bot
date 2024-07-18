import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Вставте ваш новий токен бота тут
BOT_TOKEN = 'MTI2Mjg1MTI2MDg4MTY5ODg4OA.G2Oete.wlJN6xH_0dkLo4HDW8mxnFNPe77WZl6rgn0SCc'

# Розширена таблиця відповідностей
translation_table = {
    '3': 'а', '5': 'б', '9': 'в', '6': 'г', '4': 'д', '8': 'е', '7': 'ж',
    '2': 'з', '1': 'и', '¹': 'й', '0': 'к', '19': 'л', '14': 'м', '12': 'н',
    '16': 'о', '15': 'п', '17': 'р', '10': 'с', '11': 'т', '13': 'у', '18': 'ф',
    '20': 'х', '22': 'ц', '26': 'ч', '27': 'ш', '21': 'щ', '25': 'ъ', '23': 'ы',
    '28': 'ь', '29': 'э', '24': 'ю', '30': 'я', '31': ' ', '3a': 'А', '5b': 'Б',
    '9v': 'В', '6g': 'Г', '4d': 'Д', '8e': 'Е', '7zh': 'Ж', '2z': 'З', '1i': 'И',
    '1y': 'Й', '0k': 'К', '19l': 'Л', '14m': 'М', '12n': 'Н', '16o': 'О', '15p': 'П',
    '17r': 'Р', '10s': 'С', '11t': 'Т', '13u': 'У', '18f': 'Ф', '20h': 'Х', '22c': 'Ц',
    '26ch': 'Ч', '27sh': 'Ш', '21shch': 'Щ', '25': 'Ъ', '23y': 'Ы', '28b': 'Ь', '29e': 'Э',
    '24yu': 'Ю', '30ya': 'Я', '1001': 'привет', '1002': 'как дела', '1003': 'что нового', '1': 'эль', '1005': 'Привет', '666': 'смерть'
}

# Перевернемо таблицю відповідностей для зручності зворотного перекладу
reverse_translation_table = {v: k for k, v in translation_table.items()}

def code_to_text(code):
    translated_text = []
    codes = code.split()
    for code in codes:
        translated_text.append(translation_table.get(code, ''))
    return ''.join(translated_text)

def text_to_code(text):
    words = text.split(' ')
    translated_code = []
    for word in words:
        if word in reverse_translation_table:
            translated_code.append(reverse_translation_table[word])
        else:
            for char in word:
                if char in reverse_translation_table:
                    translated_code.append(reverse_translation_table[char])
                else:
                    translated_code.append(char)
        translated_code.append('31')  # додаємо код для пробілу між словами
    return ' '.join(translated_code).strip()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def start(ctx):
    await ctx.send("Какая лучшая закуска к элю?")
    answer = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    if answer.content.strip().lower() == "ее нет":
        await send_main_menu(ctx)
    else:
        await ctx.send("Неправильный ответ. Попробуйте снова.")
        await start(ctx)

async def send_main_menu(ctx):
    await ctx.send("Привет! Я твой бот-переводчик на дворфский. Выбери действие:\n1. Перевод текста в символы\n2. Перевод символов в текст\nВведите номер действия:")

@bot.command(name='1')
async def translate_text_to_code(ctx):
    await ctx.send("Введите текст на русском:")
    text = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    text = text.content.strip()
    translated_code = text_to_code(text)
    await ctx.send(f"Перевод в код: {translated_code}")

@bot.command(name='2')
async def translate_code_to_text(ctx):
    await ctx.send("Введите код:")
    code = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    code = code.content.strip()
    translated_text = code_to_text(code)
    await ctx.send(f"Перевод из кода: {translated_text}")

bot.run('MTI2Mjg1MTI2MDg4MTY5ODg4OA.G2Oete.wlJN6xH_0dkLo4HDW8mxnFNPe77WZl6rgn0SCc')
