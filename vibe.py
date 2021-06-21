import discord
from discord.ext import commands, tasks
import typing
import asyncio
import pymongo
import random
import datetime
from vibeclass import vibes
import os
import calendar

intents = discord.Intents.all()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix=["V!", "v!"], intents=intents, case_insensitive=True, status=discord.Status.online,
                   activity=discord.Activity(name='v!help', type=discord.ActivityType.watching))
vibes = vibes(bot)
bot.remove_command('help')
client = pymongo.MongoClient(
    "connection strings for mongo",
    connect=False)
db = client.user
experience = db.exp
blacklisted = db.blacklist
voice_exp = db.voiceexp
db = client.leaderboardboth
lb_both_day = db.day
lb_both_week = db.week
lb_both_month = db.month
db = client.leaderboardtext
lb_text_day = db.day
lb_text_week = db.week
lb_text_month = db.month
db = client.leaderboardvoice
lb_voice_day = db.day
lb_voice_week = db.week
lb_voice_month = db.month
db = client.leaderboard
max_leaderboard = db.lb

clientV2 = pymongo.MongoClient(
    "another connection string",
    connect=False)
dbs = clientV2.Users
coins = dbs.Coins

def coins_lvl(user,lvl: int):
    return_coins = 0
    for i in range(0, lvl):
        return_coins = return_coins + 5
    person = coins.find_one({"user":user})
    if person:
        og = person.get('coins')
        og = int(og)
        new_coins = og + return_coins
        coins.update_one({'user': user}, {"$set": {"coins": new_coins}})
    else:
        coins.insert_one({"user":user,"coins":coins})



def delete_from_all(id):
    experience.delete_one({'user': id})
    max_leaderboard.delete_one({'user': id})
    voice_exp.delete_one({'user': id})
    lb_both_day.delete_one({'user': id})
    lb_both_week.delete_one({'user': id})
    lb_both_month.delete_one({'user': id})
    lb_text_day.delete_one({"user": id})
    lb_text_week.delete_one({'user': id})
    lb_text_month.delete_one({'user': id})
    lb_voice_day.delete_one({'user': id})
    lb_voice_week.delete_one({'user': id})
    lb_voice_month.delete_one({'user': id})


def insert_into_text(id: int, exp: int):
    og_exp = exp
    info = lb_both_day.find_one({'user': id})
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_both_day.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_both_day.insert_one({'user': id, 'exp': exp})
    info = lb_both_week.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_both_week.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_both_week.insert_one({'user': id, 'exp': exp})
    info = lb_both_month.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_both_month.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_both_month.insert_one({'user': id, 'exp': exp})
    info = lb_text_day.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_text_day.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_text_day.insert_one({'user': id, 'exp': exp})
    info = lb_text_week.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_text_week.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_text_week.insert_one({'user': id, 'exp': exp})
    info = lb_text_month.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_text_month.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_text_month.insert_one({'user': id, 'exp': exp})


def insert_into_voice(id: int, exp: int):
    og_exp = exp
    info = lb_both_day.find_one({'user': id})
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_both_day.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_both_day.insert_one({'user': id, 'exp': exp})
    info = lb_both_week.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_both_week.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_both_week.insert_one({'user': id, 'exp': exp})
    info = lb_both_month.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_both_month.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_both_month.insert_one({'user': id, 'exp': exp})
    info = lb_voice_day.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_voice_day.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_voice_day.insert_one({'user': id, 'exp': exp})
    info = lb_voice_week.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_voice_week.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_voice_week.insert_one({'user': id, 'exp': exp})
    info = lb_voice_month.find_one({'user': id})
    exp = og_exp
    if info:
        last_exp = info.get('exp')
        last_exp = int(last_exp)
        exp = exp + last_exp
        lb_voice_month.update_one({'user': id}, {"$set": {"exp": exp}})
    else:
        lb_voice_month.insert_one({'user': id, 'exp': exp})


boosted_exp = 1
vc_boosted_exp = 1
cooldown = {}


def level_max(lvl: int) -> str:
    return_lvl = 100
    for i in range(0, lvl):
        return_lvl = return_lvl + 75
    return_lvl = str(return_lvl)
    return return_lvl


def value_check(user: int) -> bool:
    for people in cooldown.keys():
        people = int(people)
        if people == user:
            return True
    return False


