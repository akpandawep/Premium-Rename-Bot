from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    bot_get = await client.get_me()
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Share Your Link" ,url=f"https://t.me/share/url?url=https://t.me/{bot_get.username}?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Refer And Earn Get premium\nPer Refer premium\n Your Link :- https://t.me/{bot_get.username}?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
