from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters


TG_TOKEN = '696207568:AAHuVMptUks7h_eQzSS62IiHWDFRrR2iBdY'


def message_handler(bot: Bot, update: Update):
    """
    Принимает сообщение от пользователя. Определяет его имя и отправляет сообщение обратно.
    """
    user = update.effective_user
    name = user.first_name if user else 'anonymous'

    text = update.effective_message.text
    reply_text = f'Hi, {name}!\n\n{text}'

    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )


def main():
    bot = Bot(token=TG_TOKEN, )
    updater = Updater(bot=bot)
    handler = MessageHandler(Filters.all, message_handler)

    updater.dispatcher.add_handler(handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
