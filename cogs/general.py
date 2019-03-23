import discord
import random
from discord.ext import commands


class GeneralCommandsCog:

	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	@commands.guild_only()
	async def joined(self, ctx, *, member: discord.Member):

		date = str(member.joined_at).split(".")[0]
		requested_by = "Requested by {}".format(ctx.author.name)

		embed = discord.Embed(title="", description="", colour=ctx.author.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		embed.set_thumbnail(url="https://twemoji.maxcdn.com/2/72x72/1f552.png")
		embed.add_field(name="Join Date:", value=date, inline=False)
		embed.set_footer(text=requested_by)
		
		await ctx.send(embed=embed)

	@commands.command()
	@commands.guild_only()
	async def ping(self, ctx):

		member = ctx.author
		requested_by = "Requested by {}".format(ctx.author.name)
		latency = '{0}'.format(round(self.bot.latency, 1))
		desc = "{} ms".format(latency)

		embed = discord.Embed(title="", description="", colour=member.colour)
		embed.set_author(icon_url=self.bot.user.avatar_url, name=str(self.bot.user.name))
		embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/439905517280690176.png")
		embed.add_field(name="Latency:", value=desc, inline=False)
		embed.set_footer(text=requested_by)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.guild_only()
	async def spotify(self, ctx, member: discord.Member):

		requested_by = "Requested by {}".format(ctx.author.name)
		listener = "{} is listening to:".format(member.name)
		spotify = member.activity
		duration = str(spotify.duration).split(".")[0]
		artists = str(spotify.artist).replace(";",",")

		embed = discord.Embed(title="", description="", colour=spotify.colour)
		embed.set_author(icon_url="https://images-eu.ssl-images-amazon.com/images/I/51rttY7a%2B9L.png", name=listener)
		embed.set_thumbnail(url=spotify.album_cover_url)
		embed.add_field(name="Title:", value=spotify.title, inline=False)
		embed.add_field(name="Artists:", value=artists, inline=False)
		embed.add_field(name="Album:", value=spotify.album, inline=False)
		embed.add_field(name="Duration:", value=duration, inline=False)
		embed.set_footer(text=requested_by)
		await ctx.send(embed=embed)


	@commands.command()
	@commands.guild_only()
	async def oof(self, ctx):

		await ctx.send("<:oof:439920274029412352>")

	@commands.command(name='createinvite',aliases=['createinv','create_inv','create_invite'])
	@commands.guild_only()
	async def createinvite(self, ctx):

		requested_by = "Requested by {}".format(ctx.author.name)
		channel = ctx.channel
		inv = await channel.create_invite(reason="Created via command")
		embed = discord.Embed(title="Invite Created", description=inv.url, color=ctx.author.colour)
		embed.set_thumbnail(url="https://twemoji.maxcdn.com/2/72x72/1f517.png")
		embed.set_footer(text=requested_by)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(GeneralCommandsCog(bot))
