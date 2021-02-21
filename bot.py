import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level = logging.INFO)



PROXY = {'proxy_url': settings.PROXY_URL,
        'urllib3_proxy_kwargs' : {'username' : settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print ('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь')


def planet_name(update, context):
    if update.message == 'eqw':
        print ('asddasd')

    update.message.reply_text('vxzc')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context = True, request_kwargs = PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()