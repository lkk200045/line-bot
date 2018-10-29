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





app = Flask(__name__)

line_bot_api = LineBotApi('/sjBLgjHsNZhdsV+Xy9pXu7rPIrErYLvvbLfVOEYDyaiH3IEVROEnEYrMkPF+BuGCFjbTu3HSfTSUfVTJz6rLIWluhYeZp7v5FKZa94SF7pkcCPvY7El21pJuki1kpg5gl8QLxtGEfhtSutfmxdgUgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ba4bdf20d14b1338b998a01491aa691f')


headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '5cf8bae594b24645bc0971c7b1169ed9',
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    msg = msg.encode('utf-8')
    with open("products.csv",'w',encoding='utf-8') as f :
        f.write(msg)
    if event.message.text == "我要找工作":
        buttons_template_message = TemplateSendMessage(
            alt_text='hi',
            template=ButtonsTemplate(
                thumbnail_image_url='https://www.limitlessiq.com/media/catalog/product/cache/1/small_image/200x200/9df78eab33525d08d6e5fb8d27136e95/z/0/z01.jpg',
                title='請選擇所在城市',
                text='歡迎光臨',
                actions=[
                MessageTemplateAction(
                    label='高雄', text='高雄'
                    ),
                MessageTemplateAction(
                    label='台北', text='台北'
                    ),
                MessageTemplateAction(
                    label='台南', text='台南'
                    ),
                MessageTemplateAction(
                    label='台中', text='台中'
                    )
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
                        label='中山跑腿小弟',
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
                        label='鹽程幫忙掃地',
                        text='鹽程幫忙掃地'
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

    elif event.message.text == "正妹求搬家" :
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

    elif event.message.text == '是':
        buttons_template_message = TemplateSendMessage(
            alt_text='hi',
            template=ButtonsTemplate(
                thumbnail_image_url='https://www.limitlessiq.com/media/catalog/product/cache/1/small_image/200x200/9df78eab33525d08d6e5fb8d27136e95/z/0/z01.jpg',
                title='請選擇身分',
                text='您好',
                actions=[
                MessageTemplateAction(
                    label='學生兼差', text='學生兼差'
                    ),
                MessageTemplateAction(
                    label='上班族兼差', text='上班族兼差'
                    )
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            buttons_template_message)
        
    elif event.message.text == '學生兼差':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入姓名'))

    elif event.message.text == "我要找人才":
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

    
    elif event.message.text == '高雄人才':
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


    elif event.message.text == "有": 
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

    elif event.message.text == "台南林志玲":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入地址及相關資訊'))


    elif event.message.text == "沒有": 
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


        
if __name__ == "__main__":
    app.run()