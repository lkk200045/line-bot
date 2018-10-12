#座標範例    
    event.message.text == "按鈕":
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