# Code has been removed in certain parts of the project. For more information read "READ ME" file

import discord
from discord.ext import commands
import random
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "~", intents = intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")    # To let us know the bot is up and running.

@bot.command(aliases = ['info'])
async def information(ctx):
    embedVariable = discord.Embed(title = "**__About Me__**", description = "Born in 2022", color = 0xe74c3c)
    embedVariable.add_field(name = "Creator:", value = "<@!742303014483787847>", inline = False)
    embedVariable.add_field(name = "Type:", value = "General, Fun and Informative Bot", inline = False)
    embedVariable.add_field(name = "Number of commands:", value = "6")
    embedVariable.set_author(name = "Shadow's Bot", icon_url = bot.user.avatar.url)

    await ctx.send(embed = embedVariable)

@bot.command(aliases = ["cmdlist", "cmds"])
async def commandlist(ctx):
    embedVariable = discord.Embed(title = "Command List", description = "All available commands", color = 0xe74c3c)
    embedVariable.add_field(name = "~information", value = "Displays this.\nAlias: ~info", inline = False)
    embedVariable.add_field(name = "~commandlist", value = "Displays all commands.\nAliases: cmdlist, cmds", inline = False)
    embedVariable.add_field(name = "~poll [question] [options]", value = "Create a poll with 2 or more options.\nOptions with more than one words to be enclosed in \"\".", inline = False)
    embedVariable.add_field(name = "~rps", values = "Rock Paper Scissors game", inline = False)
    embedVariable.add_field(name = "~joke", value = "Get a random joke.", inline = False)
    embedVariable.add_field(name = "~translate [language] [text]", value = "Translate text from English to a specified language", inline = False)


class Poll(discord.ui.View):
    def __init__(self, options, timeout = 60):
        super().__init__(timeout = timeout)
        # Code has been removed here.

    def create_vote_callback(self, option):
        async def vote_callback(interaction: discord.Interaction):
            if self.poll_ended:
                await interaction.response.send_message("This poll has ended.", ephemeral = True)
                return
            self.votes[option] += 1
            await interaction.response.send_message(f"You voted for {option}!", ephemeral = True)
        return vote_callback

    async def end_poll(self, poll_message):
        # Code has been removed here.

@bot.command()
async def poll(ctx, question: str, *options: str):
    if len(options) < 2:
        await ctx.send("You need at least two options for a poll!")
        return
    if len(options) > 5:
        await ctx.send("You can only have up to 5 options in a poll.")
        return

    # Code has been removed here.

@bot.command()
async def translate(ctx, language, *, text):
    translator = Translator()
    # Code has been removed here.

class RPS(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    def embedFn(self, result, uC, bC):
        self.choice = {"rock": "🪨", "paper": "📃", "scissors": "✂️"}
        # Code has been removed here.

    def game(self, userChoice):
        self.choices = ["rock", "paper", "scissors"]
        self.botChoice = random.choice(self.choices)
        # Code has been removed here.
        
        return self.embedFn(self.result, userChoice, self.botChoice)

    @discord.ui.button(style = discord.ButtonStyle.gray, row = 0, emoji = "🪨")
    # Code has been removed here.

@bot.command()
async def rps(ctx):
    view = RPS()
    embedVariable = discord.Embed(title = "Rock-Paper-Scissors", color = 0xe74c3c)
    # Code has been removed here.

@bot.command()
async def joke(ctx):
    jokes = ["Why did the chicken cross the road? To get to the other side.", 
             "Why did the tomato turn red? It saw the salad dressing.", 
             "Why did the scarecrow win an award? He was outstanding in his field.",
             "My friend claims that he scaled Mount Everest! But no one believes him. I think.. he made it up",
             "What do coders use when they get a rash? An app-ointment",
             "What do computers eat for snacks? Microchips...... One byte at a time"]
  # You can add more jokes if you want.

    await ctx.send(random.choice(jokes))

TOKEN = "<insert your bot's token here>"
bot.run(TOKEN)
