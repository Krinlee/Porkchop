import discord, os, random, asyncio, datetime, settings as settings
from discord.ext import commands, tasks
from settings import *
from trivia.Trivia_List import *
from config import secrets

logger = settings.logging.getLogger('trivia')

target_channel_id = secrets.bchan
utc = datetime.timezone.utc
time = datetime.time(hour=13, minute=5)




# Trivia loop
class tRivia(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.trivia.start()

    def cog_unload(self) -> None:
        self.trivia.stop()
        

    @tasks.loop(time=time)
    async def trivia(self):
        message_channel = self.bot.get_channel(int(target_channel_id))
        try:
            f = open(f'{TRIV_DIR}/question.txt', 'r')
            o_question = f.read()
            f.close()
            f = open(f'{TRIV_DIR}/answer.txt', 'r')
            o_answer = f.read()
            f.close()
            await message_channel.send(f"""@here Yesterday's question was:
            
            ¯\_(ツ)_/¯  {o_question}  ¯\_(ツ)_/¯""")
            await message_channel.send(f"""The answer is		(っ ͡ ͡º - ͡ ͡º ς)		 -> {o_answer} <-
        
        (人❛ᴗ❛)♪тнайк　чоц♪(❛ᴗ❛*人)""")
            await asyncio.sleep(10)
            pick = trivia_List[random.randint(0, 400)]
            question = pick[0]
            answer = pick[1]
            f = open(f'{TRIV_DIR}/question.txt', 'w')
            f.write(f"{question}")
            f.close()
            f = open(f'{TRIV_DIR}/answer.txt', 'w')
            f.write(f"{answer}")
            f.close
        except:
            pick = trivia_List[random.randint(0, 400)]
            question = pick[0]
            answer = pick[1]
            f = open(f'{TRIV_DIR}/question.txt', 'w')
            f.write(f"{question}")
            f.close()
            f = open(f'{TRIV_DIR}/answer.txt', 'w')
            f.write(f"{answer}")
            f.close
        # print(f"Trivia question --> {question} <-- posted to {message_channel}  --  The answer is -> {answer}")
        await message_channel.send("""@everyone 
        
        As always, post your answers to the trivia in the trivia-answers channel.

        (っ'ヮ'c)	The answer will be posted here on the next day before the next trivia question.""")
        await asyncio.sleep(3)
        await message_channel.send(f"""🧠	🧠	-> {question} <-	🧠	🧠
        
        (∩｀-´)⊃━☆ﾟ.*･｡ﾟ""")

        

    @trivia.before_loop
    async def before_trivia(self):
        # print("\nTrivia is good to go!\n")
        await self.bot.wait_until_ready()

    
async def setup(bot):
    await bot.add_cog(tRivia(bot))








    

