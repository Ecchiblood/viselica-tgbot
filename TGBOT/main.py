import telebot
from telebot import TeleBot
from newgame import MyGame

bot = telebot.TeleBot("7352457969:AAH16CMcufh5Vns2UlpBALpEDaRxYPTVaFI", parse_mode=None)
mg = MyGame()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, для того чтобы сыграть напиши слово \"Играть\"")

@bot.message_handler()
def on_message(message):
	if mg.game_toggle:
		if len(message.text) > 1:
			bot.send_message(message.chat.id, text="Введите одну букву!")
			return
		msg = mg.game_process(message.text.lower())
		bot.send_message(message.chat.id, text=msg)
		return
	if message.text == "Играть":
		mg.start()
		text = f"Привет, го играть. Угадай слово \n {mg.info()}"
		bot.send_message(message.chat.id, text=text)

if __name__ == '__main__':
	bot.polling(non_stop=True)