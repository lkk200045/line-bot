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
    elif query == "高雄" :
        a ='高雄'
        return a
    elif query == "正妹求搬家" :
        a ='正妹求搬家'
        return a
    elif query == "接小孩" :
        a ='接小孩'
        return a
    elif query == "中山跑腿小弟" :
        a ='中山跑腿小弟'
        return a
    elif query == "是" :
        a ='是'
        return a
    elif query == "否" :
        a ='否'
        return a
    elif query == '學生兼差' :
        a ='學生兼差'
        return a
    elif query == '上班族兼差' :
        a ='上班族兼差'
        return a
    elif query == '小明' :
        a ='小明'
        return a
    elif query == '0987787587' :
        a ='0987787587'
        return a

    elif query == '我要找人才' :
        a ='我要找人才'
        return a
    elif query == '高雄人才' :
        a ='高雄人才'
        return a
    elif query == '有' :
        a ='有'
        return a
    elif query == "台南林志玲":
        a ='台南林志玲'
        return a
    elif query == "高雄金城武":
        a ='高雄金城武'
        return a
    elif query == "中山劉德華":
        a ='中山劉德華'
        return a
    elif query == "沒有":
        a ='沒有'
        return a
    elif query == "幫忙接小孩":
        a ='幫忙接小孩'
        return a
    elif query == "中山大學":
        a ='中山大學'
        return a
    elif query == "阿伯":
        a ='阿伯'
        return a
    elif query == "阿伯":
        a ='阿伯'
        return a
    elif query == "0978787587":
        a ='0978787587'
        return a
    elif query == "客訴服務":
        a ='客訴服務'
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
                    title='以職務類別區分',
                    text='',
                    actions=[
                    MessageTemplateAction(
                        label='104歡迎您',
                        text='選擇職務類別區分'
                    )
                ]
            ),
                CarouselColumn(
                    thumbnail_image_url='https://rakumatw.r10s.com/d/strg/ctrl/27/1852d4cee0e9540099c5db2f1b99936027ffdac2.60.1.27.2.jpg',
                    title='以地區區分',
                    text='',
                    actions=[
                    MessageTemplateAction(
                        label='104歡迎您',
                        text='選擇地區'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://static.juksy.com/files/articles/68605/5a35353b09a3d.jpg',
                    title='以工作性質區分',
                    text='',
                    actions=[
                    MessageTemplateAction(
                        label='104歡迎您',
                        text='選擇工作性質'
                    )
                ]
            ),
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif a == "正妹求搬家" :
        Confirm_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='確認',
                text='您選的資料為正妹求搬家',
                actions=[                              
                PostbackTemplateAction(
                    label='是',
                    text='是',
                    data='action=buy&itemid=1'
                    ),
                MessageTemplateAction(
                    label='否',
                    text='否'
                    )
                ]
            )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)
    elif a == "接小孩" :
        Confirm_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='確認',
                text='您選的資料為接小孩',
                actions=[                              
                PostbackTemplateAction(
                    label='是',
                    text='是',
                    data='action=buy&itemid=1'
                    ),
                MessageTemplateAction(
                    label='否',
                    text='否'
                    )
                ]
            )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)
    elif a == "中山跑腿小弟" :
        Confirm_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='確認',
                text='您選的資料為中山跑腿小弟',
                actions=[                              
                PostbackTemplateAction(
                    label='是',
                    text='是',
                    data='action=buy&itemid=1'
                    ),
                MessageTemplateAction(
                    label='否',
                    text='否'
                    )
                ]
            )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)
    elif a == "是" :
        Confirm_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='確認',
                text='請選擇您的身分',
                actions=[                              
                PostbackTemplateAction(
                    label='學生兼差',
                    text='學生兼差',
                    data='action=buy&itemid=1'
                    ),
                MessageTemplateAction(
                    label='上班族兼差',
                    text='上班族兼差'
                    )
                ]
            )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)
    elif a == "否" :
        Confirm_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='確認',
                text='請選擇您的身分',
                actions=[                              
                PostbackTemplateAction(
                    label='學生兼差',
                    text='學生兼差',
                    data='action=buy&itemid=1'
                    ),
                MessageTemplateAction(
                    label='上班族兼差',
                    text='上班族兼差'
                    )
                ]
            )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)
    elif a == '學生兼差' or a == '上班族兼差':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入姓名'))
    elif a == '小明' :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入電話'))
    elif a == '0987787587' :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='報名成功 您的序號為001號'))
    elif a == "我要找人才":
        buttons_template_message = TemplateSendMessage(
            alt_text='hi',
            template=ButtonsTemplate(
                thumbnail_image_url='https://www.limitlessiq.com/media/catalog/product/cache/1/small_image/200x200/9df78eab33525d08d6e5fb8d27136e95/z/0/z01.jpg',
                title='請選擇所在城市',
                text='歡迎光臨',
                actions=[
                MessageTemplateAction(
                    label='高雄人才', text='高雄人才'
                    ),
                MessageTemplateAction(
                    label='台北人才', text='台北人才'
                    ),
                MessageTemplateAction(
                    label='台南人才', text='台南人才'
                    ),
                MessageTemplateAction(
                    label='台中人才', text='台中人才'
                    )
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            buttons_template_message)
    elif a == '高雄人才' :
        buttons_template_message = TemplateSendMessage(
            alt_text='hi',
            template=ButtonsTemplate(
                thumbnail_image_url='https://www.limitlessiq.com/media/catalog/product/cache/1/small_image/200x200/9df78eab33525d08d6e5fb8d27136e95/z/0/z01.jpg',
                title='請問有指定專員嗎?',
                text='您好',
                actions=[
                MessageTemplateAction(
                    label='有', text='有'
                    ),
                MessageTemplateAction(
                    label='沒有', text='沒有'
                    )
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            buttons_template_message)
    elif a == "有": 
        Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cc.tvbs.com.tw/img/upload/2018/08/26/20180826221834-d60f8573.jpg',
                    title='中山劉德華',
                    text='搬家界的第一把交椅',
                    actions=[
                    MessageTemplateAction(
                        label='中山劉德華',
                        text='中山劉德華'
                    )
                ]
            ),
                CarouselColumn(
                    thumbnail_image_url='https://cw1.tw/CW/images/article/C1418099648229.jpg',
                    title='高雄金城武',
                    text='外賣界的四大天王',
                    actions=[
                    MessageTemplateAction(
                        label='高雄金城武',
                        text='高雄金城武'
                    )
                ]
            ),
             CarouselColumn(
                    thumbnail_image_url='https://fs.mingpao.com/pns/20171215/s00092/5e98a17b98b881b7730d0d6b1e52a14b.jpg',
                    title='台南林志玲',
                    text='帶小孩的最美名模',
                    actions=[
                    MessageTemplateAction(
                        label='台南林志玲',
                        text='台南林志玲'
                    )
                ]
            ),
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif a == "台南林志玲" or a == "高雄金城武"or a == "中山劉德華" or a == "沒有":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入工作資訊'))
    elif a == "幫忙接小孩":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入地點'))
    elif a == "中山大學":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入姓名'))
    elif a == "阿伯":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入電話'))
    elif a == "0978787587":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='完成報名'))
    elif a == "客訴服務":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='您好，請輸入您的電話，我們將有專人為您服務。'))
    else :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='意圖:不明 回應:可以請你換句話說嗎?'))
       
if __name__ == "__main__":
    app.run()