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
	anim6 = "<:raceflags:433061672387739650> <:Audi:433020256521551893>"

	def tracksleeper():

		return random.randint(1,10)
		
	member = ctx.author
	membercar = "{}'s car".format(member.name)
	totaltracksleep = 0

	embed = discord.Embed(title="", description=anim1, colour=member.colour)
	embed.set_author(icon_url=member.avatar_url, name=membercar)
	trackmsg = await ctx.send(embed=embed)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep

	embed = discord.Embed(title="", description=anim2, colour=member.colour)
	embed.set_author(icon_url=member.avatar_url, name=membercar)
	await trackmsg.edit(embed=embed)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep

	embed = discord.Embed(title="", description=anim3, colour=member.colour)
	embed.set_author(icon_url=member.avatar_url, name=membercar)
	await trackmsg.edit(embed=embed)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep

	embed = discord.Embed(title="", description=anim4, colour=member.colour)
	embed.set_author(icon_url=member.avatar_url, name=membercar)
	await trackmsg.edit(embed=embed)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep

	embed = discord.Embed(title="", description=anim5, colour=member.colour)
	embed.set_author(icon_url=member.avatar_url, name=membercar)
	await trackmsg.edit(embed=embed)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep

	embed = discord.Embed(title="", description=anim6, colour=member.colour)
	embed.set_author(icon_url=member.avatar_url, name=membercar)
	await trackmsg.edit(embed=embed)
	tracksleep = tracksleeper()
	await asyncio.sleep(tracksleep)
	totaltracksleep += tracksleep

	await asyncio.sleep(1)

	laptime = "{} seconds".format(totaltracksleep)
	embed = discord.Embed(title="", description="", colour=member.colour)
	embed.set_author(icon_url=member.avatar_url, name=membercar)
	embed.set_thumbnail(url="https://twemoji.maxcdn.com/2/72x72/23f1.png")
	embed.add_field(name="Lap Time:", value=laptime, inline=False)
	await trackmsg.edit(embed=embed)


class GamesCog:

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.guild_only()
	async def roll(self, ctx, maximum_roll = 100):

		member = ctx.author
		rolled = random.randint(0,maximum_roll)

		embed = discord.Embed(title="", description="", colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		embed.set_thumbnail(url="https://twemoji.maxcdn.com/2/72x72/1f3b2.png")
		embed.add_field(name="Rolled:", value=rolled, inline=True)
		embed.add_field(name="Roll Cap:", value=maximum_roll, inline=True)
		await ctx.send(embed=embed)



	@commands.command()
	@commands.guild_only()
	async def choose(self, ctx, *choices : str):

		member = ctx.author
		choice = random.choice(choices)

		embed = discord.Embed(title="", description="", colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		embed.set_thumbnail(url="https://twemoji.maxcdn.com/2/72x72/1f3b2.png")
		embed.add_field(name="Chose:", value=choice, inline=True)
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
	async def onedeag(self, ctx, shot: discord.Member = None):

		member = ctx.author
		members = ctx.guild.members
		if shot == None:
			shot = random.choice(members)
		shot = shot.name

		deags = ["https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_gs_deagle_aggressor_light_large.51ffb87f03ae0d3c467d4412f3c246067748e61d.png", 
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_am_scales_bravo_light_large.6cba46695e74a8bee932ea90cea24e146cbef5e7.png", 
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_gs_deagle_mecha_light_large.e08c1fd8709f6b368956c41c68b17c15ff635635.png", 
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aq_deserteagle_kumichodragon_light_large.19874e9a20cfac49efbe1f1557b995e453633ffe.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_cu_deagle_aureus_light_large.7fa76057cb05f2cab829be448f120ae540715d0e.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_am_ddpatdense_peacock_light_large.a486db3160bcdcf6bc5a1d8179c450b02f620151.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aa_vertigo_light_large.85a16e4bfb8b1cc6393ca5d0c6d3a1e6e6023323.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_gs_deagle_exo_light_large.8bdc93f1b45efba187748065deff967eef8f2f2d.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aq_desert_eagle_constable_light_large.fb2f2673dd3997a21bff9129e0d2e294c03095e8.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aq_deagle_naga_light_large.b410ad835b1894a448676ae0590586298af2cb33.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_hy_webs_darker_light_large.7b9cb19bac52ebe7c49e3abdfb0c400ea252fef8.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aq_engraved_deagle_light_large.804a1a01a29bf80673b739f3eb220272a6838193.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_am_seastorm_shojo_light_large.7df4fe386dac18ae2a8c3e50df7dfb9165dece83.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_am_seastorm_blood_light_large.1e92a7e19fde014e5a70832a93b440e0c036d596.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aq_handcannon_light_large.e6e87ceb2337a423d225dc177342af3df4069585.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aq_pilot_deagle_light_large.60b0e755ef14311a82f5f35928ad18dbb6ae2a86.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aa_flames_light_large.dd140c3b359c16ccd8e918ca6ad0b2628151fe1c.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_cu_desert_eagle_corroden_light_large.5fde2cc1c9b82b0e9823445c7fb2be334bc286af.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_aq_deagle_corinthian_light_large.1a694892a1953a131775451d0542508b4b3d9e77.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_am_bronze_sparkle_light_large.42dc1d2bae9e586f75d6425f94a195014891533b.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_am_crystallized_dark_light_large.2d7d753a893ec3f0a470af9690aa64dcecd7146f.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_hy_varicamo_urban_light_large.a9791d0046206f88085f2d0850ec577c6f535a47.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_so_night_light_large.64e315553578f3c8bd08c96622fc2c34d5a789ba.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_am_seastorm_light_large.aef21efecda37237d24debe3f409f42954dadddd.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_hy_ddpat_urb_light_large.06af0cb0e08490f1fba17acd1b9c98978745c213.png",
				"https://steamcdn-a.akamaihd.net/apps/730/icons/econ/default_generated/weapon_deagle_hy_mottled_sand_light_large.615be084d4bc9db8c98451f13351cae1fa0ec69c.png",
				"https://csgostash.com/img/weapons/Desert_Eagle.png"]
		deag = random.choice(deags)

		embed = discord.Embed(title="", description="", colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		embed.set_thumbnail(url=deag)
		embed.add_field(name="You have popped a one deag on:", value=shot, inline=True)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(GamesCog(bot))
