import discord
import random
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print('준비 됨.')

class MyClient(discord.Client):

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('ㅗ'):
            await message.reply('ㅗ', mention_author=True)
        if message.content.startswith('개새끼'):
            await message.reply('뭐 이새끼야', mention_author=True)




        if message.content.startswith('소라'):

            randomNum = random.randrange(1, 6)  # 1~6까지 랜덤수
            print(randomNum)
            if randomNum == 1:
                await message.reply('안돼', mention_author=True)
            if randomNum == 2:
                await message.reply('그래', mention_author=True)
            if randomNum == 3:
                await message.reply('굶어', mention_author=True)
            if randomNum == 4:
                await message.reply('응', mention_author=True)
            if randomNum == 5:
                await message.reply('기다려', mention_author=True)
            if randomNum == 6:
                await message.reply('다시 한번 물어봐', mention_author=True)



        if message.content.startswith('마법'):

            randomNum = random.randrange(1, 6)
            print(randomNum)
            if randomNum == 1:
                await message.reply('안돼', mention_author=True)
            if randomNum == 2:
                await message.reply('그럼', mention_author=True)
            if randomNum == 3:
                await message.reply('굶어', mention_author=True)
            if randomNum == 4:
                await message.reply('어, 그래', mention_author=True)
            if randomNum == 5:
                await message.reply('기다려', mention_author=True)
            if randomNum == 6:
                await message.reply('다시 한번 물어봐', mention_author=True)

client = MyClient()
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
