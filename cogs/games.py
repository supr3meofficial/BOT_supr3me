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

		result = ":game_die:│ **Rolled:** `{}`".format(str( random.randint(0,maximum_roll) ))

		if maximum_roll <= 2:
			await ctx.send(":warning: You can't roll a number smaller than 2")

		elif maximum_roll >= 100000000000000000000:
			await ctx.send(":warning: Rolls shouldn't be higher than 100000000000000000000")

		else:
			if rigged == False:
				await ctx.send(result)

			else:
				result = ":game_die:│ **Rolled:** `{}`".format(str(maximum_roll))
				await ctx.send(result)

	@commands.command()
	@commands.guild_only()
	async def choose(self, ctx, *choices : str):
		
		choice_msg = ":game_die:│ **Chose:** {}".format(random.choice(choices))
		await ctx.send(choice_msg)

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

		print(subject)
		if "@everyone" in subject:
			await ctx.send(":warning: You cannot do that!")

		elif "@here" in subject:
			await ctx.send(":warning: You cannot do that!")

		else:
			ll = ["a <:l_trap:437614608618881024>","a <:l_thot:437614528881229833>","<:l_gay:437614582849208322>"]
			l = random.choice(ll)

			msg = "{} has been labeled as {}".format(subject, l)
			await ctx.send(msg)


def setup(bot):
	bot.add_cog(GamesCog(bot))
