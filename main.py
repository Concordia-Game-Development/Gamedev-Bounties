from typing import Final
import os, asyncio
from dotenv import load_dotenv
from discord import Intents, Client, Message, Embed, File, app_commands, Interaction
from discord.ext import commands

# Load environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
extensions: Final[list[str]] = ["cogs.bounty"]

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True
intents.voice_states = True
client: Client = commands.Bot(intents=intents, help_command=None, command_prefix="!")

# Define a tree for slash commands
tree = client.tree


#Load cogs
async def loadCogs() -> None:
   for extension in extensions:
       await client.load_extension(extension)


# Event: Bot is ready
@client.event
async def on_ready() -> None:
    print(f"{client.user} has connected to Discord!")


# Help Commands
@tree.command(name="help", description="Display all available commands")
async def help(interaction: Interaction) -> None:
    file = File("img/controller_icon.png", filename="controller_icon.png")
    help_embed = Embed(
        title="How to use CGD Gamedev Bounty Board",
        description="List of available commands:",
        color=0xCF3A65,
        timestamp=interaction.created_at,
    )
    help_embed.set_thumbnail(url="attachment://controller_icon.png")
    help_embed.add_field(
        name="/help", value="Display all available commands", inline=True
    )
    help_embed.add_field(
        name="/addBounty",
        value="Add a game dev bounty using the interactions",
        inline=True,
    )
    help_embed.add_field(
        name="/deleteQueue",
        value="Deletes all bounties from the queue",
        inline=True,
    )
    await interaction.response.send_message(file=file, embed=help_embed)

# Sync commands
@client.command(name="sync", description="Sync commands with Discord")
async def sync(ctx) -> None:
    await client.tree.sync()
    await ctx.reply("Commands synced with Discord!", ephemeral=True)

# Main entry point
async def main() -> None:
    await loadCogs()
    await client.start(token=TOKEN)


if __name__ == "__main__":
    asyncio.run(main())