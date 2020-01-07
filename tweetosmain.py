import discord

tweetosClient = discord.Client()

@tweetosClient.event
async def on_ready():
    print('We have logged in as {0.user}'.format(tweetosClient))

@tweetosClient.event
async def on_message(message):
    if message.author == tweetosClient.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

tweetosClient.run('NjYzNzgxMTE2MjYzNjYxNTc5.XhNgaQ.zTnoAmiRPqxM89XLLQCOnfglHTE')