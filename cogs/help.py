import discord
from discord.ext import commands

def display_help(help_to_display = None):

	global show_help

	if help_to_display == None:

		with open('txt/help.txt','r') as help_file:

			show_help = help_file.read()

	elif help_to_display == 'help':

		show_help = ':question:│ `Usage: +help`\n:grey_exclamation:│ `Result: Shows you the help page`'

	elif help_to_display == 'roll':

		show_help = ':question:│ `Usage: +roll <max roll>`\n:grey_exclamation:│ `Result: Rolls a dice with the max value set`'

	elif help_to_display == 'choose':

		show_help = ':question:│ `Usage: +choose <choices>`\n:grey_exclamation:│ `Result: Chooses between a selection of anything set`'

	elif help_to_display == 'joined':

		show_help = ':question:│ `Usage: +joined <user>`\n:grey_exclamation:│ `Result: Tells you when a user joined the discord`'

	elif help_to_display == 'cat':

		show_help = ':question:│ `Usage: +cat`\n:grey_exclamation:│ `Result: Posts a random cat picture`'

	elif help_to_display == 'dog':

		show_help = ':question:│ `Usage: +dog`\n:grey_exclamation:│ `Result: Posts a random dog picture.`'

	elif help_to_display == 'ping':

		show_help = ':question:│ `Usage: +ping`\n:grey_exclamation:│ `Result: Pings the bot`'

	elif help_to_display == 'opencase':

		show_help = ':question:│ `Usage: +opencase`\n:grey_exclamation:│ `Result: Opens a CS:GO case`'

	elif help_to_display == 'discord':

		show_help = ':question:│ `Usage: +discord`\n:grey_exclamation:│ `Result: Posts the official discord link`'

	elif help_to_display == 'donate':

		show_help = ':question:│ `Usage: +donate`\n:grey_exclamation:│ `Result: Posts the donation links to supr3me`'

	elif help_to_display == 'clock':

		show_help = ':question:│ `Usage: +clock`\n:grey_exclamation:│ `Result: Sets up an animated clock`'

	elif help_to_display == 'race':

		show_help = ':question:│ `Usage: +race`\n:grey_exclamation:│ `Result: Minigame that races an Audi for a random time`'

	elif help_to_display == 'nibba':

		show_help = ':question:│ `Usage: +nibba`\n:grey_exclamation:│ `Result: Minigame that tests your luck in getting the red B`'

	elif help_to_display == 'hltv':

		show_help = ':question:│ `Usage: +hltv`\n:grey_exclamation:│ `Commands: top5, top15, nextmatches, results`'

	elif help_to_display == 'invite':

		show_help = ':question:│ `Usage: +invite `\n:grey_exclamation:│ `Result: Posts the bot invitation link`'
	
	elif help_to_display == 'oof':

		show_help = ':question:│ `Usage: +oof `\n:grey_exclamation:│ `Result: Posts an oof`'
	
	elif help_to_display == 'ban':

		show_help = ':question:│ `Usage: +ban <member> <reason> <delete_message_days> `\n:grey_exclamation:│ `Result: Bans a member`'
	
	elif help_to_display == 'unban':

		show_help = ':question:│ `Usage: +unban <id> <reason> `\n:grey_exclamation:│ `Result: Unbans a member`'
	
	elif help_to_display == 'kick':

		show_help = ':question:│ `Usage: +kick <member> <reason> `\n:grey_exclamation:│ `Result: Kicks a member`'
	
	elif help_to_display == 'dab':
		
		show_help = ':question:│ `Usage: +dab <anything> `\n:grey_exclamation:│ `Result: Dabs on the haters`'
		
	elif help_to_display == 'mitochondria':
		
		show_help = ':question:│ `Usage: +mitochondria `\n:grey_exclamation:│ `Result: Posts a secret message to ISIS`'
	
	elif help_to_display == 'literallyme':
		
		show_help = ':question:│ `Usage: +literallyme `\n:grey_exclamation:│ `Result: Posts a relatable picture`'

	elif help_to_display == 'github':

		show_help = ':question:│ `Usage: +github `\n:grey_exclamation:│ `Result: Posts the bot github link`'
	
	elif help_to_display == 'onedeag':

		show_help = ':question:| `Usage: +onedeag`\n:grey_exclamation:| `Result: One deags a random guild member`'

	elif help_to_display == 'spotify':

		show_help = ':question:| `Usage: +spotify <member>`\n:grey_exclamation:| `Result: Displays the current song the user is listening to`'
	
	elif help_to_display == 'createinvite':

		show_help = ':question:| `Usage: +createinvite`\n:grey_exclamation:| `Result: Creates an invite for the channel the command is ran`'

	else:

		show_help = ':warning: **Command not found.**'

class HelpCog:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='help')
	async def help(self, ctx, h_command = None):
		
		display_help(h_command)
		await ctx.message.add_reaction("❔")
		embed=discord.Embed(title="Commands List", description=show_help, color=0x0080c0)
		embed.set_footer(text="Type +help <command> for the usage of a command | Coded by supr3me", icon_url=self.bot.user.avatar_url)
		await ctx.author.send(embed=embed)

def setup(bot):
	bot.remove_command('help')	
	bot.add_cog(HelpCog(bot))
