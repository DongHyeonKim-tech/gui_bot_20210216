# Polling 방식 (웹서비스에서는 webhook 방식)

# 텔레그램 모듈 import
import telegram
from pprint import pprint

# 토큰을 변수에 저장
TOKEN = '1403571731:AAEc89aHgshd0JANo81-PaZKvMOYcN0rEeg'

# 봇 선언
bot = telegram.Bot(token=TOKEN)
bot.set_webhook("https://guibot99.herokuapp.com/" + TOKEN)

# for update in bot.getUpdates():
#     received_text = update.message.text
#     if received_text == '안녕':
#         text = "나도 안녕"
#     else:
#         text = "뭐야"

#     chat_id = update.message.chat_id
#     bot.sendMessage(chat_id=chat_id, text=text)
