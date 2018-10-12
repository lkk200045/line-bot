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
    MessageEvent, TextMessage, TextSendMessage,
    ImageSendMessage,LocationMessage,TemplateSendMessage, ButtonsTemplate, URITemplateAction,
    PostbackTemplateAction, MessageTemplateAction
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
    msg = msg.encode('utf-8')
    if event.message.text == "文字":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
    elif event.message.text == '找工作':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入時間'))
    elif event.message.text == "按鈕":
        buttons_template_message = TemplateSendMessage(
            alt_text="Please tell me where you are",
            template=ButtonsTemplate(
                text="Please tell me where you are",
                actions=[
                URITemplateAction(
                    label="Send my location",
                    uri="line://nv/location"
                    )
                ]
            )
            )
        line_bot_api.reply_message(
            event.reply_token,
            buttons_template_message)
    
    elif event.message.text == "樣本":
        buttons_template_message = TemplateSendMessage(
            alt_text='hi',
            template=ButtonsTemplate(
                thumbnail_image_url='https://rakumatw.r10s.com/d/strg/ctrl/27/1852d4cee0e9540099c5db2f1b99936027ffdac2.60.1.27.2.jpg',
                title='hi',
                text='aa',
                actions=[
                URITemplateAction(
                    label='查看南瓜地圖',
                    uri="line://nv/location"
                    ),
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            buttons_template_message)

    elif event.message.text =='測試'
        button_template_message =ButtonsTemplate(
            thumbnail_image_url="https://rakumatw.r10s.com/d/strg/ctrl/27/1852d4cee0e9540099c5db2f1b99936027ffdac2.60.1.27.2.jpg",
            title='Menu', 
            text='Please select',
            ratio="1.51:1",
            image_size="cover",
            actions=[
            PostbackTemplateAction(
                label='postback還會回傳data參數', 
                text='postback text',
                data='action=buy&itemid=1'
                ),
            MessageTemplateAction(
                label='message會回傳text文字', text='message text'
                ),
            URITemplateAction(
                label='uri可回傳網址', uri='http://www.xiaosean.website/'
                )
            ]
        )
        line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

if __name__ == "__main__":
    app.run()