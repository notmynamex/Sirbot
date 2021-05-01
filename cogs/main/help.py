import discord
import logging
from discord.ext import commands
from utils import prefixes


async def prefix(self, ctx):
    result = await prefixes.get_prefix(self, ctx)
    if result is None:
        return self.bot.default_prefix
    else:
        return result


class HelpClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(invoke_without_command=True, case_insensitive=True, aliases=["he"])
    async def help(self, ctx):
        logging.info(f"Recieved help in {ctx.guild.name}")
        ctx.prefix = await prefix(self, ctx) # Needed in case the bot was mentioned for this command as ctx.prefix would be the bot's discord id
        embed = discord.Embed(
            title="Help",
            description=f"All of these commands use the ``{ctx.prefix}`` prefix\n<text> is a mandatory argument while [text] is an optional argument\nCommands with (NSFW) will only work within NSFW channels.",
            color=0x00A9E0
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(
            name="Sub Help Commands",
            value="""``help user`` | command and subcommands for the user command
            ``help update`` | valid fields for the user update subcommand
            ``help scoresaber`` | command and subcommands for the scoresaber command
            ``help neko`` | command and subcommands for the neko command""",
            inline=False
        )
        embed.add_field(
            name="General Commands",
            value="""``links`` | Posts important links for Sirbot
            ``amogus`` | <:amogus:826403430905937941>
            ``nhentai [ID]`` | Gets a doujin from nhentai, will be random if no ID is given. (NSFW)""",
            inline=False
        )
        embed.add_field(
            name="Admin Only Commands",
            value="""``set_prefix \"<prefix>\"`` | Changes Sirbot's prefix for this guild. __New prefix must be wrapped in ``"``s__""",
            inline=False
        )
        await ctx.reply(embed=embed)
        logging.info("Response: help embed")

    @help.command(aliases=["u"])
    async def user(self, ctx):
        logging.info(f"Recieved help user in {ctx.guild.name}")
        embed = discord.Embed(
            title="Help User",
            description=f"These are the valid arguments for ``{ctx.prefix}user",
            color=0x00A9E0)
        embed.add_field(
            name="user [mention]",
            value="get the info of a user",
            inline=False
        )
        embed.add_field(
            name="user add <ScoreSaber link>",
            value="add yourself to the userbase.",
            inline=False
        )
        embed.add_field(
            name="user update <field>",
            value=f"Update your info, use ``{ctx.prefix}help update`` for the fields and more info!",
            inline=False
        )
        embed.add_field(
            name="user remove",
            value="Removes you from the database",
            inline=False
        )
        await ctx.reply(embed=embed)
        logging.info("Response: help embed")
    
    @help.command(aliases=["up"])
    async def update(self, ctx):
        logging.info(f"Recieved help update in {ctx.guild.name}")
        embed = discord.Embed(
            title="Help User Update",
            description=f"These are the valid fields for ``{ctx.prefix}user update <field> <kwarg>``\nAny of these can be removed with ``user remove <field>``",
            color=0x00A9E0
        )
        embed.add_field(
            name="username <kwarg>",
            value="Updates your username.\nYou can put anything here, so go nuts",
            inline=False
        )
        embed.add_field(
            name="scoresaber/steam/twitch/youtube/twitter/reddit <kwarg>",
            value="Updates one of your links.\nUse a valid scoresaber link, otherwise the scoresaber command won't work!\nYou can go nuts with the other links though >w<",
            inline=False
        )
        message = ""
        for x in self.bot.valid_HMD:
            message = message + x + ", "
        embed.add_field(
            name="HMD <kwarg>",
            value=f"Updates your Head Mounted Display.\nValid arguments are: ``{message[:-2]}``",
            inline=False
        )
        embed.add_field(
            name="birthday <kwarg>",
            value="Updates your birthday.\nOnly the format of ``DD/MM`` or ``DD/MM/YYYY`` will be accepted",
            inline=False
        )
        embed.add_field(
            name="status <kwarg>",
            value="Updates your status.\nYou can put anything here, so go nuts",
            inline=False
        )
        embed.add_field(
            name="pfp <kwarg>",
            value="Updates your profile picture.\nMake sure this argument is a link going to an image!\nLil' secret: You can post a saved image to discord and use the link which discord generates.",
            inline=False
        )
        embed.add_field(
            name="colour <kwarg>",
            value="Updates your profile's embed colour\nMake sure to use a hex code. You can use a site [like this](https://www.color-hex.com/) to find the colour you want!",
            inline=False
        )
        await ctx.reply(embed=embed)
        logging.info("Response: help embed")

    @help.command(aliases=["ss"])
    async def scoresaber(self, ctx):
        logging.info(f"Recieved help scoresaber in {ctx.guild.name}")
        embed = discord.Embed(
            title="Help ScoreSaber",
            description=f"These are the valid arguments for ``{ctx.prefix}scoresaber``\n~~certainly not a bad ripoff of bs bot~~",
            color=0x00A9E0
        )
        embed.add_field(
            name="scoresaber [mention]",
            value="gets a user's ScoreSaber data,",
            inline=False
        )
        embed.add_field(
            name="scoresaber topsong [song number] [mention]",
            value="gets a user's top song from ScoreSaber. **Song number has to be given if mention is given**",
            inline=False
        )
        embed.add_field(
            name="scoresaber recentsong [song number] [mention]",
            value="gets a user's most recent song from ScoreSaber. **Song number has to be given if mention is given**",
            inline=False
        )
        embed.add_field(
            name="scoresaber topsongs [page] [mention]",
            value="gets a user's page of top songs from ScoreSaber. **Page has to be given if mention is given**",
            inline=False
        )
        embed.add_field(
            name="scoresaber recentsongs [page] [mention]",
            value="gets a user's page of recent songs from ScoreSaber. **Page has to be given if mention is given**",
            inline=False
        )
        embed.add_field(
            name="scoresaber compare <first user> [second user]",
            value="Compare two users together. excluse the second user argument if you only want to compare yourself against someone else.",
            inline=False
        )
        await ctx.reply(embed=embed)
        logging.info("Response: help embed")

    @help.command()
    async def neko(self, ctx):
        logging.info(f"Recieved help neko in {ctx.guild.name}")
        embed = discord.Embed(
            title="Help Neko",
            description=f"These are the valid arguments for ``{ctx.prefix}neko``",
            colour=0x00A9E0
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/754643335511015505/810691863610523668/unknown.png")
        embed.add_field(
            name="neko",
            value="Posts an image of a neko",
            inline=False
        )
        embed.add_field(
            name="neko gif",
            value="Posts a gif of a neko",
            inline=False
        )
        embed.add_field(
            name="neko lewd",
            value="Posts a lewd image of a neko. (NSFW)",
            inline=False
        )
        embed.add_field(
            name="neko lewd gif",
            value="Posts a lewd gif of a neko. (NSFW)",
            inline=False
        )
        await ctx.reply(embed=embed)
        logging.info("Response: help embed")


def setup(bot):
    bot.add_cog(HelpClient(bot))
