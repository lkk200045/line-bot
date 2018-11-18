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