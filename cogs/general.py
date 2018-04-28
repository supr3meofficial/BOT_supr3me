import discord
import random
from discord.ext import commands


class GeneralCommandsCog:

	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	@commands.guild_only()
	async def joined(self, ctx, *, member: discord.Member):
		"""Says when a member joined."""

		requested_by = "Requested by {}".format(ctx.author.name)
		msg = '**Join date:** `{}`'.format(member.joined_at)

		embed = discord.Embed(title="", description=msg, colour=ctx.author.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		embed.set_footer(text=requested_by)
		
		await ctx.send(embed=embed)

	@commands.command(name='cool')
	async def cool_bot(self, ctx):
		"""Is it cool?"""

		member = ctx.author
		coolness = random.randint(1,2)

		if coolness == 1:
			msg = ':game_die: **Very Cool!**'
		elif coolness == 2:
			msg = ':game_die: **Not Cool!**'
		
		embed = discord.Embed(title="", description=msg, colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		await ctx.send(embed=embed)

	@commands.command()
	@commands.guild_only()
	async def ping(self, ctx):

		member = ctx.author
		requested_by = "Requested by {}".format(ctx.author.name)
		latency = '{0}'.format(round(self.bot.latency, 1))
		desc = "<:signal:439905517280690176> **Latency:** {} ms".format(latency)

		embed = discord.Embed(title="", description=desc, colour=member.colour)
		embed.set_author(icon_url=self.bot.user.avatar_url, name=str(self.bot.user.name))
		embed.set_footer(text=requested_by)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.guild_only()
	async def publicmessage(self, ctx, *phrase):

		member = ctx.author

		if "read" in phrase:
			with open('txt/secret.txt','r') as read_secret:
				msg = read_secret.read()
				return await ctx.send(msg)
				
		else:
			if "@here" in phrase:
				msg = ':warning: **Unauthorised message.**'
				return await ctx.send(msg)

			elif "@everyone" in phrase:
				msg = ':warning: **Unauthorised message.**'

			else:
				with open('txt/secret.txt','w') as write_secret:
					for word in phrase:
						write_secret.write(word)
						write_secret.write(' ')

				msg = ':secret: **Message has been saved.** Do +publicmessage read to read it'

		embed = discord.Embed(title="", description=msg, colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		await ctx.send(embed=embed)

	@commands.command()
	@commands.guild_only()
	async def oof(self, ctx):

		await ctx.send("<:oof:439920274029412352>")

def setup(bot):
	bot.add_cog(GeneralCommandsCog(bot))
