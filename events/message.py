import lightbulb
import hikari

plugin = lightbulb.Plugin("message")

@plugin.listener(hikari.GuildMessageCreateEvent)
async def delete_event(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return

    if "https://tenor.com/view/frog-eating-frog-frog-eating-gif-23919880" in event.content:
        await event.message.delete()

def load(bot):
    bot.add_plugin(plugin)
