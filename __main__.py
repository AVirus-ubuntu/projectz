... # temp
from __config__ import cfg

from telebot import TeleBot, types

import sqlite3
import colorama
colorama.init()
import warnings
warnings.filterwarnings('ignore')

bot = TeleBot(cfg.TOKEN)

@bot.message_handler(content_types=["text"])
def getmessage(msg):
    conn = sqlite3.connect(cfg.DATABASE)
    curs = conn.cursor()

    curs.execute(f'''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY
    )''')
    conn.commit()

    if msg.chat.type == 'private':
        data = curs.execute(f'SELECT id FROM users WHERE id = {msg.from_user.id}').fetchone()
        if data is None:
            curs.execute(f'INSERT INTO users(id) VALUES(?)', [msg.from_user.id])
            conn.commit()
        data = curs.execute(f'SELECT id FROM users WHERE id = {msg.from_user.id}').fetchone()

        if msg.from_user.id in cfg.ADMINSID:
            if msg.text == '$PS' or msg.text == '/start':
                bot.send_message(msg.chat.id, 'Привет, ты вродь админ, это бот для рекламы\n\nЭтот текст - `/start`, `$PS`\nЕсли что-то напишешь другое, бот отправит это всем зарегестрированным юзерам в формате html\n\n**by AVirus**\n[GitHub SRC](https://github.com/AVirus-ubuntu/projectz)', parse_mode='Markdown')
            elif msg.text != '$PS' and msg.text != '/start':
                kb = types.InlineKeyboardMarkup(row_width=1).add(
                    types.InlineKeyboardButton('😈 Подтвердить', callback_data=f'confirm-|-{msg.from_user.id}-|-{msg.text}'),
                    types.InlineKeyboardButton('👿 Отказаться_', callback_data=f'cancel')
                )
                bot.send_message(msg.chat.id, 'Подтвердите отправку сообщений', parse_mode='html', reply_markup=kb)
    curs.close()
    conn.close()

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect(cfg.DATABASE)
    curs = conn.cursor()

    if call.data.split('-|-', maxsplit=2)[0] == 'confirm':
        bot.send_message(call.message.chat.id, 'Ок :)', parse_mode='html')
        t = 0
        f = 0
        for x in curs.execute(f'SELECT id FROM users').fetchall():
            try:
                if x[0] != int(call.data.split('-|-', maxsplit=2)[1]):
                    bot.send_message(x[0], call.data.split('-|-', maxsplit=2)[2].strip(), parse_mode='html')
                    t+=1
            except Exception as e: f+=1
        bot.send_message(call.message.chat.id, f'Отправлено:\n<i>{str(t):_<6}</i> _успешных сообщений\n<i>{str(f):_<6}</i> сломанных сообщений\n\n$PS', parse_mode='html')
    elif call.data.split('-|-', maxsplit=2)[0] == 'cancel':
        bot.send_message(call.message.chat.id, 'Ну, как хочешь', parse_mode='html')
    curs.close()
    conn.close()
while True:
    try: bot.infinity_polling(none_stop=True)
    except Exception as e: ...