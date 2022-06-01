async def send_plain(ctx, message:str, title:str=None):
    if title is None:
        title = str(ctx.command)
    return await ctx.message.edit(content=f"```ini\n[ {title} ]```\n```\n{message}```")