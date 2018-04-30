import discord
from discord.ext import commands
from .imports import hltv

class HLTVCog:

    def __init__(self,bot):
        self.bot = bot

    @commands.group()
    @commands.guild_only()
    async def hltv(self, ctx):
        if ctx.invoked_subcommand is None:
            pass
            
    @hltv.command(name='results', aliases=['matchresults','result','latestresults'])
    async def result(self, ctx):

        async with ctx.channel.typing():

            msg = """
**Date:** {}
**Event:** {}
**Score:** {} `{}-{}` {}

**Date:** {}
**Event:** {}
**Score:** {} `{}-{}` {}

**Date:** {}
**Event:** {}
**Score:** {} `{}-{}` {}

**Date:** {}
**Event:** {}
**Score:** {} `{}-{}` {}

**Date:** {}
**Event:** {}
**Score:** {} `{}-{}` {}
""".format(
    str(hltv.get_results()[0]['date'])[14:-1],
    str(hltv.get_results()[0]['event'])[2:-1],
    str(hltv.get_results()[0]['team1'])[2:-1],
    str(hltv.get_results()[0]['team1score']),
    str(hltv.get_results()[0]['team2score']),
    str(hltv.get_results()[0]['team2'])[2:-1],
    str(hltv.get_results()[1]['date'])[14:-1],
    str(hltv.get_results()[1]['event'])[2:-1],
    str(hltv.get_results()[1]['team1'])[2:-1],
    str(hltv.get_results()[1]['team1score']),
    str(hltv.get_results()[1]['team2score']),
    str(hltv.get_results()[1]['team2'])[2:-1],
    str(hltv.get_results()[2]['date'])[14:-1],
    str(hltv.get_results()[2]['event'])[2:-1],
    str(hltv.get_results()[2]['team1'])[2:-1],
    str(hltv.get_results()[2]['team1score']),
    str(hltv.get_results()[2]['team2score']),
    str(hltv.get_results()[2]['team2'])[2:-1],
    str(hltv.get_results()[3]['date'])[14:-1],
    str(hltv.get_results()[3]['event'])[2:-1],
    str(hltv.get_results()[3]['team1'])[2:-1],
    str(hltv.get_results()[3]['team1score']),
    str(hltv.get_results()[3]['team2score']),
    str(hltv.get_results()[3]['team2'])[2:-1],
    str(hltv.get_results()[4]['date'])[14:-1],
    str(hltv.get_results()[4]['event'])[2:-1],
    str(hltv.get_results()[4]['team1'])[2:-1],
    str(hltv.get_results()[4]['team1score']),
    str(hltv.get_results()[4]['team2score']),
    str(hltv.get_results()[4]['team2'])[2:-1]
        )
        
        embed=discord.Embed(title="Latest 5 Matches", description=msg, color=0x0069d2)
        embed.set_author(name="HLTV", url="https://www.hltv.org/", icon_url="https://pbs.twimg.com/profile_images/766575292441845760/ySDr_slD_400x400.jpg")
        await ctx.send(embed=embed)

    @hltv.command(name='nextmatches', aliases=['nextmatch','matches','match'])
    async def nextmatches(self, ctx):

        async with ctx.channel.typing():

            #match1_date = str(hltv.get_matches()[0]['date'])[2:-1]
            match1_time = str(hltv.get_matches()[0]['time'])[2:-1]
            match1_event = str(hltv.get_matches()[0]['event'])[2:-1]
            match1_team1 = str(hltv.get_matches()[0]['team1'])[2:-1]
            match1_team2 = str(hltv.get_matches()[0]['team2'])[2:-1]
            #match2_date = str(hltv.get_matches()[1]['date'])[2:-1]
            match2_time = str(hltv.get_matches()[1]['time'])[2:-1]
            match2_event = str(hltv.get_matches()[1]['event'])[2:-1]
            match2_team1 = str(hltv.get_matches()[1]['team1'])[2:-1]
            match2_team2 = str(hltv.get_matches()[1]['team2'])[2:-1]
            #match3_date = str(hltv.get_matches()[2]['date'])[2:-1]
            match3_time = str(hltv.get_matches()[2]['time'])[2:-1]
            match3_event = str(hltv.get_matches()[2]['event'])[2:-1]
            match3_team1 = str(hltv.get_matches()[2]['team1'])[2:-1]
            match3_team2 = str(hltv.get_matches()[2]['team2'])[2:-1]
            #match4_date = str(hltv.get_matches()[3]['date'])[2:-1]
            match4_time = str(hltv.get_matches()[3]['time'])[2:-1]
            match4_event = str(hltv.get_matches()[3]['event'])[2:-1]
            match4_team1 = str(hltv.get_matches()[3]['team1'])[2:-1]
            match4_team2 = str(hltv.get_matches()[3]['team2'])[2:-1]
            #match5_date = str(hltv.get_matches()[4]['date'])[2:-1]
            match5_time = str(hltv.get_matches()[4]['time'])[2:-1]
            match5_event = str(hltv.get_matches()[4]['event'])[2:-1]
            match5_team1 = str(hltv.get_matches()[4]['team1'])[2:-1]
            match5_team2 = str(hltv.get_matches()[4]['team2'])[2:-1]

            msg = """

**Event:** {}
**Time:** {}
**Match:** {} **vs.** {}

**Event:** {}
**Time:** {}
**Match:** {} **vs.** {}

**Event:** {}
**Time:** {}
**Match:** {} **vs.** {}

**Event:** {}
**Time:** {}
**Match:** {} **vs.** {}

**Event:** {}
**Time:** {}
**Match:** {} **vs.** {}
            """.format(
                match1_event,match1_time,match1_team1,match1_team2,
                match2_event,match2_time,match2_team1,match2_team2,
                match3_event,match3_time,match3_team1,match3_team2,
                match4_event,match4_time,match4_team1,match4_team2,
                match5_event,match5_time,match5_team1,match5_team2,
            )

            embed=discord.Embed(title="Next 5 Matches", description=msg, color=0x0069d2)
            embed.set_author(name="HLTV", url="https://www.hltv.org/", icon_url="https://pbs.twimg.com/profile_images/766575292441845760/ySDr_slD_400x400.jpg")
            await ctx.send(embed=embed)

    @hltv.command()
    async def top5(self, ctx):

        async with ctx.channel.typing():
                
            team_1 = '''
• {}
• {}
• {}
• {}
• {}
            '''.format(
                hltv.top30teams()[0]['team-players'][0]['name'],
                hltv.top30teams()[0]['team-players'][1]['name'],
                hltv.top30teams()[0]['team-players'][2]['name'],
                hltv.top30teams()[0]['team-players'][3]['name'],
                hltv.top30teams()[0]['team-players'][4]['name']
                )

            team_2 = '''
• {}
• {}
• {}
• {}
• {}
            '''.format(
                hltv.top30teams()[1]['team-players'][0]['name'],
                hltv.top30teams()[1]['team-players'][1]['name'],
                hltv.top30teams()[1]['team-players'][2]['name'],
                hltv.top30teams()[1]['team-players'][3]['name'],
                hltv.top30teams()[1]['team-players'][4]['name']
                )
            team_3 = '''
• {}
• {}
• {}
• {}
• {}
            '''.format(
                hltv.top30teams()[2]['team-players'][0]['name'],
                hltv.top30teams()[2]['team-players'][1]['name'],
                hltv.top30teams()[2]['team-players'][2]['name'],
                hltv.top30teams()[2]['team-players'][3]['name'],
                hltv.top30teams()[2]['team-players'][4]['name']
                )
            team_4 = '''
• {}
• {}
• {}
• {}
• {}
            '''.format(
                hltv.top30teams()[3]['team-players'][0]['name'],
                hltv.top30teams()[3]['team-players'][1]['name'],
                hltv.top30teams()[3]['team-players'][2]['name'],
                hltv.top30teams()[3]['team-players'][3]['name'],
                hltv.top30teams()[3]['team-players'][4]['name']
                )
            team_5 = '''
• {}
• {}
• {}
• {}
• {}
            '''.format(
                hltv.top30teams()[4]['team-players'][0]['name'],
                hltv.top30teams()[4]['team-players'][1]['name'],
                hltv.top30teams()[4]['team-players'][2]['name'],
                hltv.top30teams()[4]['team-players'][3]['name'],
                hltv.top30teams()[4]['team-players'][4]['name']
                )

            embed=discord.Embed(title="Current Top 5", description="", color=0x0069d2)
            embed.set_author(name="HLTV", url="https://www.hltv.org/", icon_url="https://pbs.twimg.com/profile_images/766575292441845760/ySDr_slD_400x400.jpg")
            embed.add_field(name=hltv.top5teams()[0], value=team_1, inline=False)
            embed.add_field(name=hltv.top5teams()[1], value=team_2, inline=False)
            embed.add_field(name=hltv.top5teams()[2], value=team_3, inline=False)
            embed.add_field(name=hltv.top5teams()[3], value=team_4, inline=False)
            embed.add_field(name=hltv.top5teams()[4], value=team_5, inline=False)
            await ctx.send(embed=embed)

    @hltv.command()
    async def top15(self, ctx):
        
        async with ctx.channel.typing():

            a = '''

**1.** {}
**2.** {}
**3.** {}
**4.** {}
**5.** {}
**6.** {}
**7.** {}
**8.** {}
**9.** {}
**10.** {}
**11.** {}
**12.** {}
**13.** {}
**14.** {}
**15.** {}
            '''.format(
                hltv.top30teams()[0]['name'],
                hltv.top30teams()[1]['name'],
                hltv.top30teams()[2]['name'],
                hltv.top30teams()[3]['name'],
                hltv.top30teams()[4]['name'],
                hltv.top30teams()[5]['name'],
                hltv.top30teams()[6]['name'],
                hltv.top30teams()[7]['name'],
                hltv.top30teams()[8]['name'],
                hltv.top30teams()[9]['name'],
                hltv.top30teams()[10]['name'],
                hltv.top30teams()[11]['name'],
                hltv.top30teams()[12]['name'],
                hltv.top30teams()[13]['name'],
                hltv.top30teams()[14]['name'],
                )

            embed=discord.Embed(title="Current Top 15", description=a, color=0x0069d2)
            embed.set_author(name="HLTV", url="https://www.hltv.org/", icon_url="https://pbs.twimg.com/profile_images/766575292441845760/ySDr_slD_400x400.jpg")
            
            await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(HLTVCog(bot))