def lvl_up_txt(lvl: int) -> str:
    if lvl == 1:
        return '**Nice!** Level 1. Keep vibing, you\'re on the right path!'
    if lvl == 2:
        return "**Good Vibes!** Keep going! Level 2, halfway there!"
    if lvl == 3:
        return "**Poggies!** Level 3! More than halfway! Let's keep going!"
    if lvl == 4:
        return "**Ooo yeah!** Level 4! Almost there!"
    if lvl == 5:
        return "**Mega poggies!** You're now level 5! Next step, become a viber!"
    if lvl >= 6 and lvl <= 9:
        return "One step closer to becoming a viber, **keep it up!**"
    if lvl == 10:
        return " **Woo-hoo! Finally!** You've become a viber! Don't stop there!"
    if lvl >= 11 and lvl <= 14:
        return "**You're doing great!** Steadily becoming a better viber!"
    if lvl == 15:
        return " **Gasp!** You're starting to know how to vibe!"
    if lvl >= 16 and lvl <= 19:
        return "**Nice!!** You're getting pretty good at this!"
    if lvl == 20:
        return " **Cool!** Your pretty talented, do you have what it takes to become a pro?"
    if lvl >= 21 and lvl <= 24:
        return "**Wow!** Slow but steady progress, to becoming at pro! "
    if lvl == 25:
        return "**Awesome!** You're a professional! Let's go even higher!"
    if lvl >= 26 and lvl <= 29:
        return "**Hmm...** I wonder what's next?"
    if lvl == 30:
        return "**Woah!** You've ascended! No more viber, you're literally Vibing!"
    if lvl >= 31 and lvl <= 34:
        return "**Huh?** Something feels different..."
    if lvl == 35:
        return "**Interesting...** Seems like you've gotten so good that you are literally one with The Vibe."
    if lvl >= 36 and lvl <= 39:
        return "**Eep!** You're transforming, the question is, into what?"
    if lvl == 40:
        return " **Oooh!** You're like a Mega Evolution of the Vibeling!"
    if lvl >= 41 and lvl <= 44:
        return "**Again?!** How much more can you improve?"
    if lvl == 45:
        return "**Hrm...** This is crazy! You're a vibe...but with 2 e's?"
    if lvl >= 46 and lvl <= 49:
        return "**Woo!** I'm excited to see what's next! What could possibly be higher?"
    if lvl == 50:
        return "**Wowie!** You're super social! Halfway to... perfection?"
    if lvl >= 51 and lvl <= 59:
        return "**Amazing!** I never expected you to get this far, keep it up!"
    if lvl == 60:
        return "**Wow!** You're in a whole new universe!"
    if lvl >= 61 and lvl <= 68:
        return "**Let's go!** Each step is closer to success!"
    if lvl == 69:
        return "**Noice!** LOL you reached the \"haha funny\" number!"
    if lvl == 70:
        return "**Incredible!** Your giving off the best vibes! But I'm sure you can aim for higher!"
    if lvl >= 71 and lvl <= 79:
        return "**Concentrate!** I sense a strong force approaching..."
    if lvl == 80:
        return "**Sweet!** I didn't even know this was possible! You're a legend!"
    if lvl >= 81 and lvl <= 89:
        return "**Amazing!** You're really on your grind! Reach for the stars!"
    if lvl == 90:
        return "**Crazy!!** I'm slightly concerned..But..go plus ultra!!"
    if lvl >= 91 and lvl <= 99:
        return "**Phew..** Keep going...Stay strong, you're almost at 100!!"
    if lvl == 100:
        return "**Nani?!** You're knowledge of vibing is impeccable! Almost to perfection..."
    if lvl >= 101 and lvl <= 199:
        return "**You got this.** You're really good. Maybe the best. And that's why it's so hard to go higher. But you just keep trying, because that's the way you are."
    if lvl == 200:
        return "**Wow...** You reached 200... You are worthy of becoming a god!"
    if lvl >= 201 and lvl <= 248:
        return "**Stellar!** Each step, a closer reach to becoming the perfect being... It'll get harder..But..you'll make it."
    if lvl == 249:
        return "**Hmm..** You feel a great power coursing through your veins. "
    if lvl == 250:
        return "**Incredible!** Oh my god! You literally are a god! A being of perfection!"
    if lvl >= 251:
        return "The results of hard work and dedication really do show. You've made a great impact on others. Your journey might end here, or it might not. But just know you've earned every ounce of your success."


def roles_add(lvl: int):
    if lvl == 1:
        return 785974298178355232, None
    elif lvl == 5:
        return 785974298665680897, 785974298178355232
    elif lvl == 10:
        return 785974300246802473, 785974298665680897
    elif lvl == 15:
        return 785974301077667880, 785974300246802473
    elif lvl == 20:
        return 785974301874323466, 785974301077667880
    elif lvl == 25:
        return 785974302549344268, 785974301874323466
    elif lvl == 30:
        return 785974303408652329, 785974302549344268
    elif lvl == 35:
        return 785974303710511115, 785974303408652329
    elif lvl == 40:
        return 785974304709017650, 785974303710511115
    elif lvl == 45:
        return 785974305501872208, 785974304709017650
    elif lvl == 50:
        return 785974305946206209, 785974305501872208
    elif lvl == 60:
        return 841785721504530432, 785974305946206209
    elif lvl == 70:
        return 785974306508898345, 841785721504530432
    elif lvl == 80:
        return 785978380553945128, 785974306508898345
    elif lvl == 90:
        return 785978381526761503, 785978380553945128
    elif lvl == 100:
        return 785978382054719540, 785978381526761503
    elif lvl == 250:
        return 785978394591756288, 785978382054719540
    else:
        return None, None


all_roles_dict = [785974298178355232, 785974298665680897, 785974300246802473, 785974301077667880, 785974301874323466,
                  785974302549344268, 785974303408652329,
                  785974303710511115, 785974304709017650, 785974305501872208, 785974305946206209, 841785721504530432,
                  785974306508898345, 785978380553945128,
                  785978381526761503, 785978382054719540, 785978394591756288]

