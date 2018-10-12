#SDK 載入LINE SDK
import requests

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)





app = Flask(__name__)

line_bot_api = LineBotApi('/sjBLgjHsNZhdsV+Xy9pXu7rPIrErYLvvbLfVOEYDyaiH3IEVROEnEYrMkPF+BuGCFjbTu3HSfTSUfVTJz6rLIWluhYeZp7v5FKZa94SF7pkcCPvY7El21pJuki1kpg5gl8QLxtGEfhtSutfmxdgUgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ba4bdf20d14b1338b998a01491aa691f')


headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '5cf8bae594b24645bc0971c7b1169ed9',
}

params ={
    # Query parameter
    'q': '我愛你',
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

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
def work(message):
    if '找工作' in message:
        s = '請輸入時間'
        return s
    elif message == '時':
        s = '請選擇地點'
        return s
    elif message == '中山大學':
        s = '請選擇工資'
        return s
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    params['q'] = msg
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d9f3feb1-6cf3-4f39-8821-e6c2bbb86fc6',headers=headers, params=params)
    result = r.json()
    a = result['topScoringIntent']['intent']
    if '找工作' or '時' or '中山大學' in msg:
        s = work(msg)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=s))
    
    elif msg == 'a':
        buttons_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ButtonsTemplate(
            title='Template-樣板介紹',
            text='Template分為四種，也就是以下四種：',
            thumbnail_image_url='https://i.imgur.com/kzi5kKy.jpg',
            actions=[
                MessageTemplateAction(
                    label='Buttons Template',
                    text='Buttons Template'
                ),
                MessageTemplateAction(
                    label='Confirm template',
                    text='Confirm template'
                ),
                MessageTemplateAction(
                    label='Carousel template',
                    text='Carousel template'
                ),
                MessageTemplateAction(
                    label='Image Carousel',
                    text='Image Carousel'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)


if __name__ == "__main__":
    app.run()