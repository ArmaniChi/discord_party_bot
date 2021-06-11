from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_reaction_add(reaction, user):
    print("Reaction Detected: " + str(reaction) + "by" + str(user)) # Prints to console
    if reaction.message.author.id == bot.user.id: # only responds if the reaction is on the message by the bot
        channel = reaction.message.channel 
        await channel.send(f'{user.name} has added {reaction.emoji} to the message: {reaction.message.content}')
        print(reaction.emoji)
    else:
        print("This is not the bot's message")

@bot.command(name='party', help='Takes 2 args -> !party Eg. 8:00 15:00 denotes a 7 hour time window')
async def party(ctx, start_time, end_time):
    await ctx.send(f'Hanging out starts at {start_time} and ends at {end_time}')

@bot.command(name='timelist')
async def timelist(ctx, *args):
    list_of_args = list(args)
    await ctx.send(list_of_args)

# @bot.event
# async def on_message(message):
#     print(message.content)
#     await message.channel.send("Hi")

# @bot.command(name='getreaction', pass_context=True)
# async def checkreacts(ctx):
#     msg1 = await ctx.send("React to me!")
#     await ctx.send("You responded with {}".format(reaction.emoji))

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)