from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, ContextTypes, filters

async def start(update: Update, context: CallbackContext) -> None:
    user_Input = update.message.text    #Input  
    chat_id = update.effective_chat.id  #ID

    print(f"Received message: {user_Input} from chat ID: {chat_id}")       #Log message

    response_message = f"Hello! You said: {user_Input}"                    #Response
    await context.bot.send_message(chat_id=chat_id, text=response_message) #ID

async def process(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hi! I am your AI assistant. How can I help you?") #Processing

def main() -> None:
    API_TOKEN = "Api token here" #Api Token
    applicationn = Application.builder().token(API_TOKEN).build() 
    applicationn.add_handler(CommandHandler("start", process))
    applicationn.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))

    print("Bot is operational...")
    applicationn.run_polling()

if __name__ == "__main__":
    main()
