import discord
from discord.ext import commands
import random
import asyncio

async def track_animation(trackracer, ctx):

	anim1 = "<:raceflags:433061672387739650> :wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash: <:Audi:433020256521551893>"
	anim2 = "<:raceflags:433061672387739650> :wavy_dash::wavy_dash::wavy_dash::wavy_dash: <:Audi:433020256521551893>"
	anim3 = "<:raceflags:433061672387739650> :wavy_dash::wavy_dash::wavy_dash: <:Audi:433020256521551893>"
	anim4 = "<:raceflags:433061672387739650> :wavy_dash::wavy_dash: <:Audi:433020256521551893>"
	anim5 = "<:raceflags:433061672387739650> :wavy_dash: <:Audi:433020256521551893>"
	anim6 = "<:raceflags:433061672387739650> <:Audi:433020256521551893> <:blacktrophy:433062084528308225>"

	def tracksleeper():

		return random.randint(1,10)
		

	totaltracksleep = 0

	trackmsg = await ctx.send(anim1)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep
	await trackmsg.edit(content=anim2)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep
	await trackmsg.edit(content=anim3)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep) 
	totaltracksleep += tracksleep
	await trackmsg.edit(content=anim4)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep
	await trackmsg.edit(content=anim5)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep
	await trackmsg.edit(content=anim6)
	await asyncio.sleep(1)

	anim7 = ":stopwatch: **{}'s Time: **{} seconds".format(trackracer, totaltracksleep) 
	await ctx.send(anim7)


class GamesCog:

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.guild_only()
	async def roll(self, ctx, maximum_roll = 100, rigged = False):

		member = ctx.author
		result = ":game_die: **Rolled:** `{}`".format(str(random.randint(0,maximum_roll)))

		if rigged:
			result = ":game_die: **Rolled:** `{}`".format(maximum_roll)
			
		else:
			if maximum_roll <= 2:
				result = ":warning: You can't roll a number smaller than 2"
			elif maximum_roll >= 100000000000000000000:
				result = ":warning: Rolls shouldn't be higher than 100000000000000000000"
		
		embed = discord.Embed(title="", description=result, colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		await ctx.send(embed=embed)



	@commands.command()
	@commands.guild_only()
	async def choose(self, ctx, *choices : str):

		member = ctx.author
		choice_msg = ":game_die: **Chose:** {}".format(random.choice(choices))

		embed = discord.Embed(title="", description=choice_msg, colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		await ctx.send(embed=embed)

	@commands.command()
	@commands.guild_only()
	async def nibba(self, ctx):

		r = random.randint(0,100)
		if r > 95:
			nibba = "🅱"
		else:
			nibba = "🇧"

		await ctx.message.add_reaction(nibba)

	@commands.command()
	@commands.guild_only()
	async def race(self, ctx):

		await track_animation(ctx.author.mention, ctx)

	@commands.command()
	@commands.guild_only()
	async def label(self, ctx, subject="You"):

		member = ctx.author

		if "@everyone" in subject:
			await ctx.send(":warning: You cannot do that!")

		elif "@here" in subject:
			await ctx.send(":warning: You cannot do that!")

		else:
			label_list = ["a <:l_trap:437614608618881024>","a <:l_thot:437614528881229833>","<:l_gay:437614582849208322>"]
			label = random.choice(label_list)

			msg = "{} has been labeled as {}".format(subject, label)
			embed = discord.Embed(title="", description=msg, colour=member.colour)
			embed.set_author(icon_url=member.avatar_url, name=str(member))
			await ctx.send(embed=embed)
	
	@commands.command()
	@commands.guild_only()
	async def onedeag(self, ctx):

		member = ctx.author
		members = ctx.guild.members
		shot = random.choice(members)
		deags = ["<:Deagle:490629020585558036>", "<:Deagle2:490629361964417048>", "<:Deagle3:490629362115149846>", "<:Deagle4:490629361851039776>"]
		deag = random.choice(deags)
		onedeag = deag + " You have popped a 1-Deag on **" + str(shot.name) + "**"
		await ctx.send(onedeag)


def setup(bot):
	bot.add_cog(GamesCog(bot))
