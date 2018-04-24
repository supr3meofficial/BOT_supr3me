import discord
from discord.ext import commands
import asyncio
import datetime
import sys, traceback
import config

def get_prefix(bot, message):
	"""A callable Prefix for our bot. This could be edited to allow per server prefixes."""

	# Notice how you can use spaces in prefixes. Try to keep them simple though.
	prefixes = ['++','+']

	# Check to see if we are outside of a guild. e.g DM's etc.
	if not message.guild:
		# Only allow ? to be used in DMs
		return 'help'

	# If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
	return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
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


bot.run(config.key, bot=True, reconnect=True)