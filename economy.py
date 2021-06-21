import discord
from discord.ext import commands, tasks
import pymongo
import random
import datetime
import asyncio
from discord.ext.commands import BucketType
from vibeclass import vibes

#starlorddev05
client = pymongo.MongoClient(
    "mongodb+srv://Starlord:Adeoluwa.05@cluster0.8jinl.mongodb.net/myFirstDatabase&retryWrites=true&w=majority?ssl=true&ssl_cert_reqs=CERT_NONE",
    connect=False)
dbs = client.Users
jobs= dbs.Jobs
dbev = client.Inv

# starlordDev69
client = pymongo.MongoClient(
    "mongodb+srv://Starlord:Adeoluwa.05@cluster0.q1yxp.mongodb.net/myFirstDatabase&retryWrites=true&w=majority?ssl=true&ssl_cert_reqs=CERT_NONE",
    connect=False)
db = client.leaderboard
max_leaderboard = db.lb

class Economy(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.coins = dbs.Coins
        self.Items = dbev.Items
        self.vibes = vibes(self.bot)
        self.money_adder.start()


    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        print('Cog is online')

    @commands.Cog.listener("on_member_leave")
    async def the_member_leave(self,member):
        jobs.delete_one({'user':member.id})
        self.Items.delete_one({'user':member.id})
        self.coins.delete_one({'user':member.id})


    @commands.command()
    @commands.cooldown(rate=1,per=86400,type= BucketType.user)
    async def daily(self,ctx):
        random_coins = random.randint(25,100)
        person = self.coins.find_one({"user": ctx.author.id})
        if person:
            og = person.get('coins')
            og = int(og)
            new_coins = og + random_coins
            self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
            await ctx.send(f'{ctx.author.mention} You have gained {random_coins} Vibins! <:vibegem:813864223137595402>')
        else:
            self.coins.insert_one({"user": ctx.author.id, "coins": random_coins})
            await ctx.send(f'{ctx.author.mention} You have gained {random_coins} Vibins! <:vibegem:813864223137595402>')
    @daily.error
    async def daily_error(self,ctx,error):
        if isinstance(error,commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'Error: You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)
    @commands.command()
    @commands.cooldown(rate=1, per=30, type=BucketType.user)
    async def give(self,ctx,person:discord.Member,amount:int):
        user = self.coins.find_one({'user':ctx.author.id})
        coin = user.get('coins')
        coin = int(coin)
        if amount > coin:
            await ctx.send("Error: Your giving more money than you have... Try a lower amount.")
        else:
            new_coins = coin - amount
            self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
            user_two = self.coins.find_one({'user': person.id})
            coin = user_two.get('coins')
            coin = int(coin)
            og_amount = amount
            tax = round(amount * 0.1)
            amount = amount - tax
            new_coins = coin + amount
            self.coins.update_one({'user': person.id}, {"$set": {"coins": new_coins}})
            await ctx.send(f"You have successfully given {person} {og_amount} Vibins with 10% tax | {amount} vibins")

    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'Error: You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)
    @commands.command(aliases=['bal'])
    async def balance(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        try:
            person = self.coins.find_one({"user": user.id})
        except:
            person = None
        if person:
            coins = person.get('coins')
            embed = discord.Embed(title=f'{user}\' Balance\'s', description=f'You have {coins} Vibins! <:vibegem:813864223137595402>', color=0x00fff6)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f'{user}\' Balance\'s', description=f'You have 0 Vibins! <:vibegem:813864223137595402>', color=0x00fff6)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=43200,type= BucketType.user)
    @commands.max_concurrency(1, per=BucketType.user, wait=False)
    async def work(self,ctx):
        check = jobs.find_one({'user':ctx.author.id})
        if check:
            job = check.get('job')
            if job == 'vibe collecter':
                person = self.coins.find_one({"user": ctx.author.id})
                if person:
                    og = person.get('coins')
                    og = int(og)
                    new_coins = og + 25
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                    await ctx.send(f'{ctx.author.mention} You have gained 25 Vibins! <:vibegem:813864223137595402>')
                else:
                    self.coins.insert_one({"user": ctx.author.id, "coins": 25})
                    await ctx.send(f'{ctx.author.mention} You have gained 25 Vibins! <:vibegem:813864223137595402>')
            elif job == 'viber':
                person = self.coins.find_one({"user": ctx.author.id})
                if person:
                    og = person.get('coins')
                    og = int(og)
                    new_coins = og + 50
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                    await ctx.send(f'{ctx.author.mention} You have gained 50 Vibins! <:vibegem:813864223137595402>')
                else:
                    self.coins.insert_one({"user": ctx.author.id, "coins": 50})
                    await ctx.send(f'{ctx.author.mention} You have gained 50 Vibins! <:vibegem:813864223137595402>')
            elif job == 'vibe cleaner':
                person = self.coins.find_one({"user": ctx.author.id})
                if person:
                    og = person.get('coins')
                    og = int(og)
                    new_coins = og + 100
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                    await ctx.send(f'{ctx.author.mention} You have gained 100 Vibins! <:vibegem:813864223137595402>')
                else:
                    self.coins.insert_one({"user": ctx.author.id, "coins": 100})
                    await ctx.send(f'{ctx.author.mention} You have gained 100 Vibins! <:vibegem:813864223137595402>')
        else:
            await ctx.send("At that moment You\'ve realized you dont have a job. Its time to get one.")
            embed = discord.Embed(title='Which Job would u like to work at.',color=0x00fff6)
            try:
                person = max_leaderboard.find_one({'user':ctx.author.id})
                level = person.get('level')
                level = int(level)
            except:
                level = 0
            amount = None
            if level >= 1:
                embed.add_field(name='Vibe Collecter | 25 vibins <:vibegem:813864223137595402>',value='\u200b',inline=False)
                amount = 1
            if level >= 5:
                embed.add_field(name='Viber | 50 vibins <:vibegem:813864223137595402>',value='\u200b',inline=False)
                amount = 2
            if level >= 10:
                embed.add_field(name='Vibe Cleaner | 100 vibins <:vibegem:813864223137595402>',value='\u200b',inline=False)
                amount = 3
            embed.set_footer(text='If the embed is empty, You have to gain lvl 1 to be able to have a job. | Type out what job you want. ex. "Viber"')
            await ctx.send(embed = embed)
            if amount == 1:
                job_question = ['Vibe Collecter','vibe collecter','Vibe collecter']
                def check(message):
                    return (message.content in job_question) and (message.channel == ctx.channel) and (message.author == ctx.author)
                try:
                    answer = await self.bot.wait_for('message', timeout=30, check=check)
                except asyncio.TimeoutError:
                    await ctx.send('You didnt respond... Cancelling.')
                else:
                    answer = answer.content.lower()
                    if answer == 'vibe collecter':
                        jobs.insert_one({'user':ctx.author.id,"job":'vibe collecter'})
                        await ctx.send('You\'ve Succesfully gotten the job. Congrats!')
                        await ctx.reinvoke()
            if amount == 2:
                job_question = ['Vibe Collecter', 'Viber','vibe collecter', 'viber',
                                'Vibe collecter']
                def check(message):
                    return (message.content in job_question) and (message.channel == ctx.channel) and (message.author == ctx.author)
                try:
                    answer = await self.bot.wait_for('message', timeout=30, check=check)
                except asyncio.TimeoutError:
                    await ctx.send('You didnt respond... Cancelling.')
                else:
                    answer = answer.content.lower()
                    if answer == 'vibe collecter':
                        jobs.insert_one({'user':ctx.author.id,"job":'vibe collecter'})
                        await ctx.send('You\'ve Succesfully gotten the job. Congrats!')
                        await ctx.reinvoke()
                    if answer == 'viber':
                        jobs.insert_one({'user': ctx.author.id, "job": 'viber'})
                        await ctx.send('You\'ve Succesfully gotten the job. Congrats!')
                        await ctx.reinvoke()
            if amount == 3:
                job_question = ['Vibe Collecter', 'Viber','vibe collecter', 'viber',
                                'Vibe collecter','Vibe Cleaner','vibe cleaner','Vibe cleaner']
                def check(message):
                    return (message.content in job_question) and (message.channel == ctx.channel) and (message.author == ctx.author)
                try:
                    answer = await self.bot.wait_for('message', timeout=30, check=check)
                except asyncio.TimeoutError:
                    await ctx.send('You didnt respond... Cancelling.')
                else:
                    answer = answer.content.lower()
                    if answer == 'vibe collecter':
                        jobs.insert_one({'user':ctx.author.id,"job":'vibe collecter'})
                        await ctx.send('You\'ve Succesfully gotten the job. Congrats!')
                        await ctx.reinvoke()
                    if answer == 'viber':
                        jobs.insert_one({'user': ctx.author.id, "job": 'viber'})
                        await ctx.send('You\'ve Succesfully gotten the job. Congrats!')
                        await ctx.reinvoke()
                    if answer == 'vibe cleaner':
                        jobs.insert_one({'user': ctx.author.id, "job": 'vibe cleaner'})
                        await ctx.send('You\'ve Succesfully gotten the job. Congrats!')
                        await ctx.reinvoke()
    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'Error: You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)
    @commands.command()
    @commands.cooldown(rate=1, per=172800,type= BucketType.user)
    async def quit(self,ctx):
        jobs.delete_one({'user':ctx.author.id})
        await ctx.send('You\'ve succesfully quit your job')
    @quit.error
    async def quit_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)
    @commands.command()
    async def lbm(self,ctx):
        embed = discord.Embed(title='Top 10 Richest people in the server.',color=0x00fff6)
        x = self.coins.find()
        x = x.sort('coins', -1)
        counter = 1
        for info in x:
            if counter == 1:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f':first_place: {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402> ',
                                inline=False)
            if counter == 2:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f':second_place: {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>',
                                inline=False)
            if counter == 3:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f':third_place: {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>',
                                inline=False)
            if counter == 4:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f'4th {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>', inline=False)
            if counter == 5:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f'5th {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>', inline=False)
            if counter == 6:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f'6th {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>', inline=False)
            if counter == 7:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f'7th {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>', inline=False)
            if counter == 8:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f'8th {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>', inline=False)
            if counter == 9:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f'9th {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>', inline=False)
            if counter == 10:
                x = self.bot.get_user(info.get('user'))
                embed.add_field(name=f'10th {x}', value=f'{info.get("coins")} vibins <:vibegem:813864223137595402>', inline=False)
                break
            counter = counter + 1
        await ctx.send(embed = embed)
    @commands.command()
    @commands.cooldown(rate=1, per=21600,type= BucketType.user)
    @commands.max_concurrency(1, per=BucketType.user, wait=False)
    async def shoot(self,ctx,user:discord.Member):
        our_user = self.Items.find_one({'user':ctx.author.id})
        check1 = our_user.get('gun')
        check2 = our_user.get('bullet')
        if check2 == 0:
            check2 = None
        if not check1:
            await ctx.send('Error: you dont have the required items to perform this task.')
        else:
            if not check2:
                await ctx.send('Error: you dont have the required items to perform this task.')
            else:
                await ctx.send(f'Its a dark night and you walk up on {user} Pull out your gun and...SHOOT')
                try:
                    their_user = self.Items.find_one({'user':user.id})
                    check3 = their_user.get('bulletproofvest')
                except:
                    check3 = None
                if check3:
                    check4 = their_user.get('b_uses')
                    check4 = int(check4)
                    check4 = check4 + 1
                    if check4 >= 10:
                        check3 = check3 - 1
                        if check3 == 0:
                            self.Items.update_one({'user': user.id}, {"$unset": {'b_uses':'','bulletproofvest':''}})
                        else:
                            self.Items.update_one({'user': user.id}, {"$set": {'bulletproofvest': check3,'b_uses': 0}})
                    else:
                        self.Items.update_one({'user':user.id},{'$set':{'b_uses':check4}})
                    await ctx.send(f"But wait {user} is wearing a Bulletproof vest. You try to shoot {user} again but then u realized u only brought 1 bullet.")
                    await ctx.send(f'So you run away cursing {user} under your breath.')
                    bullet = our_user.get('bullet')
                    bullet = int(bullet)
                    bullet = bullet - 1
                    gun = our_user.get('g_uses')
                    gun = int(gun)
                    gun = gun + 1
                    if gun >= 10:
                        await ctx.send('As you run away you begin to feel you gun break in your hands...')
                        await asyncio.sleep(3)
                        await ctx.send('Your gun broke. You might have to go buy a new one')
                        real_gun = our_user.get('gun')
                        real_gun = int(real_gun)
                        real_gun = real_gun - 1
                        if real_gun == 0:
                            self.Items.update_one({'user': ctx.author.id}, {"$unset": {'g_uses':'','gun':''}})
                        else:
                            self.Items.update_one({'user': ctx.author.id}, {"$set": {'gun': real_gun,'g_uses': 0, 'bullet': bullet}})
                    else:
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'g_uses':gun,'bullet':bullet}})
                else:
                    await ctx.send(f'You go over to {user} and they are lying on the ground. DEAD')
                    user_coins = self.coins.find_one({'user':user.id})
                    user_coins = user_coins.get('coins')
                    user_coins = int(user_coins)
                    self.coins.update_one({'user': user.id}, {"$set": {'coins': 0}})
                    await ctx.send(f'Brimming with joy you happily take all of {user} money which is about {user_coins} Vibins')
                    author = self.coins.find_one({'user':ctx.author.id})
                    author_coins = author.get('coins')
                    author_coins = int(author_coins)
                    author_coins = author_coins + user_coins
                    await ctx.send(f'Mission Successfull you now have {author_coins} Vibins')
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': author_coins}})
                    bullet = our_user.get('bullet')
                    bullet = int(bullet)
                    bullet = bullet - 1
                    gun = our_user.get('g_uses')
                    gun = int(gun)
                    gun = gun + 1
                    if gun >= 10:
                        await ctx.send('As you run away you begin to feel you gun break in your hands...')
                        await asyncio.sleep(3)
                        await ctx.send('Your gun broke. You might have to go buy a new one')
                        real_gun = our_user.get('gun')
                        real_gun = int(real_gun)
                        real_gun = real_gun - 1
                        if real_gun == 0:
                            self.Items.update_one({'user': ctx.author.id}, {"$unset": {'g_uses': '', 'gun': ''}})
                        else:
                            self.Items.update_one({'user': ctx.author.id},
                                                  {"$set": {'gun': real_gun, 'g_uses': 0, 'bullet': bullet}})
                    else:
                        self.Items.update_one({'user': ctx.author.id}, {"$set": {'g_uses': gun, 'bullet': bullet}})

    @shoot.error
    async def shoot_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'Error: You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)
    @commands.command()
    async def shop(self,ctx):
        embed = discord.Embed(title='Item Shop',color=0x00fff6)
        embed.add_field(name=':gun: Gun ',value='5000 <:vibegem:813864223137595402> \n ━◥◣◆◢◤━ \nShoot someone, and claim all their money if you succeed! You will also need to buy bullets. To use, type v!shoot @user',inline=False)
        embed.add_field(name=':black_small_square: Bullets',value='500 <:vibegem:813864223137595402> \n ━◥◣◆◢◤━\n Ammo for your gun, once used, you will need to buy more.',inline=False)
        embed.add_field(name=':safety_vest: Bulletproof Vest',value='2500 <:vibegem:813864223137595402> \n ━◥◣◆◢◤━ \n Protects you from 10 bullets before breaking. ', inline=False)
        #embed.add_field(name=':notes: Vibebox', value='10000 <:vibegem:813864223137595402> \n ━◥◣◆◢◤━\n Adds a 0.25% multiplier when gambling. Max Multiplier Stack: 200%', inline=False)
        embed.set_footer(text='To buy any of these items just use the v!buy command... ex: v!buy gun')
        user = self.bot.get_user(840393373138944031)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed = embed)


    @commands.command()
    async def buy(self,ctx,*,item):
        item = item.lower()
        if item == 'gun':
            user = self.coins.find_one({'user':ctx.author.id})
            coin = user.get('coins')
            coin = int(coin)
            if coin < 5000:
                await ctx.send('You dont have enough money to buy this... come back later.')
            else:
                new_coin = coin - 5000
                self.coins.update_one({'user':ctx.author.id},{"$set":{'coins':new_coin}})
                check = self.Items.find_one({'user':ctx.author.id})
                if not check:
                    self.Items.insert_one({'user':ctx.author.id,'gun':1,'g_uses':0})
                    await ctx.send('You have successfully bought a Gun.')
                else:
                    if not check.get('gun'):
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'gun':1,'g_uses':0}})
                        await ctx.send('You have successfully bought a Gun.')
                    else:
                        num = check.get('gun')
                        num = int(num)
                        num = num + 1
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'gun':num}})
                        await ctx.send('You have successfully bought a Gun.')
        elif item == 'bullet' or item == 'bullets':
            user = self.coins.find_one({'user':ctx.author.id})
            coin = user.get('coins')
            coin = int(coin)
            if coin < 500:
                await ctx.send('You dont have enough money to buy this... come back later.')
            else:
                new_coin = coin - 500
                self.coins.update_one({'user':ctx.author.id},{"$set":{'coins':new_coin}})
                check = self.Items.find_one({'user':ctx.author.id})
                if not check:
                    self.Items.insert_one({'user':ctx.author.id,'bullet':1})
                    await ctx.send('You have successfully bought a Bullet.')
                else:
                    if not check.get('bullet'):
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'bullet':1}})
                        await ctx.send('You have successfully bought a Bullet.')
                    else:
                        num = check.get('bullet')
                        num = int(num)
                        num = num + 1
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'bullet':num}})
                        await ctx.send('You have successfully bought a Bullet.')

        elif item == 'bulletproof vest' or item == 'bpv':
            user = self.coins.find_one({'user':ctx.author.id})
            coin = user.get('coins')
            coin = int(coin)
            if coin < 2500:
                await ctx.send('You dont have enough money to buy this... come back later.')
            else:
                new_coin = coin - 2500
                self.coins.update_one({'user':ctx.author.id},{"$set":{'coins':new_coin}})
                check = self.Items.find_one({'user':ctx.author.id})
                if not check:
                    self.Items.insert_one({'user':ctx.author.id,'bulletproofvest':1,'b_uses':0})
                    await ctx.send('You have successfully bought a Bulletproof Vest.')
                else:
                    if not check.get('bulletproofvest'):
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'bulletproofvest':1,'b_uses':0}})
                        await ctx.send('You have successfully bought a Bulletproof Vest.')
                    else:
                        num = check.get('bulletproofvest')
                        num = int(num)
                        num = num + 1
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'bulletproofvest':num}})
                        await ctx.send('You have successfully bought a Bulletproof Vest.')

        elif item == 'vibebox':
            user = self.coins.find_one({'user':ctx.author.id})
            coin = user.get('coins')
            coin = int(coin)
            if coin < 10000:
                await ctx.send('You dont have enough money to buy this... come back later.')
            else:
                new_coin = coin - 10000
                self.coins.update_one({'user':ctx.author.id},{"$set":{'coins':new_coin}})
                check = self.Items.find_one({'user':ctx.author.id})
                if not check:
                    self.Items.insert_one({'user':ctx.author.id,'vibebox':1})
                    await ctx.send('You have successfully bought a Vibebox.')
                else:
                    if not check.get('vibebox'):
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'vibebox':1}})
                        await ctx.send('You have successfully bought a Vibebox.')
                    else:
                        num = check.get('vibebox')
                        num = int(num)
                        num = num + 1
                        self.Items.update_one({'user':ctx.author.id},{"$set":{'vibebox':num}})
                        await ctx.send('You have successfully bought a Vibebox.')
        else:
            await ctx.send('Error: That is not a valid item.')
    @commands.command()
    async def sell(self,ctx,*,item):
        item = item.lower()
        if item == 'gun':
            user = self.Items.find_one({'user': ctx.author.id})
            coin = user.get('gun')
            try:
                coin = int(coin)
            except:
                pass
            users = self.coins.find_one({'user': ctx.author.id})
            item = users.get('coins')
            item = int(item)
            if not coin:
                await ctx.send('You dont have this item to sell.')
            else:
                new_coin = item + 2500
                check = self.Items.find_one({'user': ctx.author.id})
                num = check.get('gun')
                num = int(num)
                if num == 0:
                    await ctx.send('You dont have this item to sell for 2500 vibins.')
                num = num - 1
                if num == 0:
                    self.Items.update_one({'user': ctx.author.id}, {"$unset": {'gun':'','g_uses':''}})
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': new_coin}})
                    await ctx.send('You have successfully sold a Gun.')
                else:
                    self.Items.update_one({'user': ctx.author.id}, {"$set": {'gun': num}})
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': new_coin}})
                    await ctx.send('You have successfully sold a Gun for 2500 vibins.')
        elif item == 'bullet' or item == 'bullets':
            user = self.Items.find_one({'user': ctx.author.id})
            coin = user.get('bullet')
            coin = int(coin)
            try:
                coin = int(coin)
            except:
                pass
            users = self.coins.find_one({'user': ctx.author.id})
            item = users.get('coins')
            item = int(item)
            if not coin:
                await ctx.send('You dont have this item to sell.')
            else:
                new_coin = item + 250
                check = self.Items.find_one({'user': ctx.author.id})
                num = check.get('bullet')
                num = int(num)
                if num == 0:
                    await ctx.send('You dont have this item to sell.')
                num = num - 1
                if num == 0:
                    self.Items.update_one({'user': ctx.author.id}, {"$unset": {'bullet': ''}})
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': new_coin}})
                    await ctx.send('You have successfully sold a Bullet for 500 vibins.')
                else:
                    self.Items.update_one({'user': ctx.author.id}, {"$set": {'bullet': num}})
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': new_coin}})
                    await ctx.send('You have successfully sold a Bullet for 500 vibins.')
        elif item == 'bulletproof vest' or item == 'bpv':
            user = self.Items.find_one({'user': ctx.author.id})
            coin = user.get('bulletproofvest')
            coin = int(coin)
            try:
                coin = int(coin)
            except:
                pass
            users = self.coins.find_one({'user': ctx.author.id})
            item = users.get('coins')
            item = int(item)
            if not coin:
                await ctx.send('You dont have this item to sell.')
            else:
                new_coin = item + 1250
                check = self.Items.find_one({'user': ctx.author.id})
                num = check.get('bulletproofvest')
                num = int(num)
                if num == 0:
                    await ctx.send('You dont have this item to sell.')
                num = num - 1
                if num == 0:
                    self.Items.update_one({'user': ctx.author.id}, {"$unset": {'bulletproofvest': '', 'b_uses': ''}})
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': new_coin}})
                    await ctx.send('You have successfully sold a Bulletproof Vest for 1250 vibins.')
                else:
                    self.Items.update_one({'user': ctx.author.id}, {"$set": {'bulletproofvest': num}})
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': new_coin}})
                    await ctx.send('You have successfully sold a Bulletproof Vest for 1250 vibins.')
        elif item == 'vibebox':
            user = self.Items.find_one({'user': ctx.author.id})
            coin = user.get('vibebox')
            coin = int(coin)
            try:
                coin = int(coin)
            except:
                pass
            users = self.coins.find_one({'user': ctx.author.id})
            item = users.get('coins')
            item = int(item)
            if not coin:
                await ctx.send('You dont have this item to sell.')
            else:
                new_coin = item + 5000
                check = self.Items.find_one({'user': ctx.author.id})
                num = check.get('vibebox')
                num = int(num)
                if num == 0:
                    await ctx.send('You dont have this item to sell.')
                num = num - 1
                if num == 0:
                    self.Items.update_one({'user': ctx.author.id}, {"$unset": {'vibebox': ''}})
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': new_coin}})
                    await ctx.send('You have successfully sold a Vibebox for 5000 vibins')
                else:
                    self.Items.update_one({'user': ctx.author.id}, {"$set": {'vibebox': num}})
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {'coins': new_coin}})
                    await ctx.send('You have successfully sold a Vibebox for 5000 vibins')
        else:
            await ctx.send('Error: That is not a valid item.')

    @commands.command(aliases=['inv'])
    @commands.cooldown(rate=1, per=15, type=BucketType.user)
    async def inventory(self,ctx):
        embed = discord.Embed(title=f'{ctx.author}\'s inventory', color=0x00fff6)
        try:
            user = self.Items.find_one({'user':ctx.author.id})
        except:
            user = None
        if not user:
            pass
        else:
            if user.get('gun'):
                num = user.get('gun')
                embed.add_field(name=f':gun: Gun | {num}',value='\u200b',inline=False)
            if user.get('bullet'):
                num = user.get('bullet')
                embed.add_field(name=f':black_small_square: Bullet(s) | {num}',value='\u200b',inline=False)
            if user.get('bulletproofvest'):
                num = user.get('bulletproofvest')
                embed.add_field(name=f':safety_vest: Bulletproof Vest | {num}',value=f'\u200b',inline=False)
            if user.get('vibebox'):
                num = user.get('vibebox')
                embed.add_field(name=f':notes: Vibebox | {num}',value=f'\u200b',inline=False)
        await ctx.send(embed = embed)

    @inventory.error
    async def inventory_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'Error: You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)


    @commands.command(aliases=['gi'])
    async def gamblinginfo(self,ctx):
        embed = discord.Embed(title='Gambling games info.',color=0x00fff6)
        embed.add_field(name='dice',value='You have three rolls of the dice to match a number you select. \n ---------------------------------------------------------------\nYou will win 3 times your wager if you guess on the 1st roll. You will win 2 times your wager if you guess on the 2nd roll.If you guess it on the 3rd role... Well then you dont lose your money.',inline=False)
        embed.add_field(name='high/low',value='Yes, this is your average game of High/Low The number will be random 1-100. You will have ten tried to try and guess the answer. If you guess correct thne you win .25% of your wager Good luck! | v!highlow',inline=False)
        embed.add_field(name='slots',value='Your average slots games get all 3 slots times your vibins by 5. If you get 2 matching you double. | v!slots',inline=False)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(rate=1, per=15, type=BucketType.user)
    @commands.max_concurrency(1, per=BucketType.user, wait=False)
    async def dice(self,ctx,amount:int):
        user = self.coins.find_one({'user':ctx.author.id})
        coin = user.get('coins')
        coin = int(coin)
        if amount > coin:
            await ctx.send("Error: Your betting more money than you have... Try a lower amount.")
        else:
            new_coins = coin - amount
            self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
            embed = discord.Embed(title=f'Ok,{ctx.author} you are at a point of no return.',description=f'What is your first choice for dice? your answer has to be 2-12',color=0x00fff6)
            await ctx.send(embed = embed)
            loop_num = 1
            gottem = False
            while loop_num != 4:
                dice_role = ['2','3','4','5','6','7','8','9','10','11','12']
                def check(message):
                    return (message.content in dice_role) and (message.channel == ctx.channel) and (message.author == ctx.author)
                try:
                    answer = await self.bot.wait_for('message', timeout=30, check=check)
                except asyncio.TimeoutError:
                    await ctx.send('You didnt respond in time. Cancelling and taxing. Your losing half of the coins you were gonna bet.')
                    coin = coin/2
                    user = self.coins.find_one({'user':ctx.author.id})
                    og_amount = user.get('coins')
                    new_coins = og_amount + coin
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                else:
                    dice_answer = random.randint(2,12)
                    user_answer = int(answer.content)
                    if dice_answer == user_answer:
                        if loop_num == 1:
                            amount = amount * 3
                            user = self.coins.find_one({'user': ctx.author.id})
                            og_amount = user.get('coins')
                            new_coins = og_amount + amount
                            self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                            embed = discord.Embed(title='Congrats you got the right answer, And on your first try.',description=f'You have gained {amount} vibins!',color=0x00fff6)
                            await ctx.send(embed=embed)
                            gottem = True
                            break
                        if loop_num == 2:
                            amount = round(amount * 2)
                            user = self.coins.find_one({'user': ctx.author.id})
                            og_amount = user.get('coins')
                            new_coins = og_amount + amount
                            self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                            embed = discord.Embed(title='Congrats you got the right answer, And on your second try.',
                                                  description=f'You have gained {amount} vibins!',color=0x00fff6)
                            await ctx.send(embed=embed)
                            gottem = True
                            break
                        if loop_num == 3:
                            amount = amount
                            user = self.coins.find_one({'user': ctx.author.id})
                            og_amount = user.get('coins')
                            new_coins = og_amount + amount
                            self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                            embed = discord.Embed(title='Congrats you got the right answer, And on your third try.',
                                                  description=f'You have gained {amount} vibins!',color=0x00fff6)
                            await ctx.send(embed=embed)
                            gottem = True
                            break
                    else:
                        embed = discord.Embed(title='Oops, thats the wrong Number',description=f'You guessed {user_answer} when the answer was {dice_answer}',color=0x00fff6)
                        embed.set_footer(text='Try again!')
                        await ctx.send(embed = embed)
                        loop_num = loop_num + 1
            if gottem == False:
                embed = discord.Embed(title='Uh Oh. Looks like you failed all 3 tries. Im sorry but you lose all your money.',description='Better luck next time!',color=0x00fff6)
                await ctx.send(embed = embed)

    @dice.error
    async def dice_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'Error: You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)

    @commands.command(aliases = ['hilow'])
    @commands.cooldown(rate=1, per=15, type=BucketType.user)
    @commands.max_concurrency(1, per=BucketType.user, wait=False)
    async def highlow(self,ctx,amount:int):
        user = self.coins.find_one({'user':ctx.author.id})
        coin = user.get('coins')
        if coin < amount:
            await ctx.send('Error: You dont have that amount of money in your bank.')
        else:
            new_coins = coin - amount
            self.coins.update_one({'user':ctx.author.id},{'$set':{'coins':new_coins}})
            random_num = random.randint(1,100)
            embed = discord.Embed(description='You number has been choosen please choose a number between the range of 1-100',color=0x00fff6)
            await ctx.send(embed = embed)
            turns = 0
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
                 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel and message.content in str(x)
            gottem = False
            while turns != 10:
                turns = turns + 1
                try:
                    answer = await self.bot.wait_for('message',check=check,timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send('You didnt respond in time. Cancelling and taxing. Your losing half of the coins you were gonna bet.')
                    amount = round(amount / 2)
                    user = self.coins.find_one({'user': ctx.author.id})
                    og_amount = user.get('coins')
                    new_coins = og_amount + amount
                    self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                    gottem = True
                    break
                else:
                    answer_num = int(answer.content)
                    if answer_num > random_num:
                        await ctx.send("Oop You got it wrong. The answer is too high. Try again.")
                    elif answer_num < random_num:
                        await ctx.send("Oop You got it wrong. The answer is too low. Try again.")
                    elif answer_num == random_num:
                        await ctx.send('You got it correct. Congrats.')
                        gottem = True
                        if turns <= 5:
                            added = round(amount * .25)
                            await ctx.send(f"You have gained {added} Vibins")
                            new_coins = coin + amount
                            self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                            break
                        elif turns > 5:
                            added = round(amount * .25)
                            await ctx.send(f"You have gained {added} Vibins")
                            new_coins = coin + amount
                            self.coins.update_one({'user': ctx.author.id}, {"$set": {"coins": new_coins}})
                            break
            if gottem == False:
                await ctx.send("Welp you lost your money... Better luck next time.")
    @highlow.error
    async def highlow_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'Error: You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)


    @commands.command(aliases=['slot'])
    @commands.cooldown(rate=1, per=15, type=BucketType.user)
    @commands.max_concurrency(1, per=BucketType.user, wait=False)
    async def slots(self,ctx,money:int):
        user = self.coins.find_one({'user': ctx.author.id})
        coin = user.get('coins')
        if coin < money:
            await ctx.send('Error: You dont have that amount of money in your bank.')
        else:
            new_coins = coin - money
            self.coins.update_one({'user': ctx.author.id}, {'$set': {'coins': new_coins}})
            roulette1 = random.randint(1,9)
            roulette2 = random.randint(1,9)
            roulette3 = random.randint(1,9)
            def uni(num:str):
                num = num.replace('1',':one:')
                num = num.replace("2", ':two:')
                num = num.replace("3", ':three:')
                num = num.replace("4", ':four:')
                num = num.replace("5", ':five:')
                num = num.replace("6", ':six:')
                num = num.replace("7", ':seven:')
                num = num.replace("8", ':eight:')
                num = num.replace("9", ':nine:')
                return num
            x = await ctx.send('**`___SLOTS___`**\n <a:slotsgif:856395585720156191> <a:slotsgif:856395585720156191> <a:slotsgif:856395585720156191>\n`|            |`\n`|            |`')
            await asyncio.sleep(1.5)
            unicode = uni(str(roulette1))
            await x.edit(content = f'**`___SLOTS___`**\n {unicode} <a:slotsgif:856395585720156191> <a:slotsgif:856395585720156191>\n`|            |`\n`|            |`')
            await asyncio.sleep(1.5)
            unicode2 = uni(str(roulette2))
            await x.edit(
                content=f'**`___SLOTS___`**\n {unicode} {unicode2} <a:slotsgif:856395585720156191>\n`|            |`\n`|            |`')
            await asyncio.sleep(1.5)
            unicode3 = uni(str(roulette3))
            await x.edit(
                content=f'**`___SLOTS___`**\n {unicode} {unicode2} {unicode3}\n`|            |`\n`|            |`')
            if roulette1 == roulette2:
                if roulette1 == roulette3:
                    money = round(money * 5)
                    moneh = money
                    money = coin + money
                    self.coins.update_one({'user': ctx.author.id}, {'$set': {'coins': money}})
                    await ctx.send(f'You have gained {moneh} Vibins! | x3')
                else:
                    money = round(money * 1.5)
                    moneh = money
                    money = coin + money
                    self.coins.update_one({'user': ctx.author.id}, {'$set': {'coins': money}})
                    await ctx.send(f'You have gained {moneh} Vibins!  | x1.5')
            elif roulette1 == roulette3:
                money = round(money * 1.5)
                moneh = money
                money = coin + money
                self.coins.update_one({'user': ctx.author.id}, {'$set': {'coins': money}})
                await ctx.send(f'You have gained {moneh} Vibins! | x1.5')
            elif roulette2 == roulette3:
                money = round(money * 1.5)
                moneh = money
                money = coin + money
                self.coins.update_one({'user': ctx.author.id}, {'$set': {'coins': money}})
                await ctx.send(f'You have gained {moneh} Vibins! | x1.5')
            else:
                await ctx.send("You have gained 0 Vibins!")

    @slots.error
    async def slots_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry = round(error.retry_after)
            time = str(datetime.timedelta(seconds=retry))
            await ctx.send(f'Error: You are on a cooldown, Please try again in {time}')
        else:
            await ctx.send(error)
    #@commands.command()
    #async def purge(self,ctx,amount:int):
        #await ctx.channel.purge(limit=amount + 1)

    @tasks.loop(minutes=1)
    async def money_adder(self):
        date = datetime.datetime.now()
        time = (date.strftime("%H:%M"))
        if time == '23:00':
            guild = await self.vibes.guild()
            for member in guild.members:
                for roles in member.roles:
                    user = self.coins.find_one({'user': member.id})
                    if user == None:
                        self.coins.insert_one({'user':member.id,'coins':0})
                        user = self.coins.find_one({'user': member.id})
                    coin = user.get('coins')
                    if roles.id == 834245311105990727: #dev
                        money = coin + 150
                        self.coins.update_one({'user': member.id}, {'$set': {'coins': money}})
                    user = self.coins.find_one({'user': member.id})
                    coin = user.get('coins')
                    if roles.id == 795699534734426114: #booster
                        money = coin + 150
                        self.coins.update_one({'user': member.id}, {'$set': {'coins': money}})
                    user = self.coins.find_one({'user': member.id})
                    coin = user.get('coins')
                    if roles.id == 811007572270252033:  # staff
                        money = coin + 150
                        self.coins.update_one({'user': member.id}, {'$set': {'coins': money}})
                    user = self.coins.find_one({'user': member.id})
                    coin = user.get('coins')
                    if roles.id == 803706029447053372:  # appreciate
                        money = coin + 150
                        self.coins.update_one({'user': member.id}, {'$set': {'coins': money}})
                    user = self.coins.find_one({'user': member.id})
                    coin = user.get('coins')
                    if roles.id == 801878608192077865:  # lots of friend
                        money = coin + 175
                        self.coins.update_one({'user': member.id}, {'$set': {'coins': money}})
                    user = self.coins.find_one({'user': member.id})
                    coin = user.get('coins')
                    if roles.id == 803706025793814550:  # servertilizator
                        money = coin + 200
                        self.coins.update_one({'user': member.id}, {'$set': {'coins': money}})
            channel = self.bot.get_channel(840627525994151958)
            await channel.send('Everybody has gotten their money!!')




def setup(bot):
    bot.add_cog(Economy(bot))