import json
import telegram
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import sikdan_DF

TELEGRAM_TOKEN = '1403571731:AAEc89aHgshd0JANo81-PaZKvMOYcN0rEeg'
bot = telegram.Bot(token=TELEGRAM_TOKEN)


def index(request):
    return HttpResponse("Hello django")


@csrf_exempt
def webhook(request):
    json_string = request.body
    telegram_update = json.loads(json_string)  # dict type

    received_text = telegram_update["message"]["text"]

    if received_text == "식단":
        keyword_list = sikdan_DF.menu
        text = '\n'.join(keyword_list)

    chat_id = telegram_update["message"]["chat"]["id"]
    bot.sendMessage(chat_id=chat_id, text=text)

    return HttpResponse("OK")
