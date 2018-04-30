import discord
from discord.ext import commands
import random
import aiohttp
import asyncio

class MiscCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):

        embed=discord.Embed(title="<:discord:434011189656158219> BOT Invite Link", url="https://discordapp.com/oauth2/authorize?&client_id=331818798015315970&scope=bot&permissions=8", description="Click the link above to invite the bot to your discord!", color=0x80ff00)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def discord(self, ctx):

        embed=discord.Embed(title="<:discord:434011189656158219> Discord", url="https://discord.gg/FMn43Qq", description="Please join our discord using the link above", color=0x80ff00)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def patreon(self, ctx):

        embed=discord.Embed(title="<:Patreon:437227448384618527> Patreon", url="https://www.patreon.com/supr3me", description="If you would like to become a patron, click the link above, thank you!", color=0x80ff00)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def donate(self, ctx):

        embed=discord.Embed(title="<:steam:434018638748581898> Trade Link", url="https://steamcommunity.com/tradeoffer/new/?partner=342778939&token=tS1Rd02f", description="If you would like to help me, click the link above, thank you!", color=0x80ff00)
        await ctx.send(embed=embed)
        embed=discord.Embed(title="<:PayPal:437213765923241986> Paypal Link", url="https://www.paypal.me/supr3medonate", description="If you would like to help me, click the link above, thank you!", color=0x80ff00)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as r:
				
                if r.status == 200:

                    js = await r.json()
                    embed = discord.Embed(title=":cat: Random Cat", description="", colour=ctx.author.colour)
                    embed.set_image(url=js['file'])
                    requested_by = "Requested by {}".format(ctx.author.name)
                    embed.set_footer(text=requested_by)
                    await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://random.dog/woof.json') as r:

                if r.status == 200:

                    js = await r.json()
                    embed = discord.Embed(title=":dog: Random Dog", description="", colour=ctx.author.colour)
                    embed.set_image(url=js['url'])
                    requested_by = "Requested by {}".format(ctx.author.name)
                    embed.set_footer(text=requested_by)
                    await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def clock(self, ctx):

        botmsg = await ctx.send("Clocking..")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock1:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock2:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock3:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock4:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock5:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock6:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock7:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock8:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock9:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock10:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock11:")
        await asyncio.sleep(1)
        await botmsg.edit(content=":clock12:")
        await botmsg.add_reaction("🏁")

    @commands.command()
    @commands.guild_only()
    async def dab(self, ctx, member):

        msg = ":arrow_forward: {} just dabbed on {}".format(ctx.author.name, member)
        embed = discord.Embed(title="<:Dab:423581839165358080> Dabbing on the haters", description=msg, colour=ctx.author.colour)
        await ctx.send(embed=embed)
		

def setup(bot):
    bot.add_cog(MiscCog(bot))
