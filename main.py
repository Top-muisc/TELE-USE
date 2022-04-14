import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
dev = types.InlineKeyboardButton(text=f"- Owner 🤫",url="https://t.me/OYOYV")
start =types.InlineKeyboardButton(text=f"- Start ❤️‍🔥",callback_data="s")
user3 = types.InlineKeyboardButton(text=f"- User 3 💞️",callback_data="s3")
user4 =types.InlineKeyboardButton(text=f"- User 4 🔱",callback_data="s4")
user5 = types.InlineKeyboardButton(text=f"- User 5 🎸",callback_data="s5")
user6 = types.InlineKeyboardButton(text=f"- User 6 ☢️",callback_data="s6")
user7 = types.InlineKeyboardButton(text=f"- User 7 🛡️",callback_data="s7")
user8 = types.InlineKeyboardButton(text=f"- User Bot 🤫️",callback_data="s8")

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	key=types.InlineKeyboardMarkup()
	key.raw_width=1
	key.add(start)
	key.add(dev)
	hu = "https://t.me/yygguuii/2"
	name =message.chat.first_name
	bot.send_photo(message.chat.id,hu,f"""
────── • ✧✧ • ──────
‹ Hi {name} 
‹ Welcome Bot
‹ Hunt User Telegram
────── • ✧✧ • ──────""",reply_markup=key)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
	if call.data=="s3":
		st3(call.message)
	if call.data=="s":
		st(call.message)
	if call.data=="s4":
		st4(call.message)
	if call.data=="s5":
		st5(call.message)
	if call.data=="s6":
		st6(call.message)
	if call.data=="s7":
		st7(call.message)
	if call.data=="s8":
		st8(call.message)
def st8(message):
	ra = "ASDFGHJKLMNBVCXZQWERTYUIOP0987654321"
	a=0
	b=0
	chat_id = str(message.chat.id)
	start =  bot.send_message(message.chat.id,"- Hello "+message.chat.first_name)
	while True:
		ur = ''.join(random.choice(ra)for i in range(4))
		user = ur+"bot"
		req = requests.get(f"https://t.me/{user}").text
		if "tgme_username_link" in req:
			a+=1
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(dev)
			bot.send_message(message.chat.id,f"""
‹ New User Teleegram UserBot
────── • ✧✧ • ──────
‹ User : @{user} 
────── • ✧✧ • ──────""",reply_markup=key)
		else:
			b+=1
			u = types.InlineKeyboardButton(text=f"- Hit ✅ {a}️",callback_data="cnfnfb")
			uu = types.InlineKeyboardButton(text=f"- Bad ❌ {b}️",callback_data="cnfnfb")
			uuu = types.InlineKeyboardButton(text=f"- User 🔱 {user}️",callback_data="cnfnfb")
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(u)
			key.add(uu)
			key.add(uuu)
			name = message.chat.first_name
			result = f"""
────── • ✧✧ • ──────
‹ Hello {name} Please Wait... 
────── • ✧✧ • ──────"""
			bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id,reply_markup=key)
def st7(message):
	ra = "ASDFGHJKLMNBVCXZQWERTYUIOP0987654321"
	re = "ASDFGHJKLMNBVCXZQWERTYUIOP"
	a=0
	b=0
	chat_id = str(message.chat.id)
	start =  bot.send_message(message.chat.id,"- Hello "+message.chat.first_name)
	while True:
		ran = ''.join(random.choice(ra)for i in range(1))
		ran2 = ''.join(random.choice(re)for i in range(1))
		ran3 = ''.join(random.choice(ra)for i in range(1))
		ran4 = ''.join(random.choice(ra)for i in range(1))
		ran5 = ''.join(random.choice(ra)for i in range(1))
		user = ran2+ran2+ran2+ran2+ran3+ran4+ran2
		req = requests.get(f"https://t.me/{user}").text
		if "tgme_username_link" in req:
			a+=1
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(dev)
			bot.send_message(message.chat.id,f"""
‹ New User Teleegram User7
────── • ✧✧ • ──────
‹ User : @{user} 
────── • ✧✧ • ──────""",reply_markup=key)
		else:
			b+=1
			u = types.InlineKeyboardButton(text=f"- Hit ✅ {a}️",callback_data="cnfnfb")
			uu = types.InlineKeyboardButton(text=f"- Bad ❌ {b}️",callback_data="cnfnfb")
			uuu = types.InlineKeyboardButton(text=f"- User 🔱 {user}️",callback_data="cnfnfb")
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(u)
			key.add(uu)
			key.add(uuu)
			name = message.chat.first_name
			result = f"""
────── • ✧✧ • ──────
‹ Hello {name} Please Wait... 
────── • ✧✧ • ──────"""
			bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id,reply_markup=key)
