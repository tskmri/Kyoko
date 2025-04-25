import lightbulb
import hikari

plugin = lightbulb.Plugin('ready')


@plugin.listener(hikari.StartedEvent)
async def on_ready(event):
    print("Ready to go!")


def load(bot):
    bot.add_plugin(plugin)
