import discord
import responses as responses
import json
from dotenv import dotenv_values

json_path='config/config.json'
async def send_message(message: discord.Message, is_private: bool):
    # user_message = await message.channel.send(user_message)
    try:
        response, reactions = responses.handle_response(message)
        
        if response != None:
            await message.channel.send(response)
        if reactions != None:
            for reaction in reactions:
                await message.add_reaction(reaction) 

        
        # if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = dotenv_values("config/.env")['TOKEN']
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # get prefix from config.json
        with open(json_path, 'r') as file:
           data = json.load(file)
        prefix = data['prefix']
        file.close()
        
        if message.author == client.user:
            return
        
        if not message.content.startswith(prefix):
            return
        
        if message.author.bot:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)     
        print(f"{username} said: '{user_message}' ({channel})")
        
        # if user_message[0] == '?':          #sends private message if command is '?
        #     user_message = user_message[1:]
        #     await send_message(message, user_message, is_private=True)
        # else:
        
        await send_message(message, is_private=False)

    client.run(TOKEN)