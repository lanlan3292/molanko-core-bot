from core.context import BotContext


class WhoAmICommand:
    async def execute(self, ctx: BotContext) -> None:
        user = ctx.user
        message = f"{user.name} `{user.id}`"
        await ctx.reply(message)
