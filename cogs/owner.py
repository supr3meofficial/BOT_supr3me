import discord
from discord.ext import commands
import datetime

def get_human_readable_uptime_diff(start_time):
	
	now = datetime.datetime.utcnow()
	delta = now - start_time
	hours, remainder = divmod(int(delta.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)

	if days:
		fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
	else:
		fmt = '{h} hours, {m} minutes, and {s} seconds'

	return fmt.format(d=days, h=hours, m=minutes, s=seconds)

class OwnerCog:

	def __init__(self, bot):
		self.bot = bot
	
	# Hidden means it won't show up on the default help.
	@commands.command(name='load', hidden=True)
	@commands.is_owner()
	async def cog_load(self, ctx, *, cog: str):
		"""Command which Loads a Module.
		Remember to use dot path. e.g: cogs.owner"""

		try:
			self.bot.load_extension(cog)
		except Exception as e:
			msg=f'**:warning: ERROR:** `{type(e).__name__} - {e}`'
			print("\n[WARNING] Failed to load {}".format(cog))
		else:
			msg='**:white_check_mark: SUCCESS**'
			print("\n[INFO] Loaded {}".format(cog))
		
		embed = discord.Embed(title='Module Load', description=msg, colour=0xbf0000)
		embed.set_author(icon_url=self.bot.user.avatar_url, name=self.bot.user.name)
		await ctx.send(embed=embed)
		
	@commands.command(name='unload', hidden=True)
	@commands.is_owner()
	async def cog_unload(self, ctx, *, cog: str):
		"""Command which Unloads a Module.
		Remember to use dot path. e.g: cogs.owner"""
		
		try:
			self.bot.unload_extension(cog)
		except Exception as e:
			msg=f'**:warning: ERROR:** `{type(e).__name__} - {e}`'
			print("\n[WARNING] Failed to unload {}".format(cog))
		else:
			msg='**:white_check_mark: SUCCESS**'
			print("\n[INFO] Unloaded {}".format(cog))
		
		embed = discord.Embed(title='Module Unload', description=msg, colour=0xbf0000)
		embed.set_author(icon_url=self.bot.user.avatar_url, name=self.bot.user.name)
		await ctx.send(embed=embed)		

	@commands.command(name='reload', hidden=True)
	@commands.is_owner()
	async def cog_reload(self, ctx, *, cog: str):
		"""Command which Reloads a Module.
		Remember to use dot path. e.g: cogs.owner"""

		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
		except Exception as e:
			msg=f'**:warning: ERROR:** `{type(e).__name__} - {e}`'
			print("\n[WARNING] Failed to reload {}".format(cog))
		else:
			msg='**:white_check_mark: SUCCESS**'
			print("\n[INFO] Reloaded {}".format(cog))
		
		embed = discord.Embed(title='Module Reload', description=msg, colour=0xbf0000)
		embed.set_author(icon_url=self.bot.user.avatar_url, name=self.bot.user.name)
		await ctx.send(embed=embed)
			

	@commands.command(name='top_role', aliases=['toprole'])
	@commands.is_owner()
	@commands.guild_only()
	async def show_toprole(self, ctx, *, member: discord.Member=None):
		"""Simple command which shows the members Top Role."""

		if member is None:
			member = ctx.author

		await ctx.send(f'The top role for `{member.display_name}` is `{member.top_role.name}`')

	@commands.command(name='perms', aliases=['perms_for', 'permissions'])
	@commands.is_owner()
	@commands.guild_only()
	async def check_permissions(self, ctx, *, member: discord.Member=None):
		"""A simple command which checks a members Guild Permissions.
		If member is not provided, the author will be checked."""

		if not member:
			member = ctx.author

		# Here we check if the value of each permission is True.
		perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

		# And to make it look nice, we wrap it in an Embed.
		embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))

		# \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
		embed.add_field(name='\uFEFF', value=perms)

		await ctx.send(content=None, embed=embed)

	@commands.command(name='spam', aliases=['say'])
	@commands.is_owner()
	@commands.guild_only()
	async def spam(self, ctx, amount, content : str):

		for spammer in range(int(amount)):
			await ctx.send(content)

	@commands.group()
	@commands.is_owner()
	@commands.guild_only()
	async def info(self, ctx):
		if ctx.invoked_subcommand is None:
			pass
	
	@info.command()
	async def servers(self, ctx):

		embed = discord.Embed(title='Connected Servers:', description='', colour=0xbf0000)
		embed.set_author(icon_url=self.bot.user.avatar_url, name=self.bot.user.name)

		for guild in self.bot.guilds:

			embed.add_field(name='\uFEFF', value=guild.name, inline=False)

		await ctx.send(embed=embed)

	@info.command()
	async def uptime(self, ctx):

		def get_bot_uptime():

			return get_human_readable_uptime_diff(self.bot.uptime)

		embed = discord.Embed(title='Uptime:', description=get_bot_uptime(), colour=0xbf0000)
		embed.set_author(icon_url=self.bot.user.avatar_url, name=self.bot.user.name)
		await ctx.send(embed=embed)
	
	@info.command()
	async def channel(self, ctx):

		embed = discord.Embed(title='', description='', colour=0xbf0000)
		embed.set_author(icon_url=self.bot.user.avatar_url, name=self.bot.user.name)
		embed.add_field(name='**Channel Name:**', value=ctx.channel.name, inline=False)
		embed.add_field(name='**Channel ID:**', value=ctx.channel.id, inline=False)
		await ctx.send(embed=embed)

	@info.command()
	async def member(self, ctx, member: discord.Member=None):

		if member is None:
			member = ctx.author
		
		embed = discord.Embed(title='', description='', colour=0xbf0000)
		embed.set_author(icon_url=member.avatar_url, name=member.name)
		embed.add_field(name='**Member Name:**', value=member.name, inline=False)
		embed.add_field(name='**Member Nickname:**', value=member.nick, inline=False)
		embed.add_field(name='**Member ID:**', value=member.id, inline=False)
		embed.add_field(name='**Member Status:**', value=str(member.status), inline=False)
		embed.add_field(name='**Member Activity:**', value=str(member.activity), inline=False)
		await ctx.send(embed=embed)


# Thanks to Gio for the Command.

def setup(bot):
	bot.add_cog(OwnerCog(bot))