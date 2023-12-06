import os

import requests

import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler

from modules import config_manager

known_users = {
    #111: {'name':'John'},
    #222: {'name':'Doe'},
}

GOOGLE_SCRIPTS_URL = config_manager._get_config('basic', 'crop_book', 'google_scripts_url')
project_name = config_manager._get_config('basic', 'root', 'project_name')

def start(update, context):
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text="Aquest és el bot del llibre de camp de {}.".format(project_name))

def telegram_bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    updater = Updater(token=os.environ["TELEGRAM_TOKEN"], use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        username = update.message.from_user.username

        # Send info to googlesheets
        payload = text_to_dict(update.message.text, username)
        response = save_to_googlesheets(payload)
        # Reply with the same message
        if response['result'] == 'success':
            bot.sendMessage(chat_id=chat_id, text='Hey {} la teva comanda s''ha registrat a la fila {}'.format(username, response['row']))    
            for key in known_users:
                bot.sendMessage(chat_id=key, text='{} ha registrat la seguent activitat: "{}"'.format(username, update.message.text))    

        else:
            bot.sendMessage(chat_id=chat_id, text=update.message.text+'/n'+'No s''ha pogut guardar correctament. Revisar.')
    return "{'result':'success', 'version':1}"


def text_to_dict(text, name):
    l = text.split('/')
    payload = {
        'A': name,
        'B': l[0].lower() if 0 < len(l) else '',
        'C': l[1].lower() if 1 < len(l) else '',
        'D': l[2].lower() if 2 < len(l) else '',
        'E': l[2].lower() if 3 < len(l) else '',
    }
    return payload

def save_to_googlesheets(payload):
    try:
        session = requests.session()
        r = requests.post(GOOGLE_SCRIPTS_URL, data=payload)
        return (r.json())
    except Exception as e:
        return (e)