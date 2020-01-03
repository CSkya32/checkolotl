import os

import checkolotl.utils.discord.webhook as webhook
from checkolotl.settings import settings


def start():
    if settings.events.discord_webhook_url and settings.events.on_start.discord.enabled:
        webhook.start()
    if settings.events.on_start.command:
        os.system(settings.events.on_start.command)
