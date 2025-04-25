import hikari
import lightbulb

plugin = lightbulb.Plugin("avatar")

@plugin.command
@lightbulb.option("user", "enter user", hikari.Member, required=False)
@lightbulb.command("avatar", "get someone's avatar!")
@lightbulb.implements(lightbulb.SlashCommand)
async def _avatar(ctx):
    user = ctx.options.user
    if not user:
        user = ctx.author
    avatar = user.avatar_url
    await ctx.respond(avatar)

def load(bot):
    bot.add_plugin(plugin)