all_roles_json = {785974298178355232: 1, 785974298665680897: 5, 785974300246802473: 10, 785974301077667880: 15,
                  785974301874323466: 20,
                  785974302549344268: 25, 785974303408652329: 30, 785974303710511115: 35, 785974304709017650: 40,
                  785974305501872208: 45
    , 785974305946206209: 50, 841785721504530432: 60, 785974306508898345: 70, 785978380553945128: 80,
                  785978381526761503: 90,
                  785978382054719540: 100, 785978394591756288: 250}


@bot.event
async def on_ready():
    print(f'{bot.user} is online.')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.CommandOnCooldown):
        return
    else:
        channel = bot.get_channel(840627525994151958)
        await channel.send(f'<@705992469426339841> | {ctx.author.mention} : {error}')
        await ctx.send(error)

@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency}')


@bot.event
async def on_member_leave(member):
    experience.delete_one({'user': member.id})
    delete_from_all(member.id)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    global boosted_exp
    blacklist_channel = blacklisted.find_one({'channel': message.channel.id})
    if blacklist_channel != None:
        return
    else:
        if message.author.bot == False:
            check = message.content.startswith("V!")
            if check:
                return
            check = message.content.startswith("v!")
            if check:
                return
            else:
                exp = random.randint(1, 3) * boosted_exp
                insert_into_text(message.author.id, exp)
                info = {'user': message.author.id}
                user = experience.find_one(info)
                if user == None:
                    info = {'user': message.author.id, 'level': 0, 'exp': exp}
                    experience.insert_one(info)
                else:
                    user_exp = user.get('exp')
                    user_lvl = user.get('level')
                    exp = user_exp + exp
                    levelmax = level_max(user_lvl)
                    levelmax = int(levelmax)
                    user_exp = int(user_exp)
                    ctx = bot.get_channel(841836241313464351)
                    if user_exp >= levelmax:
                        new_lvl = user_lvl + 1
                        text = lvl_up_txt(new_lvl)
                        embed = discord.Embed(title=f"{message.author}", color=0x00fff6)
                        embed.add_field(name=f'Level {new_lvl}', value=f'{text}')
                        embed.set_thumbnail(url=message.author.avatar_url)
                        embed.timestamp = datetime.datetime.utcnow()
                        await ctx.send(message.author.mention, embed=embed)
                        find = max_leaderboard.find_one({'user': message.author.id})
                        if find == None:
                            max_leaderboard.insert_one({'user': message.author.id, 'level': 1})
                            #coins_lvl(message.author.id,1)
                            add, remove = roles_add(1)
                            if add == None:
                                pass
                            else:
                                guild = bot.get_guild(776822249314582538)
                                og_role = guild.get_role(add)
                                await message.author.add_roles(og_role)
                                if remove == None:
                                    pass
                                else:
                                    bruh = guild.get_role(remove)
                                    await message.author.remove_roles(bruh)
                        else:
                            x = find.get('level')
                            x = int(x)
                            x = x + 1
                            #coins_lvl(message.author.id, x)
                            max_leaderboard.update_one({'user': message.author.id}, {'$set': {'level': x}})
                            add, remove = roles_add(x)
                            if add == None:
                                pass
                            else:
                                guild = bot.get_guild(776822249314582538)
                                og_role = guild.get_role(add)
                                if remove == None:
                                    pass
                                else:
                                    bruh = guild.get_role(remove)
                                    await message.author.remove_roles(bruh)
                                    await message.author.add_roles(og_role)
                        experience.update_one({"user": message.author.id}, {"$set": {"exp": 0, 'level': new_lvl}})
                    else:
                        experience.update_one({"user": message.author.id}, {"$set": {"exp": exp}})
                        cooldown[f'{message.author.id}'] = 1
                        await asyncio.sleep(5)
                        try:
                            cooldown.pop(f'{message.author.id}')
                        except Exception as e:
                            return


@bot.command(hidden=True)
async def leveldeletion(ctx, user: discord.User):
    if ctx.author.id == 705992469426339841:
        delete_from_all(user.id)
        await ctx.send('successfully delete user\'s levels')


@bot.command(hidden=True)
async def day(ctx):
    if ctx.author.id == 705992469426339841:
        x = lb_both_day.find()
        for info in x:
            user = info.get('user')
            lb_both_day.delete_one({'user': user})
        x = lb_voice_day.find()
        for info in x:
            user = info.get('user')
            lb_voice_day.delete_one({'user': user})
        x = lb_text_day.find()
        for info in x:
            user = info.get('user')
            lb_text_day.delete_one({'user': user})

def day_delete():
    x = lb_both_day.find()
    for info in x:
        user = info.get('user')
        lb_both_day.delete_one({'user': user})
    x = lb_voice_day.find()
    for info in x:
        user = info.get('user')
        lb_voice_day.delete_one({'user': user})
    x = lb_text_day.find()
    for info in x:
        user = info.get('user')
        lb_text_day.delete_one({'user': user})


