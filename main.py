import lightbulb
import hikari
import os
from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.environ.get("TOKEN")

client = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=[790491469512179712, 1169146038913859606]
)

client.load_extensions_from("./commands")

client.load_extensions_from("./events")

client.sync_application_commands()

client.run(
    # status=hikari.Status.IDLE,
    activity=hikari.Activity(
        name="FINAL FANTASY XIV",
        type=hikari.ActivityType.PLAYING,
    )
)