import discord, datetime, json
from discord.ext import commands

myid = 301014178703998987

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.remove_command("help")
tree = client.tree

dbdir = "db.json"

@client.event
async def on_ready():
    print(f"SS Automation now online with {round(client.latency * 1000)}ms latency.")

@tree.command(name="test", description="desc")
async def test(interaction : discord.Interaction):
    embed = discord.Embed(
        title = "Test Command",
        colour = 0x948365,
        description = "eyo wassup bbg ahahaha",
        timestamp = datetime.datetime.utcnow() - datetime.timedelta(seconds=18000)
    )
    embed.add_field(name="Wassup daddy Goleros ahaha", value="please read my fletc app")
    embed.set_author(name="made by Gytis5089 (you can click this)", url="https://www.pornhub.com/gay", icon_url="https://i.ibb.co/qn4MM0W/CAT-Logo.png")
    embed.set_footer(text="footer ahaha", icon_url="https://i.ibb.co/P5hXfbL/Logo-White-NBG.png")
    embed.set_image(url="https://i.ibb.co/QcMG1jm/Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/0nGm5Kv/UD-Logo.png")
    await interaction.response.send_message(embed=embed, ephemeral=True)

points = discord.app_commands.Group(name="points", description="All things points related")
tree.add_command(points)

@points.command(name="check", description="Check your or another user's current points")
async def pointscheck(interaction : discord.Interaction, user : discord.Member = None):
    if not user:
        user = interaction.user
    with open(dbdir, "r+") as f:
        data = json.load(f)
        if str(user.id) in data:
            points = data[str(user.id)]
        else:
            data[str(user.id)] = 0
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=4)
            points = 0
    embed = discord.Embed(
        title=f"{user.name}#{user.discriminator}",
        colour=0x948365,
        description=f"Has `{points}` points"
    )
    embed.set_thumbnail(url=user.display_avatar.url)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@points.command(name="add", description="Add points to a user")
async def pointadd(interaction : discord.Interaction, user : discord.Member, amount : int):
    with open(dbdir, "r+") as f:
        data = json.load(f)
        if str(user.id) in data:
            data[str(user.id)] = data[str(user.id)] + amount
            points = data[str(user.id)]
        else:
            data[str(user.id)] = amount
            points = amount
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
    embed = discord.Embed(
        title=f"{user.name}#{user.discriminator}",
        colour=0x32a858,
        description=f"Has been awarded `{amount}` points\nThey are now at `{points}` points",
        timestamp = datetime.datetime.utcnow() - datetime.timedelta(seconds=18000)
    )
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text=f"{interaction.user.name}#{interaction.user.id}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@points.command(name="remove", description="Remove points from a user")
async def pointremove(interaction : discord.Interaction, user : discord.Member, amount : int):
    with open(dbdir, "r+") as f:
        data = json.load(f)
        if str(user.id) in data:
            if data[str(user.id)] - amount < 0:
                points = data[str(user.id)]
                low = True
            else:
                data[str(user.id)] = data[str(user.id)] - amount
                points = data[str(user.id)]
                low = False
        else:
            points = data[str(user.id)]
            low = True
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
    embed = discord.Embed(
        title=f"{user.name}#{user.discriminator}",
        colour=0x948365,
        description="",
        timestamp = datetime.datetime.utcnow() - datetime.timedelta(seconds=18000)
    )
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text=f"{interaction.user.name}#{interaction.user.id}", icon_url=interaction.user.display_avatar.url)
    if not low:
        embed.colour = 0x32a858
        embed.description = f"Has had `{amount}` points removed\nThey are now at `{points}` points"
    else:
        embed.colour = 0xa83232
        embed.description = f"Doesn't have that many points\nThey are still at `{points}` points"
    await interaction.response.send_message(embed=embed, ephemeral=True)

@points.command(name="set", description="Set a user's points")
async def pointset(interaction : discord.Interaction, user : discord.Member, amount : int):
    with open(dbdir, "r+") as f:
        data = json.load(f)
        data[str(user.id)] = amount
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
    embed = discord.Embed(
        title=f"{user.name}#{user.discriminator}",
        colour=0x32a858,
        description=f"Has had their points set to `{amount}`",
        timestamp = datetime.datetime.utcnow() - datetime.timedelta(seconds=18000)
    )
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text=f"{interaction.user.name}#{interaction.user.id}", icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed, ephemeral=True)

@client.command()
@commands.check(lambda ctx : ctx.author.id == myid)
async def connect(ctx):
    await tree.sync()

client.run("MTExMzkwMjUwNjg1MDkzMDgzMQ.GF-nvu.topdf1nrZrbu1Nbfw6UgrKB_OiUJI6zoTuXlks")
#https://discord.com/api/oauth2/authorize?client_id=1113902506850930831&permissions=8&scope=bot

#Green - 0x32a858
#Red - 0xa83232
#Blue - 0x325fa8
#Beige - 0x948365