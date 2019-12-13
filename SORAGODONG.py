import discord
import random

soragodong = ['a', 'b', 'c', 'd', 'e']
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("Ready!")
    game = discord.Game("D.R.I.N.K")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("잘남"):
        await message.channel.send("가만")


    if message.content.startswith("소라"):
        randomNum = random.randrange(1, 6)  # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(embed=discord.Embed(title="안 돼.", color=discord.Color.red()))
        if randomNum == 2:
            await message.channel.send(embed=discord.Embed(title="언젠가는.", color=discord.Color.gold()))
        if randomNum == 3:
            await message.channel.send(embed=discord.Embed(title="굶어.", color=discord.Color.red()))
        if randomNum == 4:
            await message.channel.send(embed=discord.Embed(title="그럼.", color=discord.Color.blue()))
        if randomNum == 5:
            await message.channel.send(embed=discord.Embed(title="다시 한 번 물어봐.", color=discord.Color.gold()))
        if randomNum == 6:
            await message.channel.send(embed=discord.Embed(title="그럼.", color=discord.Color.blue()))





    if message.content.startswith("마법"):
        randomNum = random.randrange(1, 6)  # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(embed=discord.Embed(title="안 돼.", color=discord.Color.red()))
        if randomNum == 2:
            await message.channel.send(embed=discord.Embed(title="언젠가는.", color=discord.Color.gold()))
        if randomNum == 3:
            await message.channel.send(embed=discord.Embed(title="굶어.", color=discord.Color.red()))
        if randomNum == 4:
            await message.channel.send(embed=discord.Embed(title="그럼.", color=discord.Color.blue()))
        if randomNum == 5:
            await message.channel.send(embed=discord.Embed(title="다시 한 번 물어봐.", color=discord.Color.gold()))
        if randomNum == 6:
            await message.channel.send(embed=discord.Embed(title="그럼.", color=discord.Color.blue()))






client.run("NjU0NjIxOTcwMDI1MDIxNDQx.XfIhpQ.FndnmdjtZbLG3nqTZBluqUxAdiQ")