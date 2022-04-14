import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
import telebot,time
from telebot import types 
import requests
#-----------------color-----------------#
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
#-----------------color-----------------#
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
  h = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text = "DOWNLOAD", callback_data= "click1")
  button2 = types.InlineKeyboardButton(text = "- DEV", url= "t.me/HarithTools")
  h.add(button1, button2)
  bot.reply_to(message, text="""<strong>⌔ Hello Pro :
⌔ Bot Download TikTok  
⌔ Ch : @Lis_5_t
⌔ Program Bot : Haider
</strong>  """, reply_markup=h, parse_mode="html")
@bot.callback_query_handler(func=lambda call: True)
def callback_date(call):
    time.sleep(1)
    if call.data == "click1":
      bot.send_message(call.message.chat.id, text = "* Hi Please Send Me Url : *", parse_mode="markdown")
@bot.message_handler(func=lambda m:True)
def content(message):
	d = message.text    
	bot.send_message(message.chat.id,"* Wait a little while the video is ready *", parse_mode="markdown")
	api = requests.get(f"https://kabospythonanywhere.nhnh7.repl.co/api/tik?url={d}").json()['url']
	bot.send_message(message.chat.id,api)
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://sidrabot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