@bot.command(hidden=True, aliases=['week'])
async def weekly(ctx):
    if ctx.author.id == 705992469426339841:
        x = lb_both_week.find()
        for info in x:
            user = info.get('user')
            lb_both_week.delete_one({'user': user})
        x = lb_voice_week.find()
        for info in x:
            user = info.get('user')
            lb_voice_week.delete_one({'user': user})
        x = lb_text_week.find()
        for info in x:
            user = info.get('user')
            lb_text_week.delete_one({'user': user})

def weekly_delete():
    x = lb_both_week.find()
    for info in x:
        user = info.get('user')
        lb_both_week.delete_one({'user': user})
    x = lb_voice_week.find()
    for info in x:
        user = info.get('user')
        lb_voice_week.delete_one({'user': user})
    x = lb_text_week.find()
    for info in x:
        user = info.get('user')
        lb_text_week.delete_one({'user': user})


@bot.command(hidden=True, aliases=['month'])
async def monthly(ctx):
    if ctx.author.id == 705992469426339841:
        x = lb_both_month.find()
        for info in x:
            user = info.get('user')
            lb_both_month.delete_one({'user': user})
        x = lb_voice_month.find()
        for info in x:
            user = info.get('user')
            lb_voice_month.delete_one({'user': user})
        x = lb_text_month.find()
        for info in x:
            user = info.get('user')
            lb_text_month.delete_one({'user': user})


@bot.command(aliases=['lvl', 'exp', 'xp', 'profile'])
async def level(ctx, person: discord.User = None):
    if person == None:
        person = ctx.author
    async with ctx.channel.typing():
        await asyncio.sleep(2)
    user = experience.find_one({'user': person.id})
    exp = user.get('exp')
    level = user.get('level')
    next_level = level + 1
    needed_exp = level_max(level)
    needed_exp = int(needed_exp)
    final_exp = needed_exp - exp
    embed = discord.Embed(title=f'{person.name} experience points',
                          description=f'You are level {level} |  {exp}/{needed_exp}', color=0x00fff6)
    user = voice_exp.find_one({'user': person.id})
    if user != None:
        level = user.get('level')
        exp = user.get('exp')
        x = level_max(level)
        embed.add_field(name=f'\u200b', value=f'Your voice level {level} | {exp}/{x}')
    embed.set_footer(text=f'You need {final_exp} more experience points to get to level {next_level}')
    await ctx.send(embed=embed)


@bot.command(hidden=True)
@commands.has_permissions(administrator=True)
async def blacklist(ctx, type, channel: typing.Union[discord.TextChannel, discord.VoiceChannel]):
    type = type.lower()
    channel = bot.get_channel(channel.id)
    if channel == None:
        await ctx.send('Error: Please put in a valid discord TextChannel/VoiceChannel.')
    else:
        if_existing = blacklisted.find_one({'channel': channel.id})
        if type == 'add':
            if if_existing == None:
                blacklisted.insert_one({'channel': channel.id})
                await ctx.send(f'Successfully added <#{channel.id}> to the blacklist.')
            else:
                await ctx.send('Error: That channel is already blacklisted from gaining exp.')
        elif type == 'remove':
            if if_existing != None:
                blacklisted.delete_one({'channel': channel.id})
                await ctx.send(f'Successfully removed <#{channel.id}> from the blacklist')
            else:
                await ctx.send(f'Error: <#{channel.id} has not been blacklisted.')
        else:
            await ctx.send('Error: Blacklist types are Add, Remove.')


