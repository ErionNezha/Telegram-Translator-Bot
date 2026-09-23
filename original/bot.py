import telebot
from googletrans import Translator
#@iq_python - @DuDrD
bot = telebot.TeleBot("Token")
translator = Translator()
#@iq_python - @DuDrD
@bot.message_handler(func=lambda message: True)
def tr(message):
    text = message.text
    wait = bot.reply_to(message, "wait . . .")
    es = translator.translate(text, dest='es').text
    en = translator.translate(text, dest='en').text
    ar = translator.translate(text, dest='ar').text
    zh = translator.translate(text, dest='zh-cn').text
    Tu = translator.translate(text, dest='tr').text
    bot.delete_message(message.chat.id, wait.message_id)
    bot.reply_to(message,f'''▫️ Translated for : `{text}`
▫️🇬🇧 English : `{en}`
▫️🇪🇸 Spanish : `{es}`
▫️🇮🇶 Arabic : `{ar}`
▫️🇨🇳 Chinese  : `{zh}`
▫️🇹🇷Turkish : `{Tu}`''',parse_mode="markdown")

bot.infinity_polling()