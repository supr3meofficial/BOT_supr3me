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

	# BOT OWNER COMMANDS 

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

		perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

		embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
		embed.set_author(icon_url=member.avatar_url, name=str(member))

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
			def get_invites():
				invites_url = ""
				invites = guild.invites()
				for invite in invites:
					invites_url += str(invite.url + "\n")
				return invites_url
					
			embed.add_field(name=guild.name, value=get_invites(), inline=False)

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

	# GUILD OWNER/STAFF COMMANDS:
	
	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, reason=None, delete_message_days=0):

		banned_by = "Banned by {}".format(ctx.author.name)
		user_banned = "{} is no longer.".format(member.name)
		guild = ctx.message.guild

		embed = discord.Embed(title='',
		description="<:BanHammer:439943003847786499> The ban hammer has spoken", 
		colour=ctx.author.colour)
		embed.set_author(icon_url=member.avatar_url, name=user_banned)
		embed.set_footer(text=banned_by)

		try:
			await guild.ban(member, reason=reason, delete_message_days=delete_message_days)
			await ctx.send(embed=embed)

		except discord.Forbidden:
			embed = discord.Embed(title='No permissions',
			description="You do not have enough permissions to perform this command",
			colour=0xbf0000)
			embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
			await ctx.send(embed=embed)	
			
	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, reason=None):

		kicked_by = "Kicked by {}".format(ctx.author.name)
		user_kicked = "{} is gone.".format(member.name)
		guild = ctx.message.guild

		embed = discord.Embed(title='',
		description="<:BanHammer:439943003847786499> The ban hammer has spoken, lightly", 
		colour=ctx.author.colour)
		embed.set_author(icon_url=member.avatar_url, name=user_kicked)
		embed.set_footer(text=kicked_by)

		try:
			await guild.kick(member, reason=reason)
			await ctx.send(embed=embed)

		except discord.Forbidden:
			embed = discord.Embed(title='No permissions',
			description="You do not have enough permissions to perform this command",
			colour=0xbf0000)
			embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
			await ctx.send(embed=embed)

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, member: int, reason=None):

		unbanned_by = "Unbanned by {}".format(ctx.author.name)
		user_unbanned = "ID {} has been unbanned".format(member)
		guild = ctx.message.guild

		embed = discord.Embed(title="",
		description="<:BanHammer:439943003847786499> The ban hammer has forgiven", 
		colour=ctx.author.colour)
		embed.set_author(icon_url="https://cdn.discordapp.com/embed/avatars/0.png", name=user_unbanned)
		embed.set_footer(text=unbanned_by)

		try:
			await guild.unban(user=discord.Object(id=member), reason=reason)
			await ctx.send(embed=embed)

		except discord.Forbidden:
			embed = discord.Embed(title='No permissions',
			description="You do not have enough permissions to perform this command",
			colour=0xbf0000)
			embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(OwnerCog(bot))
