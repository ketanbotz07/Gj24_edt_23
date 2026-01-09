import os
from pyrogram import Client, filters
from utils.editor import advanced_edit

# Credentials
API_ID = int(os.environ.get("API_ID", "12345"))
API_HASH = os.environ.get("API_HASH", "your_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_token")

app = Client("movie_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video & filters.private)
async def handle_video(client, message):
    status = await message.reply("📥 Downloading...")
    file_path = await message.download()
    output_path = f"edited_{file_path}"

    await status.edit("✂️ Auto-Editing in progress (Zoom, Filter, Mirror)...")
    try:
        advanced_edit(file_path, output_path)
        await status.edit("📤 Uploading to Telegram...")
        await message.reply_video(output_path, caption="✅ Edited by Advanced AI Bot")
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")
    
    # Cleanup
    if os.path.exists(file_path): os.remove(file_path)
    if os.path.exists(output_path): os.remove(output_path)
    await status.delete()

print("Bot is running...")
app.run()
