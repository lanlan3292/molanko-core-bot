from core.context import BotContext
from core.commands.version.version import VersionService
from utils.i18n import t


class VersionCommand:
    def __init__(self, service: VersionService | None = None):
        self.service = service or VersionService()

    async def execute(self, ctx: BotContext) -> None:
        info = self.service.get_version()

        message = t(
            "version.response",
            locale=ctx.locale,
            version=info.version,
        )
        # message = f"Current version: **{info.version}**"

        await ctx.reply(message)