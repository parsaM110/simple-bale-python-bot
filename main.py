import bale
bot = bale.Bot(token = "here_goes_your_token")
@bot.listen("on_message")
async def when_message(message: bale.Message):
     await message.reply(text="Salam! ")
bot.run()
