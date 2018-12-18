from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import littleMaruDAO

app = Flask(__name__)
sec = littleMaruDAO.getToken()
# Channel Access Token
line_bot_api = LineBotApi('7QOb0ctgmnDIMgQn8f6xx5Sw8o/ubO7/2xad8HbcREROFTlmCTDQI87Y12nrTvXfwni4NfLyU5g6ZkmPMe7sRMjbbtXyg2wCHMVNKjf/vH7IR6GJrFyu8uMBuROMWJXWIJsbQQ51MIPFVoE2xqPUZwdB04t89/1O/w1cDnyilFU=')
#line_bot_api = LineBotApi(sec[0])
# Channel Secret
handler = WebhookHandler('624fcd094f053724f59922cc96747faa')
#handler = WebhookHandler(sec[1])

# listem on the income message /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Dealing with the messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    secM = TextSendMessage(text=sec[1])
    line_bot_api.reply_message(event.reply_token, message)
    line_bot_api.reply_message(event.reply_token, secM)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)