@blacklist.error
async def blacklist_error(ctx, error):
    if isinstance(error, commands.BadUnionArgument):
        await ctx.send('Error: Please put in a valid discord TextChannel/VoiceChannel.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('Error: You dont have the required permmsions to use this command.')
    else:
        print(error)


@bot.command(aliases=['multi'])
@commands.has_permissions(administrator=True)
async def multiplier(ctx, type, number: int):
    type = type.lower()
    global boosted_exp
    global vc_boosted_exp
    if number < 1:
        number = 1
    if type == 'vc' or type == 'voice':
        await ctx.send(f'The exp multiplier for vc\'s has been set to {number}')
        vc_boosted_exp = number
    elif type == 'txt' or type == 'text':
        await ctx.send(f'The exp multiplier for text has been set to {number}')
        boosted_exp = number
    else:
        await ctx.send('Error: The supported types are; vc, voice, txt, text')


@bot.command()
@commands.has_permissions(administrator=True)
async def add(ctx, user: discord.Member, type, amount: int):
    type = type.lower()
    if type == 'txt' or type == 'txt':
        data = experience.find_one({'user': user.id})
        level = data.get('level')
        level = level + amount
        experience.update_one({"user": user.id}, {"$set": {"level": level}})
        data = max_leaderboard.find_one({'user': user.id})
        if data == None:
            max_leaderboard.insert_one({'user': user.id, 'level': amount})
        else:
            l = data.get('level')
            l = l + amount
            max_leaderboard.update_one({'user': user.id}, {'$set': {'level': l}})
        await ctx.send(f'successfully added {amount} text levels to {user}')
    elif type == 'vc' or type == 'voice':
        data = voice_exp.find_one({'user': user.id})
        level = data.get('level')
        level = level + amount
        voice_exp.update_one({"user": user.id}, {"$set": {"level": level}})
        data = max_leaderboard.find_one({'user': user.id})
        if data == None:
            max_leaderboard.insert_one({'user': user.id, 'level': amount})
        else:
            l = data.get('level')
            l = l + amount
            max_leaderboard.update_one({'user': user.id}, {'$set': {'level': l}})
        await ctx.send(f'successfully added {amount} voice levels to {user}')
    else:
        await ctx.send('Error: The valid types are vc,voice,txt, or text')


@bot.command()
@commands.has_permissions(administrator=True)
async def remove(ctx, user: discord.Member, type, amount: int):
    type = type.lower()
    if type == 'txt' or type == 'text':
        data = experience.find_one({'user': user.id})
        level = data.get('level')
        level = level - amount
        experience.update_one({"user": user.id}, {"$set": {"level": level}})
        data = max_leaderboard.find_one({'user': user.id})
        l = data.get('level')
        l = l - amount
        max_leaderboard.update_one({'user': user.id}, {'$set': {'level': l}})
        await ctx.send(f'successfully removed {amount} text levels from {user}')
    elif type == 'vc' or type == 'voice':
        data = voice_exp.find_one({'user': user.id})
        level = data.get('level')
        level = level - amount
        voice_exp.update_one({"user": user.id}, {"$set": {"level": level}})
        data = max_leaderboard.find_one({'user': user.id})
        l = data.get('level')
        l = l - amount
        max_leaderboard.update_one({'user': user.id}, {'$set': {'level': l}})
        await ctx.send(f'successfully removed {amount} voice levels from {user}')
    else:
        await ctx.send('Error: The valid types are vc,voice,txt, or text')


@bot.command()
@commands.has_permissions(administrator=True)
async def set(ctx, user: discord.Member, type, amount: int):
    type = type.lower()
    if type == 'txt' or type == 'text':
        experience.update_one({"user": user.id}, {"$set": {"level": amount}})
        x = voice_exp.find_one({'user': user.id})
        x = x.get('level')
        x = int(x) + amount
        max_leaderboard.update_one({'user': user.id}, {"$set": {'level': x}})
        await ctx.send(f'user now only has {amount} text levels ')
    if type == 'voice' or type == 'vc':
        voice_exp.update_one({"user": user.id}, {"$set": {"level": amount}})
        x = experience.find_one({'user': user.id})
        x = x.get('level')
        x = int(x) + amount
        max_leaderboard.update_one({'user': user.id}, {"$set": {'level': x}})
        await ctx.send(f'user now only has {amount} voice levels ')
    else:
        await ctx.send('Error: The valid types are vc,voice,txt, or text')


@bot.command()
async def rank(ctx):
    embed = discord.Embed(title=f'{ctx.author}\'s ranks', color=0x00fff6)
    async with ctx.channel.typing():
        all = max_leaderboard.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                both_alltime_count = count
                break
            else:
                count = count + 1
        all = experience.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                text_alltime_count = count
                break
            else:
                count = count + 1
        all = voice_exp.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                voice_alltime_count = count
                break
            else:
                count = count + 1
        all = lb_text_day.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                text_day_count = count
                break
            else:
                count = count + 1
        all = lb_text_week.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                text_week_count = count
                break
            else:
                count = count + 1
        all = lb_text_month.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                text_month_count = count
                break
            else:
                count = count + 1
        all = lb_voice_day.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                voice_day_count = count
                break
            else:
                count = count + 1
        all = lb_voice_week.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                voice_week_count = count
                break
            else:
                count = count + 1
        all = lb_voice_month.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                voice_month_count = count
                break
            else:
                count = count + 1
        all = lb_both_day.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                both_day_count = count
                break
            else:
                count = count + 1
        all = lb_both_week.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                both_week_count = count
                break
            else:
                count = count + 1
        all = lb_both_month.find()
        x = all.sort('level', -1)
        count = 1
        for info in x:
            if int(info.get('user')) == ctx.author.id:
                both_month_count = count
                break
            else:
                count = count + 1
    try:
        embed.add_field(name='**__Voice & Text__**',
                        value=f" #{both_day_count} | Daily \n #{both_week_count} | Weekly \n #{both_month_count} | Monthly \n #{both_alltime_count} | All time",
                        inline=False)
    except:
        pass
    try:
        embed.add_field(name='**__Text__**',
                        value=f" #{text_day_count} | Daily \n #{text_week_count} | Weekly \n #{text_month_count} | Monthly \n #{text_alltime_count} | All time",
                        inline=False)
    except:
        pass
    try:
        embed.add_field(name='**__Voice__**',
                        value=f" #{voice_day_count} | Daily \n #{voice_week_count} | Weekly \n #{voice_month_count} | Monthly \n #{voice_alltime_count} | All time",
                        inline=False)
    except:
        pass
    await ctx.send(embed=embed)


@bot.command(aliases=['lb'])
async def leaderboard(ctx, type=None):
    async with ctx.channel.typing():
        pass
    if type == None:
        x = max_leaderboard.find()
        x = x.sort('level', -1)
        embed = discord.Embed(title='All Time Leaderboard', color=0x00fff6)
        counter = 1
        for info in x:
            if counter == 1:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':first_place: {x}', value=f'lvl {info.get("level")}', inline=False)
            if counter == 2:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':second_place: {x}', value=f'lvl {info.get("level")}', inline=False)
            if counter == 3:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':third_place: {x}', value=f'lvl {info.get("level")}', inline=False)
            if counter == 4:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f'4th {x}', value=f'lvl {info.get("level")}', inline=False)
            if counter == 5:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f'5th {x}', value=f'lvl {info.get("level")}', inline=False)
            counter = counter + 1
        embed.set_footer(text='1/3 | all-time')
        x = await ctx.send(embed=embed)
    elif type == 'txt' or type == 'text' or type == 'Text' or type == 'Txt':
        embed = discord.Embed(title='Top 5 Texters | Daily', color=0x00fff6)
        counter = 1
        x = lb_text_day.find()
        x = x.sort('exp', -1)
        for info in x:
            if counter == 1:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 2:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 3:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 4:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 5:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp', inline=False)
            counter = counter + 1
        embed.set_footer(text='1/3 | text')
        x = await ctx.send(embed=embed)
    elif type == 'voice' or type == 'Voice' or type == 'vc' or type == 'Vc':
        embed = discord.Embed(title='Top 5 Voice-chatters | Daily', color=0x00fff6)
        counter = 1
        x = lb_voice_day.find()
        x = x.sort('exp', -1)
        for info in x:
            if counter == 1:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 2:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 3:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 4:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
            if counter == 5:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
            counter = counter + 1
        embed.set_footer(text='1/3 | voice')
        x = await ctx.send(embed=embed)
    elif type == 'both' or type == 'all':
        embed = discord.Embed(title='Top 5 Text & Voice-chatters | Daily', color=0x00fff6)
        counter = 1
        x = lb_both_day.find()
        x = x.sort('exp', -1)
        for info in x:
            if counter == 1:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 2:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 3:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp', inline=False)
            if counter == 4:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
            if counter == 5:
                x = bot.get_user(info.get('user'))
                embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
            counter = counter + 1
        embed.set_footer(text='1/3 | both')
        x = await ctx.send(embed=embed)
    else:
        x = None
    if x == None:
        return
    else:
        emoji = bot.get_emoji(841397189171609640)
        await x.add_reaction(emoji)
        emoji = bot.get_emoji(841392863237636176)
        await x.add_reaction(emoji)
        emoji = bot.get_emoji(841399219486851143)
        await x.add_reaction(emoji)

    # cooldown.pop(f'{message.author.id}')
    # x = alltime_lb.find()
    # x = x.sort('level')
    # print(x)


