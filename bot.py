from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2


def welcome(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = 'Olá, ' + firstName + '!'
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))

def pergunte(update, context):
    try:
        message = '''Em que posso ajudar? \n 1 - setor de cobrança \n 2 - setor financeiro'''
        update.message.reply_text(
            message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
        return STATE1
    except Exception as e:
        print(str(e))

def inputPergunte(update, context):
    pergunte = (update.message.text).lower()
    print(pergunte)
    if (pergunte == '1'
        or pergunte == 'cobrança'
            or pergunte == 'setor de cobrança'):
        message = """Contrato... 
                        \n Divida
                        \n Negociação"""
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (pergunte == '2'
          or pergunte == 'financeiro'
          or pergunte == 'setor financeiro'):
        message = """Boleto... 
                        \n Debito
                        \n Credito"""
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
        return STATE2


def inputResposta(update, context):
    message = "Muito obrigado, logo lhe daremos retorno"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def cancel(update, context):
    return ConversationHandler.END


def main():
    token = '1337767378:AAFLwJJVPfmSP16UVc2TJ4MZXaLOLiQa1A0'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('pergunte', pergunte)],
        states={
            STATE1: [MessageHandler(Filters.text, inputPergunte)],
            STATE2: [MessageHandler(Filters.text, inputResposta)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    print('oi, eu sou o updater' + str(updater))
    updater.idle()


if __name__ == '__main__':
    main()
