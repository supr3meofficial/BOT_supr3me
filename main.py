import discord
from discord.ext import commands
import asyncio
import datetime
import sys
import traceback
import os
import math

def get_prefix(bot, message):
	"""Bot prefixes"""

	prefixes = ['++','+']

	# Check to see if we are outside of a guild. e.g DM's etc.
	if not message.guild:
	
		pass

	# If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
	return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in.
initial_extensions = ['cogs.general',
					  'cogs.owner',
					  'cogs.help',
					  'cogs.games',
					  'cogs.misc',
					  'cogs.caseopening',
					  'cogs.hltvcog'
					  ]

bot = commands.Bot(command_prefix=get_prefix, description='BOT supr3me')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print(f'Failed to load extension {extension}.', file=sys.stderr)
			traceback.print_exc()

@bot.event
async def on_message(message):

	if not message.guild:
		pass
	else:
		if message.guild.id == 331892870367805440:
			guild = message.guild
			member = message.author
			channel = message.channel

			if "sausage" in message.content.lower():

				await message.add_reaction("👀")
				sausagerole = discord.utils.get(guild.roles, id=401875611141931008)
				await member.add_roles(sausagerole)

			if message.content == "i play csgo":

				rolecsgo = discord.utils.get(guild.roles, id=384112406663528448)
				await member.add_roles(rolecsgo)
				await channel.send(":white_check_mark: │ Your role has been added!")

			if message.content == "i play pubg":

				rolepubg = discord.utils.get(guild.roles, id=384112588113313793)
				await member.add_roles(rolepubg)
				await channel.send(":white_check_mark: │ Your role has been added!")

			if message.content == "i play lol":

				rolelol = discord.utils.get(guild.roles, id=384112673853276161)
				await member.add_roles(rolelol)
				await channel.send(":white_check_mark: │ Your role has been added!")

			if message.content == "i play overwatch":

				roleoverwatch = discord.utils.get(guild.roles, id=401359547127693313)
				await member.add_roles(roleoverwatch)
				await channel.send(":white_check_mark: │ Your role has been added!")

			if message.content == "i play fortnite":

				rolefortnite = discord.utils.get(guild.roles, id=422142121630498816)
				await member.add_roles(rolefortnite)
				await channel.send(":white_check_mark: │ Your role has been added!")

		msg = message.content
		if "hmm" in msg:
			await message.add_reaction("🤔")
		elif "HMM" in msg:
			e = bot.get_emoji(437667802149683200,)
			await message.add_reaction(e)

	await bot.process_commands(message)

@bot.event
async def on_member_update(before, after):
# The Panther Lounge Automatic Role Assignment

	guild = bot.get_guild(id=331892870367805440)

	try:
		if str(after.activity) == "Counter-Strike Global Offensive":
			rolecsgo = discord.utils.get(guild.roles, id=384112406663528448)
			await after.add_roles(rolecsgo)

		if str(after.activity) == "Fortnite":
			rolefortnite = discord.utils.get(guild.roles, id=422142121630498816)
			await after.add_roles(rolefortnite)

		if str(after.activity) == "Overwatch":
			roleoverwatch = discord.utils.get(guild.roles, id=401359547127693313)
			await after.add_roles(roleoverwatch)

		if str(after.activity) == "League of Legends":
			rolelol = discord.utils.get(guild.roles, id=384112673853276161)
			await after.add_roles(rolelol)

		if str(after.activity) == "PLAYERUNKOWN'S BATTLEGROUNDS":
			rolepubg = discord.utils.get(guild.roles, id=384112588113313793)
			await after.add_roles(rolepubg)
            
	except (discord.Forbidden, discord.NotFound):
		pass
    
@bot.event
async def on_command_error(ctx, error):
    # Return in local command handler
    if hasattr(ctx.command, 'on_error'):
        return

    # Get the original exception
    error = getattr(error, 'original', error)

    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.BotMissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)
        _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
        embed = discord.Embed(title="No permissions",
		description=_message,
		colour=0xbf0000)
        embed.set_author(icon_url=bot.user.avatar_url, name=bot.user.name)
        await ctx.send(embed=embed)
        return

    if isinstance(error, commands.DisabledCommand):
        await ctx.send('This command has been disabled.')
        return

    if isinstance(error, commands.CommandOnCooldown):
        msg="This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after))
        embed = discord.Embed(title="Cooling Down",
        description=msg,
        colour=0xbf0000)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        await ctx.send(embed=embed)
        return

    if isinstance(error, commands.MissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)
        _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)
        embed = discord.Embed(title="No permissions",
		description=_message,
		colour=0xbf0000)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        await ctx.send(embed=embed)
        return
	
    if isinstance(error, discord.Forbidden):
        embed = discord.Embed(title="No permissions",
        description="You do not have permission to perform this command",
        colour=0xbf0000)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        await ctx.send(embed=embed)

    if isinstance(error, commands.UserInputError):
        embed = discord.Embed(title="Invalid input",
				description="Please re-check your command and try again",
				colour=0xbf0000)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author.name)
        await ctx.send(embed=embed)
        return

    if isinstance(error, commands.NoPrivateMessage):
        try:
            await ctx.author.send('This command cannot be used in direct messages.')
        except discord.Forbidden:
            pass
        return

    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title="Invalid input",
				description="You do not have permission to use this command.",
				colour=0xbf0000)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author.name)
        await ctx.send(embed=embed)
        return

    # Ignore all other exception types, but print them to stderr
    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)

    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@bot.event
async def on_error(event, *args, **kwargs):

	print("[ERROR]",sys.exc_info())

@bot.event
async def on_member_join(member):
# The Panther Lounge Automatic Role Assignment (MEMBER ROLE)

	guild = bot.get_guild(id=331892870367805440)
	role = discord.utils.get(guild.roles, id=372454832646258688)

	try:
		await member.add_roles(role)
	except (discord.Forbidden, discord.NotFound):
		pass

@bot.event
async def on_ready():
	"""http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

	print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
	print(f'[INFO] Successfully logged in and booted\n')
	
	bot.uptime = datetime.datetime.utcnow()

	# Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
	while True:
		await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="+help", url="http://twitch.tv/supr3meofficial"))
		await asyncio.sleep(300)
		print("\n[INFO] Changed bot's activity and status")
		await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name="v2.0", type=3))
		await asyncio.sleep(300)
		print("\n[INFO] Changed bot's activity and status")
		await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name="New: +hltv", type=2))
		await asyncio.sleep(300)
		print("\n[INFO] Changed bot's activity and status")
		await bot.change_presence(status=discord.Status.online, activity=discord.Game("@supr3meofficial"))
		await asyncio.sleep(300)
		print("\n[INFO] Changed bot's activity and status")

bot.run(os.environ['BOT_TOKEN'], bot=True, reconnect=True)