@bot.event
async def on_raw_reaction_add(payload):
    cached = bot.cached_messages
    message = None
    for info in cached:
        if info.id == payload.message_id:
            message = info
            break
    if payload.user_id == 840393373138944031:
        return
    if message == None:
        return
    else:
        if message.author.id == 840393373138944031:
            if message.embeds:
                if payload.emoji.id == 841399219486851143:
                    emoji = bot.get_emoji(841399219486851143)
                    user = bot.get_user(payload.user_id)
                    await message.remove_reaction(emoji, user)
                    for info in message.embeds:
                        info = info.to_dict()
                        info = info.get('footer')
                        if info.get('text') == '1/3 | all-time':
                            x = experience.find()
                            x = x.sort('level', -1)
                            counter = 1
                            embed = discord.Embed(title='All Time Leaderboard | Text', color=0x00fff6)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'level {info.get("level")}', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'level {info.get("level")}', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='2/3 | all-time')
                            await message.edit(embed=embed)
                        elif info.get('text') == '2/3 | all-time':
                            x = voice_exp.find()
                            x = x.sort('level', -1)
                            counter = 1
                            embed = discord.Embed(title='All Time Leaderboard | Voice', color=0x00fff6)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'level {info.get("level")}', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'level {info.get("level")}', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='3/3 | all-time')
                            await message.edit(embed=embed)
                        elif info.get('text') == '1/3 | text':
                            embed = discord.Embed(title='Top 5 texters | Weekly', color=0x00fff6)
                            counter = 1
                            x = lb_text_week.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='2/3 | text')
                            await message.edit(embed=embed)
                        elif info.get('text') == '2/3 | text':
                            embed = discord.Embed(title='Top 5 texters | Monthly', color=0x00fff6)
                            counter = 1
                            x = lb_text_month.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='3/3 | text')
                            await message.edit(embed=embed)
                        elif info.get('text') == '1/3 | voice':
                            embed = discord.Embed(title='Top 5 voice-chatters | Weekly', color=0x00fff6)
                            counter = 1
                            x = lb_voice_week.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='2/3 | voice')
                            await message.edit(embed=embed)
                        elif info.get('text') == '2/3 | voice':
                            embed = discord.Embed(title='Top 5 voice-chatters | Monthly', color=0x00fff6)
                            counter = 1
                            x = lb_voice_month.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='3/3 | voice')
                            await message.edit(embed=embed)
                        elif info.get('text') == '1/3 | both':
                            embed = discord.Embed(title='Top 5 Text & Voice-chatters | Weekly', color=0x00fff6)
                            counter = 1
                            x = lb_both_week.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='2/3 | both')
                            await message.edit(embed=embed)
                        elif info.get('text') == '2/3 | both':
                            embed = discord.Embed(title='Top 5 Text & Voice-chatters | Monthly', color=0x00fff6)
                            counter = 1
                            x = lb_both_month.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='3/3 | both')
                            await message.edit(embed=embed)
                if payload.emoji.id == 841397189171609640:
                    emoji = bot.get_emoji(841397189171609640)
                    user = bot.get_user(payload.user_id)
                    await message.remove_reaction(emoji, user)
                    for info in message.embeds:
                        info = info.to_dict()
                        info = info.get('footer')
                        if info.get('text') == '3/3 | all-time':
                            x = experience.find()
                            x = x.sort('level', -1)
                            counter = 1
                            embed = discord.Embed(title='All Time Leaderboard | Text', color=0x00fff6)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'level {info.get("level")}',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'level {info.get("level")}', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'level {info.get("level")}', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='2/3 | all-time')
                            await message.edit(embed=embed)
                        elif info.get('text') == '2/3 | all-time':
                            x = max_leaderboard.find()
                            x = x.sort('level', -1)
                            embed = discord.Embed(title='All Time Leaderboard', color=0x00fff6)
                            counter = 1
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'lvl {info.get("level")}',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'lvl {info.get("level")}',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'lvl {info.get("level")}',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'lvl {info.get("level")}', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'lvl {info.get("level")}', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='1/3 | all-time')
                            await message.edit(embed=embed)
                        elif info.get('text') == '3/3 | text':
                            embed = discord.Embed(title='Top 5 texters | Weekly', color=0x00fff6)
                            counter = 1
                            x = lb_text_week.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='2/3 | text')
                            await message.edit(embed=embed)
                        elif info.get('text') == '2/3 | text':
                            embed = discord.Embed(title='Top 5 texters | daily', color=0x00fff6)
                            counter = 1
                            x = lb_text_day.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='1/3 | text')
                            await message.edit(embed=embed)
                        elif info.get('text') == '3/3 | voice':
                            embed = discord.Embed(title='Top 5 voice-chatters | Weekly', color=0x00fff6)
                            counter = 1
                            x = lb_voice_week.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='2/3 | voice')
                            await message.edit(embed=embed)
                        elif info.get('text') == '2/3 | voice':
                            embed = discord.Embed(title='Top 5 voice-chatters | daily', color=0x00fff6)
                            counter = 1
                            x = lb_voice_day.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='1/3 | voice')
                            await message.edit(embed=embed)
                        elif info.get('text') == '3/3 | both':
                            embed = discord.Embed(title='Top 5 Text & Voice-chatters | Weekly', color=0x00fff6)
                            counter = 1
                            x = lb_both_week.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='2/3 | both')
                            await message.edit(embed=embed)
                        elif info.get('text') == '2/3 | both':
                            embed = discord.Embed(title='Top 5 Text & Voice-chatters | Daily', color=0x00fff6)
                            counter = 1
                            x = lb_both_day.find()
                            x = x.sort('exp', -1)
                            for info in x:
                                if counter == 1:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':first_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 2:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':second_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 3:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f':third_place: {x}', value=f'{info.get("exp")} exp',
                                                    inline=False)
                                if counter == 4:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'4th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                if counter == 5:
                                    x = bot.get_user(info.get('user'))
                                    embed.add_field(name=f'5th {x}', value=f'{info.get("exp")} exp ', inline=False)
                                counter = counter + 1
                            embed.set_footer(text='1/3 | both')
                            await message.edit(embed=embed)
                if payload.emoji.id == 841392863237636176:
                    emoji = bot.get_emoji(841399219486851143)
                    await message.clear_reaction(emoji)
                    emoji = bot.get_emoji(841392863237636176)
                    await message.clear_reaction(emoji)
                    emoji = bot.get_emoji(841397189171609640)
                    await message.clear_reaction(emoji)
            else:
                return



