import telebot
import re

bot = telebot.TeleBot('6561490280:AAFLZgHFLsHEbJGCnBo17Yec5bFhJI35i1c')

numManuls = 0


@bot.message_handler(func=lambda message: True, content_types=['text'])
def reply_to_hello(message):
    global numManuls

    manulPattern = get_manul_pattern(message.text.lower())
    countPattern = get_count_pattern(message.text.lower())

    if countPattern:
        for i in range(int(countPattern[1])):
            bot.send_message(message.chat.id, "{} манулов".format(numManuls + 1))
            numManuls += 1

    if manulPattern:
        if int(manulPattern[0]) <= numManuls:
            bot.send_message(message.chat.id, "это число меньше или равно предыдущему. иди нахуй.")
            return
        if numManuls < 1:
            numManuls += 1
        else:
            numManuls += 2
        bot.send_message(message.chat.id, "{} манулов".format(numManuls + 1))

    if message.text.lower() == "манул":
        numManuls += 1
        bot.send_message(message.chat.id, "{} манулов".format(numManuls))


def get_manul_pattern(s):
    pattern = r"([0-9]*) ([а-я]*)"
    matches = re.search(pattern, s, re.IGNORECASE)

    if matches:
        number = matches.group(1)
        manul = matches.group(2)
        if manul == "манулов" or manul == "манул" or manul == "манула":
            return [number, manul]
        return 0
    else:
        return 0


def get_count_pattern(s):
    pattern = r"([а-яА-я]*) ([0-9]*) ([а-яА-я]*)"
    matches = re.search(pattern, s, re.IGNORECASE)

    if matches:
        check = matches.group(1)
        count = matches.group(2)
        manul = matches.group(3)

        if check.lower() == "отсчитай" and manul == "манулов" or "манул" or "манула":
            return [check, count, manul]
        return 0
    else:
        return 0


if __name__ == "__main__":
    bot.polling(none_stop=True)
