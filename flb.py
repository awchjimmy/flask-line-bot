import os
from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage,
)
import bible

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

@app.route("/")
def hello():
	return "Hello World!"

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
	user_input = event.message.text
	reply_text = ''

	# starts with one space, query bible, e.g. ' {book} {chapter}'
	if user_input[0] == ' ':
		_, book, chapter = user_input.split(' ')
		reply_text = bible.query(book, int(chapter))

	# normal user input
	else:
		reply_text = user_input

	# send reply message
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=reply_text))