@bot.command()
async def help(ctx):
    user = bot.get_user(840393373138944031)
    embed = discord.Embed(title='Help Section for Vibe House Gardener', color=0x00fff6)
    embed.add_field(name='**leaderboard**', value='`Alias: lb`\n Displays the level leaderboards! ', inline=False)
    embed.add_field(name='**level**',
                    value='`Alias: lvl, profile, exp, xp, profile` \n Shows your current text and vc level.',
                    inline=False)
    embed.add_field(name='**rank**', value='Shows your current rank on all leaderboards.', inline=False)
    embed.add_field(name='**ping**', value='Check my ping!')
    embed.add_field(name= "**Economy Commands!**",value='\u200b',inline=False)
    embed.add_field(name='**work**', value='Work hard and make a living.', inline=False)
    embed.add_field(name='**leaderboardmoney**', value='`Alias: lbm`\n Displays the currency leaderboards! ', inline=False)
    embed.add_field(name='**daily**', value='Get free money every 24hours! ', inline=False)
    embed.add_field(name='**give**', value=' Give someboty money! ', inline=False)
    embed.add_field(name='**quit**', value='Quit your current job! ', inline=False)
    embed.add_field(name='**shop**', value='Check out the shop!', inline=False)
    embed.add_field(name='**buy**', value='Buy something from the shop!', inline=False)
    embed.add_field(name='**sell**', value='Sell something from your Inventory', inline=False)
    embed.add_field(name='**inventory**', value='`Alias: inv`\n Check out your Inventory! ', inline=False)
    embed.add_field(name='**shoot**', value='Shoot someone!?!?! ', inline=False)
    embed.add_field(name='**gamblinginfo**', value='`Alias: gi`\n Check all the gambling games there are to offer! ', inline=False)
    embed.set_footer(text='starlord#0146 | All economy commands are beta, Please report any bugs to starlord#0146')
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)


