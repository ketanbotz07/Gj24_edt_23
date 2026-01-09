import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from editor import advanced_edit

TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Mujhe video bhejo, main use auto-edit karke YouTube ready bana dunga.")

def process_video(update: Update, context: CallbackContext):
    message = update.message
    video = message.video or message.document
    
    if not video:
        return

    msg = message.reply_text("Downloading video... ⏳")
    file = context.bot.get_file(video.file_id)
    input_file = "input.mp4"
    output_file = "output_ready.mp4"
    file.download(input_file)
    
    msg.edit_text("Applying Advanced Editing (2s cuts, zoom, filters)... 🛠️")
    try:
        advanced_edit(input_file, output_file)
        msg.edit_text("Uploading edited video... 📤")
        with open(output_file, 'rb') as v:
            message.reply_video(v, caption="✅ Edited by Advanced Bot\n\nNote: Use your voiceover for better safety.")
    except Exception as e:
        message.reply_text(f"Error: {str(e)}")
    
    # Cleaning up files
    if os.path.exists(input_file): os.remove(input_file)
    if os.path.exists(output_file): os.remove(output_file)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.video | Filters.document.mime_type("video/mp4"), process_video))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
