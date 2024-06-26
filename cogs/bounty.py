from discord.ext import commands
from discord import (
    SelectOption,
    ui,
    Button,
    ButtonStyle,
    Interaction,
    app_commands,
)
import asyncio
from typing import Final

### Bounty command class ###
class Bounty(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        #self.client.tree.add_command(BountyGroup())

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Cog Bounty is ready")


async def setup(client: commands.Bot):
    await client.add_cog(Bounty(client))