@tasks.loop(minutes=1)
async def voice_exp_ppl():
    global vc_boosted_exp
    await bot.wait_until_ready()
    guild = await vibes.guild()
    for members in guild.members:
        x = members.voice
        if x == None:
            pass
        else:
            if x.self_mute:
                pass
            else:
                try:
                    blacklist_channel = blacklisted.find_one({'channel': x.channel.id})
                except:
                    pass
                if blacklist_channel != None:
                    pass
                else:
                    if members.bot:
                        pass
                    else:
                        exp = random.randint(10, 30) * vc_boosted_exp
                        insert_into_voice(members.id, exp)
                        info = {'user': members.id}
                        user = voice_exp.find_one(info)
                        if user == None:
                            info = {'user': members.id, 'level': 0, 'exp': exp}
                            voice_exp.insert_one(info)
                        else:
                            user_exp = user.get('exp')
                            user_lvl = user.get('level')
                            exp = user_exp + exp
                            levelmax = level_max(user_lvl)
                            levelmax = int(levelmax)
                            user_exp = int(user_exp)
                            if user_exp >= levelmax:
                                ctx = bot.get_channel(841836241313464351)
                                new_lvl = user_lvl + 1
                                #coins_lvl(user.id,new_lvl)
                                find = max_leaderboard.find_one({'user': members.id})
                                if find == None:
                                    max_leaderboard.insert_one({'user': members.id, 'level': 1})
                                    add, remove = roles_add(1)
                                    if add == None:
                                        pass
                                    else:
                                        guild = bot.get_guild(776822249314582538)
                                        og_role = guild.get_role(add)
                                        await members.add_roles(og_role)
                                        if remove == None:
                                            pass
                                        else:
                                            bruh = guild.get_role(remove)
                                            await members.remove_roles(bruh)

                                    text = lvl_up_txt(1)
                                else:
                                    x = find.get('level')
                                    x = int(x)
                                    x = x + 1
                                    max_leaderboard.update_one({'user': members.id}, {'$set': {'level': x}})
                                    text = lvl_up_txt(new_lvl)
                                    add, remove = roles_add(x)
                                    if add == None:
                                        pass
                                    else:
                                        guild = bot.get_guild(776822249314582538)
                                        og_role = guild.get_role(add)
                                        if remove == None:
                                            pass
                                        else:
                                            bruh = guild.get_role(remove)
                                            await members.remove_roles(bruh)
                                            await members.add_roles(og_role)
                                embed = discord.Embed(title=f"{members}", color=0x00fff6)
                                embed.add_field(name=f'Level {new_lvl}', value=f'{text}')
                                embed.set_thumbnail(url=members.avatar_url)
                                embed.timestamp = datetime.datetime.utcnow()
                                await ctx.send(members.mention, embed=embed)
                                voice_exp.update_one({"user": members.id}, {"$set": {"exp": 0, 'level': new_lvl}})
                            else:
                                voice_exp.update_one({"user": members.id}, {"$set": {"exp": exp}})


@tasks.loop(minutes=1)
async def leaderboard_reset():
    await bot.wait_until_ready()
    date = datetime.datetime.now()
    test = int(date.strftime("%Y"))
    test2 = int(date.strftime("%m"))
    test3 = int(date.strftime("%d"))
    day = calendar.weekday(test, test2, test3)
    time = (date.strftime("%H:%M"))
    if time == '23:00':
        channel = bot.get_channel(840627525994151958)
        if day == 5:
                weekly_delete()
                channel.send('Reseted Weekly Leaderboards')
        day_delete()
        await channel.send('Reseted Daily Leaderboards')

@bot.command()
async def reload(ctx,file):
    if ctx.author.id == 705992469426339841:
        for filename in os.listdir('cogging'):
            if filename.startswith(file):
                bot.reload_extension(f'cogging.{file}')
                await ctx.send(f"the cog {file} has been reloaded.")

@bot.command()
async def load(ctx,file):
    if ctx.author.id == 705992469426339841:
        for filename in os.listdir('cogging'):
            if filename.startswith(file):
                bot.load_extension(f'cogging.{file}')
                await ctx.send(f"the cog {file} has been loaded.")

@bot.command()
async def unload(ctx,file):
    if ctx.author.id == 705992469426339841:
        for filename in os.listdir('cogging'):
            if filename.startswith(file):
                bot.unload_extension(f'cogging.{file}')
                await ctx.send(f"the cog {file} has been unloaded.")


for filename in os.listdir('cogging'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogging.{filename[:-3]}')

leaderboard_reset.start()
voice_exp_ppl.start()
bot.run('noseetoken')
