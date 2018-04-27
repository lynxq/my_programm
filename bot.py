
import telebot
import constans

bot = telebot.TeleBot(constans.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
	user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
	user_markup.row('🤝 Обо мне', '📎 Ссылки', '📱 Мои девайсы')
	user_markup.row('🙏 Донат', '👀 Реклама', '❔ Помощь')
	bot.send_message(message.chat.id, "Привет! Что бы узнать о боте нажми \"Помощь\"", reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_message(message):
	if message.text == "🤝 Обо мне":
		bot.send_message(message.chat.id, """ 
🔷 Меня зовут 

🔧 Занимаюсь ремонтом смартфонов, планшетов, частично стационарных компьютеров и ноутбуков.

✏️ PHP, html. 

🏐 Играю в волейбол, 🎹 занимаюсь музыкой..
""")
	elif message.text == '📎 Ссылки':
		bot.send_message(message.chat.id, """ 
🔸 VK : soon

🔹 YouTube : soon

🔸 Telegram : soon

🔹 Telegram channel : soon

🔸 instagram : soon
""")
	elif message.text == '📱 Мои девайсы':
		bot.send_message(message.chat.id, """ 
🔸 🔥 Xiaomi Redmi 5 Plus ( Моё основное устройство ) 

🔹 🌚 Lenovo A536

🔸 🍀 LG K8



❇️ PC : 😓 Intel(R) Pentium(R) Dual CPU E2160 ( 1.80GHz ) 
❇️ PC : NVIDIA GeForce 8600 GT ( 512 MB ) 
❇️ PC : Mouse : A4Tech Bloody V3
❇️ PC : Keyboard : Genius KB-110 
❇️ PC : OS : 🖥 Win 10 / 🌱 Linux Mint / 🔏 Kali Linux
""")
#	bot.send_message(message.chat.id, )
	else:
		bot.send_message(message.chat.id, "Ошибка! :(")

bot.polling(none_stop=True, interval=0)
