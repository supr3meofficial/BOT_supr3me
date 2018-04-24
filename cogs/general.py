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
		await ctx.send(f':bust_in_silhouette:│ **User** `{member.display_name}` **joined at** `{member.joined_at}` :thinking:')

	@commands.command(name='cool')
	async def cool_bot(self, ctx):
		"""Is it cool?"""
		coolness = random.randint(1,2)
		if coolness == 1:
			await ctx.send(':game_die:│ **Very Cool**')

		elif coolness == 2:
			await ctx.send(':game_die:│ **Not Cool!**')

	@commands.command()
	@commands.guild_only()
	async def ping(self, ctx):

		with open('txt/ping_counter.txt','r') as bot_pinged_counter_file:

			bot_pinged_counter = int(bot_pinged_counter_file.read())

		bot_pinged_counter += 1
		pong_msg = ':ping_pong: **PONG!**\n*The bot has been pinged %s times so far*' % bot_pinged_counter

		with open('txt/ping_counter.txt','w') as bot_pinged_counter_file:

			bot_pinged_counter_file.write(str(bot_pinged_counter))

		await ctx.send(pong_msg)

	@commands.command()
	@commands.guild_only()
	async def publicmessage(self, ctx, *phrase):

		if "read" in phrase:
			with open('txt/secret.txt','r') as read_secret:
				await ctx.send(read_secret.read())

		else:
			if "@here" in phrase:
				await ctx.send(':warning: **Unauthorised message.**')

			elif "@everyone" in phrase:
				await ctx.send(':warning: **Unauthorised message.**')

			else:
				with open('txt/secret.txt','w') as write_secret:

					for word in phrase:

						write_secret.write(word)
						write_secret.write(' ')

				await ctx.send(':secret:│ **Message has been saved.** Do +publicmessage read to read it')


	

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
	bot.add_cog(GeneralCommandsCog(bot))