def st6(message):
	ra = "ASDFGHJKLMNBVCXZQWERTYUIOP0987654321"
	re = "ASDFGHJKLMNBVCXZQWERTYUIOP"
	a=0
	b=0
	chat_id = str(message.chat.id)
	start =  bot.send_message(message.chat.id,"- Hello "+message.chat.first_name)
	while True:
		ran = ''.join(random.choice(ra)for i in range(1))
		ran2 = ''.join(random.choice(re)for i in range(1))
		ran3 = ''.join(random.choice(ra)for i in range(1))
		ran4 = ''.join(random.choice(ra)for i in range(1))
		ran5 = ''.join(random.choice(ra)for i in range(1))
		user = ran2+ran2+ran2+ran2+ran3+ran4
		req = requests.get(f"https://t.me/{user}").text
		if "tgme_username_link" in req:
			a+=1
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(dev)
			bot.send_message(message.chat.id,f"""
‹ New User Teleegram User6
────── • ✧✧ • ──────
‹ User : @{user} 
────── • ✧✧ • ──────""",reply_markup=key)
		else:
			b+=1
			u = types.InlineKeyboardButton(text=f"- Hit ✅ {a}️",callback_data="cnfnfb")
			uu = types.InlineKeyboardButton(text=f"- Bad ❌ {b}️",callback_data="cnfnfb")
			uuu = types.InlineKeyboardButton(text=f"- User 🔱 {user}️",callback_data="cnfnfb")
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(u)
			key.add(uu)
			key.add(uuu)
			name = message.chat.first_name
			result = f"""
────── • ✧✧ • ──────
‹ Hello {name} Please Wait... 
────── • ✧✧ • ──────"""
			bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id,reply_markup=key)
def st5(message):
	ra = "ASDFGHJKLMNBVCXZQWERTYUIOP0987654321"
	re = "ASDFGHJKLMNBVCXZQWERTYUIOP"
	a=0
	b=0
	chat_id = str(message.chat.id)
	start =  bot.send_message(message.chat.id,"- Hello "+message.chat.first_name)
	while True:
		ran = ''.join(random.choice(ra)for i in range(1))
		ran2 = ''.join(random.choice(re)for i in range(1))
		ran3 = ''.join(random.choice(ra)for i in range(1))
		ran4 = ''.join(random.choice(ra)for i in range(1))
		user = ran4+ran2+ran2+ran2+ran4
		user2 = ran3+ran3+ran2+ran3+ran3
		user3 = ran3+ran2+ran2+ran2+ran2
		user3 = ran3+ran2+ran3+ran3+ran3
		
		req = requests.get(f"https://t.me/{user}").text
		if "tgme_username_link" in req:
			a+=1
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(dev)
			bot.send_message(message.chat.id,f"""
‹ New User Teleegram User4
────── • ✧✧ • ──────
‹ User : @{user} 
────── • ✧✧ • ──────""",reply_markup=key)
		else:
			b+=1
			u = types.InlineKeyboardButton(text=f"- Hit ✅ {a}️",callback_data="cnfnfb")
			uu = types.InlineKeyboardButton(text=f"- Bad ❌ {b}️",callback_data="cnfnfb")
			uuu = types.InlineKeyboardButton(text=f"- User 🔱 {user}️",callback_data="cnfnfb")
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(u)
			key.add(uu)
			key.add(uuu)
			name = message.chat.first_name
			result = f"""
────── • ✧✧ • ──────
‹ Hello {name} Please Wait... 
────── • ✧✧ • ──────"""
			bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id,reply_markup=key)
