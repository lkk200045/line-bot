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
    PostbackTemplateAction, MessageTemplateAction, CarouselTemplate, CarouselColumn, ConfirmTemplate
)


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


app = Flask(__name__)

line_bot_api = LineBotApi('/sjBLgjHsNZhdsV+Xy9pXu7rPIrErYLvvbLfVOEYDyaiH3IEVROEnEYrMkPF+BuGCFjbTu3HSfTSUfVTJz6rLIWluhYeZp7v5FKZa94SF7pkcCPvY7El21pJuki1kpg5gl8QLxtGEfhtSutfmxdgUgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ba4bdf20d14b1338b998a01491aa691f')


headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '5cf8bae594b24645bc0971c7b1169ed9',
}

def luis(query):
    params['q'] = query
    if query == "我要找工作":
        a ='我要找工作'
        return a
    elif query == '我要找人才' :
        a ='我要找人才'
        return a
    else :
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d9f3feb1-6cf3-4f39-8821-e6c2bbb86fc6',headers=headers, params=params)
        result = r.json()
        a = result['topScoringIntent']['intent']
        return a     

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    a = luis(event.message.text)
    if a =='告白':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:告白 回應:我不愛妳'))
    elif a=='聊天':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:聊天 回應:我不想聊天'))
    elif a=='例外':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:例外 回應:我聽不懂耶'))
    elif a=='詢問':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:詢問 回應:歡迎光臨'))
    elif a=='誇獎':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:誇獎 回應:我會不好意思耶'))
    elif a=='問候':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:問候 回應:你好喔'))
    elif a == "我要找工作" :
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.104.com.tw/jobs/main/static/img/fb_600x315.png',
                    title='以職務類型區分',
                    text='您好，歡迎光臨',
                    actions=[
                    MessageTemplateAction(
                        label='104人力銀行',
                        text='選擇職務類型'
                    )
                ]
            ),
                CarouselColumn(
                    thumbnail_image_url='https://rakumatw.r10s.com/d/strg/ctrl/27/1852d4cee0e9540099c5db2f1b99936027ffdac2.60.1.27.2.jpg',
                    title='接小孩',
                    text='幫忙接小孩，詳細地點鹽埕區五福四路100號，時薪200',
                    actions=[
                    MessageTemplateAction(
                        label='接小孩',
                        text='接小孩'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://static.juksy.com/files/articles/68605/5a35353b09a3d.jpg',
                    title='正妹求搬家',
                    text='幫忙搬家，詳細地點鹽埕區五福四路1號，友情無價，陪你吃頓飯',
                    actions=[
                    MessageTemplateAction(
                        label='正妹求搬家',
                        text='正妹求搬家'
                    )
                ]
            ),
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    else :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:不明 回應:可以請你換句話說嗎?'))
       
if __name__ == "__main__":
    app.run()