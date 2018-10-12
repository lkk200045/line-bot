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
    PostbackTemplateAction, MessageTemplateAction, CarouselTemplate, CarouselColumn,DatetimePickerTemplateAction
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

    if event.message.text == "找工作":
        buttons_template_message = TemplateSendMessage(
            alt_text='hi',
            template=ButtonsTemplate(
                thumbnail_image_url='https://photos.google.com/photo/AF1QipN6ssz4Ewsiik3Ef-R0tzzSOKjlqlf6y4LFLJgf',
                title='請選擇所在城市',
                text='歡迎光臨',
                actions=[
                MessageTemplateAction(
                    label='高雄', text='高雄'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            buttons_template_message)
   
    elif event.message.text == "高雄":
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                CarouselColumn(
                    thumbnail_image_url='https://rakumatw.r10s.com/d/strg/ctrl/27/1852d4cee0e9540099c5db2f1b99936027ffdac2.60.1.27.2.jpg',
                    title='中山跑腿小弟',
                    text='幫忙外送飲料，詳細地點高雄中山大學，時薪200',
                    actions=[
                    MessageTemplateAction(
                        label='message1',
                        text='中山跑腿小弟'
                    )
                ]
            ),
                CarouselColumn(
                    thumbnail_image_url='https://rakumatw.r10s.com/d/strg/ctrl/27/1852d4cee0e9540099c5db2f1b99936027ffdac2.60.1.27.2.jpg',
                    title='鹽程幫忙掃地',
                    text='幫忙打掃宿舍，詳細地點鹽埕區五福四路100號，時薪200',
                    actions=[
                    MessageTemplateAction(
                        label='message2',
                        text='鹽程幫忙掃地'
                    )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)      
        
if __name__ == "__main__":
    app.run()