def st4(message):
	ra = "ASDFGHJKLMNBVCXZQWERTYUIOP0987654321"
	re = "ASDFGHJKLMNBVCXZQWERTYUIOP"
	a=0
	b=0
	chat_id = str(message.chat.id)
	start =  bot.send_message(message.chat.id,"- Hello "+message.chat.first_name)
	while True:
		ran = ''.join(random.choice(ra)for i in range(1))
		ran2 = ''.join(random.choice(re)for i in range(1))
		ran3 = ''.join(random.choice(ra)for i in range(1))
		ran4 = ''.join(random.choice(ra)for i in range(1))
		user = ran2+'_'+ran2+'_'+ran2+'_'+ran
		req = requests.get(f"https://t.me/{user}").text
		if "tgme_username_link" in req:
			a+=1
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(dev)
			bot.send_message(message.chat.id,f"""
‹ New User Teleegram User4
────── • ✧✧ • ──────
‹ User : @{user} 
────── • ✧✧ • ──────""",reply_markup=key)
		else:
			b+=1
			u = types.InlineKeyboardButton(text=f"- Hit ✅ {a}️",callback_data="cnfnfb")
			uu = types.InlineKeyboardButton(text=f"- Bad ❌ {b}️",callback_data="cnfnfb")
			uuu = types.InlineKeyboardButton(text=f"- User 🔱 {user}️",callback_data="cnfnfb")
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(u)
			key.add(uu)
			key.add(uuu)
			name = message.chat.first_name
			result = f"""
────── • ✧✧ • ──────
‹ Hello {name} Please Wait... 
────── • ✧✧ • ──────"""
			bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id,reply_markup=key)
def st3(message):
	ra = "ASDFGHJKLMNBVCXZQWERTYUIOP0987654321"
	re = "ASDFGHJKLMNBVCXZQWERTYUIOP"
	a=0
	b=0
	chat_id = str(message.chat.id)
	start =  bot.send_message(message.chat.id,"- Hello "+message.chat.first_name)
	while True:
		ran = ''.join(random.choice(ra)for i in range(1))
		ran2 = ''.join(random.choice(re)for i in range(1))
		ran3 = ''.join(random.choice(ra)for i in range(1))
		user = ran2+'_'+ran3+'_'+ran
		req = requests.get(f"https://t.me/{user}").text
		if "tgme_username_link" in req:
			a+=1
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(dev)
			bot.send_message(message.chat.id,f"""
‹ New User Teleegram User3
────── • ✧✧ • ──────
‹ User : @{user} 
────── • ✧✧ • ──────""",reply_markup=key)
		else:
			b+=1
			u = types.InlineKeyboardButton(text=f"- Hit ✅ {a}️",callback_data="cnfnfb")
			uu = types.InlineKeyboardButton(text=f"- Bad ❌ {b}️",callback_data="cnfnfb")
			uuu = types.InlineKeyboardButton(text=f"- User 🔱 {user}️",callback_data="cnfnfb")
			key=types.InlineKeyboardMarkup()
			key.raw_width=1
			key.add(u)
			key.add(uu)
			key.add(uuu)
			name = message.chat.first_name
			result = f"""
────── • ✧✧ • ──────
‹ Hello {name} Please Wait... 
────── • ✧✧ • ──────"""
			bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id,reply_markup=key)

def st(message):
	ur = "https://t.me/yygguuii/2"
	key=types.InlineKeyboardMarkup()
	key.raw_width=1
	key.add(user3)
	key.add(user4)
	key.add(user5)
	key.add(user6)
	key.add(user7)
	key.add(user8)
	bot.send_photo(message.chat.id,ur,f"""
────── • ✧✧ • ──────
‹ Choice 🛡️
‹ User4 🔱
‹ User5 🎸
‹ User6 ☢️
‹ User7 🛡️
‹ User3 💞
‹ UserBot 🤫
────── • ✧✧ • ──────""",reply_markup=key)
bot.polling(True)
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
