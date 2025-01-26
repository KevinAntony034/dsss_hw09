from telegram import Update
from telegram.ext import Application, CommandHandler,CallbackContext, MessageHandler, filters, ContextTypes
from transformers import pipeline

TinyLlama = "PY007/TinyLlama-1.1B-Chat-v0.1" #TinyLlama LLM
pipe = pipeline(                             #Slide 02
    "text-generation",
    model=TinyLlama,     # Model
    torch_dtype="auto",  # Data Type
    device=0             # CPU
)

async def start(update: Update, context: CallbackContext) -> None:      #Send Message
    await update.message.reply_text("Hi! I am your AI assistant. How can I help you?")

async def process(update: Update, context: CallbackContext) -> None:   #Processing the user message
    user_Input = update.message.text                                   # Extract the user message
    print(f"User Message: {user_Input}")

    prompt = f"### Human: {user_Input}\n### Assistant:"                #Response
    response = pipe(
        prompt,
        do_sample=True,
        top_k=70,
        top_p=0.85,
        repetition_penalty=1.1,
        max_new_tokens=250,
    )

    reply = response[0]["generated_text"].split("### Assistant:")[-1].strip()      #Bot Response
    await update.message.reply_text(reply)

def main():
    API_TOKEN = "7567125441:AAE2AO_nsTnkrn6k882gvmSOMX_jwgEsX1I"                   #Api token
    applicationn = Application.builder().token(API_TOKEN).build()                  #starting the Bot
    applicationn.add_handler(CommandHandler("start", start))
    applicationn.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process))
    applicationn.run_polling()

if __name__ == "__main__":
    main()
