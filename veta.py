# coding=<utf-8>
import discord
import random
import datetime
import sqlite3
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix = '!', help_command = None)  # 명령어 접두어 설정
token = ("")  # Discord RG Stock bot 토큰값(※노출금지)

def gmser_check(id) :  # GM 서비스에 가입되어있는지 확인하는 함수
    alr_exist = []
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT id FROM UserInfo WHERE UserInfo.id")
    rows = cur.fetchall()
    for i in range(len(rows)) :
        ex = rows[i]
        alr_exist.append(ex[0])
    if id not in alr_exist :
        return 0
    elif id in alr_exist :
        return 1
    con.close()

def bring_acc(id) :  # 계좌 정보를 가져오는 함수
    alr_exist = []
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT * FROM UserInfo WHERE id = ?", (id,))
    rows = cur.fetchall()
    alr_exist = list(rows[0])
    con.close()
    bank = alr_exist[1]
    acc_num = alr_exist[2]
    money = alr_exist[3]
    return bank, acc_num, money

def acc_check(id) :  # 계좌가 개설되었는지 확인하는 함수
    total = bring_acc(id)
    bank = total[0]
    acc_num = total[1]
    money = total[2]
    if bank == 'NULL' and acc_num == 'NULL' and money == 'NULL' :
        return 0
    elif bank != 'NULL' and acc_num != 'NULL' and money != 'NULL' :
        return 1

def now_stock_price() :
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT * FROM Stock_Price")
    rows = cur.fetchall()
    now_price = list(rows[0])
    con.close()
    return now_price

def stock_updown_pic() :
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT * FROM updown_pic")
    rows = cur.fetchall()
    ex = list(rows[0])
    con.close()
    return ex

def stock_updown_giho() :
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT * FROM updown")
    rows = cur.fetchall()
    ex = list(rows[0])
    con.close()
    return ex

def updown_price() :
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT * FROM updown_price")
    rows = cur.fetchall()
    ex = list(rows[0])
    con.close()
    return ex

@bot.event  # Bot 온라인 접속 이벤트
async def on_ready() :
    print(f'부팅 성공: {bot.user.name}!')
    game = discord.Game("Beta Ver")  # ~~하는중에 표시
    await bot.change_presence(status = discord.Status.online, activity = game)

@bot.command()
async def ping(ctx) :
    embed = discord.Embed(title = ":ping_pong:Pong!", description = "Latency : `{}`ms".format(round(bot.latency * 1000)), color = 0xa9dbea)
    embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command()
async def help(ctx) :
    embed = discord.Embed(title = "도움말", description = "**!가입**\nRG Stock 게임 서비스에 가입할 수 있습니다.\n\n**!탈퇴**\nRG Stock 게임 서비스에서 탈퇴할 수 있습니다.\n\n**!계좌개설**\n계좌를 개설하여 주식, 금융거래가 가능합니다.\n\n**!계좌**\n계좌의 정보, 잔액을 확인할 수 있습니다.\n\n**!지원금**\n랜덤으로 1만원~5만원 사이의 돈을 받습니다.\n`잔고가 0원일 때 사용 가능`\n\n**!일**\n일을 하여 돈을 벌 수 있습니다.\n`쿨타임 : 5초`\n\n**!도박**\n도박을 할 수 있습니다.\n`!도박 <금액> or !도박 올인`\n\n**!송금**\n상대방에게 계좌이체를 할 수 있습니다.\n`!송금 <은행명> <계좌번호> <금액>`\n`수수료 : 10%`", color = 0xffc0cb)
    embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
    msg = await ctx.send(embed = embed)
    await msg.add_reaction("⬅")
    await msg.add_reaction("➡")

@bot.command()
async def 도움(ctx) :
    embed = discord.Embed(title = "도움말", description = "**!가입**\nRG Stock 게임 서비스에 가입할 수 있습니다.\n\n**!탈퇴**\nRG Stock 게임 서비스에서 탈퇴할 수 있습니다.\n\n**!계좌개설**\n계좌를 개설하여 주식, 금융거래가 가능합니다.\n\n**!계좌**\n계좌의 정보, 잔액을 확인할 수 있습니다.\n\n**!지원금**\n랜덤으로 1만원~5만원 사이의 돈을 받습니다.\n`잔고가 0원일 때 사용 가능`\n\n**!일**\n일을 하여 돈을 벌 수 있습니다.\n`쿨타임 : 5초`\n\n**!도박**\n도박을 할 수 있습니다.\n`!도박 <금액> or !도박 올인`\n\n**!송금**\n상대방에게 계좌이체를 할 수 있습니다.\n`!송금 <은행명> <계좌번호> <금액>`\n`수수료 : 10%`", color = 0xffc0cb)
    embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
    msg = await ctx.send(embed = embed)
    await msg.add_reaction("⬅")
    await msg.add_reaction("➡")

@bot.command()
async def 가입(ctx) :
    id = ctx.author.id
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    check = gmser_check(id)
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    if check == 0 :
        null = 'NULL'
        cur.execute("INSERT INTO UserInfo VALUES(?, ?, ?, ?, ?)", (id, null, null, null, nowDatetime,))
        embed = discord.Embed(title = ':wave: 가입', description = '성공적으로 RG Stock 게임 서비스에 가입되셨습니다.', color = 0xffc0cb)
        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif check == 1 :
        embed = discord.Embed(title = ':wave: 가입', description = '이미 RG Stock 게임 서비스에 가입되어 있습니다.', color = 0xff0000)
        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    con.close()

@bot.command()
async def 탈퇴(ctx) :
    id = ctx.author.id
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    check = gmser_check(id)
    if check == 0 :
        embed = discord.Embed(title = ':wave: 탈퇴', description = 'RG Stock 게임 서비스에 가입되어 있지 않습니다.', color = 0xff0000)
        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif check == 1 :
        cur.execute("DELETE FROM UserInfo WHERE id = ?", (id,))
        embed = discord.Embed(title = ':wave: 탈퇴', description = '성공적으로 RG Stock 게임 서비스에서 탈퇴되었습니다.\n`서비스를 다시 이용하시려면 !가입 명령어를 이용해 주세요.`', color = 0xffc0cb)
        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    con.close()

@bot.command()
async def 계좌(ctx) :
    id = ctx.author.id
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    bank_list = ['너희은행', '민족은행', '은행나무', '참좋은행', '카카뱅크', '그린은행']
    msg_req = ctx.message.content[4:6]
    msg_bank = ctx.message.content[7:11]
    if msg_req == '개설' :
        check = gmser_check(id)
        if check == 0 :
            embed = discord.Embed(title = ':gift: 지원금', description = 'RG Stock 게임 서비스에 가입되어 있지 않습니다.', color = 0xff0000)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        elif check == 1 :
            check = acc_check(id)
            if check == 1 :
                embed = discord.Embed(title = ':closed_lock_with_key: 계좌개설', description = '계좌가 이미 개설되었습니다.', color = 0xff0000)
                embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                await ctx.send(embed = embed)
            elif check == 0 :
                if msg_bank in bank_list :
                    id = str(id)
                    account_1 = random.randint(1111, 9999)
                    account_2 = random.randint(11, 99)
                    account_3 = id[11:]
                    account = "{}-{}-{}".format(account_1, account_2, account_3)
                    bank = msg_bank
                    money = 0
                    cur.execute("UPDATE UserInfo SET bank = ? WHERE id = ?", (bank, id,))
                    cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (money, id,))
                    cur.execute("UPDATE UserInfo SET account = ? WHERE id = ?", (account, id,))
                    embed = discord.Embed(title = ':closed_lock_with_key: 계좌개설', description = '성공적으로 계좌가 개설되셨습니다.', color = 0xffc0cb)
                    embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                    await ctx.send(embed = embed)
                elif msg_bank not in bank_list :
                    embed = discord.Embed(title = ':closed_lock_with_key: 계좌개설', description = '계좌 개설에 실패하셨습니다.\n은행 명을 다시 확인해 주세요.\n\n개설 가능 은행\n`{}, {}, {}, {}, {}`'.format(bank_list[0], bank_list[1], bank_list[2], bank_list[3], bank_list[4], bank_list[5]), color = 0xff0000)
                    embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                    await ctx.send(embed = embed)
    elif msg_req == '' and msg_bank == '' :
        check = gmser_check(id)
        if check == 0 :
            embed = discord.Embed(title = ':gift: 지원금', description = 'RG Stock 게임 서비스에 가입되어 있지 않습니다.', color = 0xff0000)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        elif check == 1 :
            check = acc_check(id)
            if check == 1:
                total = bring_acc(id)
                bank = total[0]
                acc_num = total[1]
                money = total[2]
                embed = discord.Embed(description = ':atm: **계좌 정보**\n\n은행 : `{}`\n\n계좌번호 : `{}`\n\n잔고 : `{}원`'.format(bank, acc_num, money), color = 0xffc0cb)
                embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                await ctx.send(embed = embed)
            elif check == 0:
                embed = discord.Embed(title = ':atm: 계좌 정보', description = '계좌가 개설되지 않았습니다.', color = 0xff0000)
                embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                await ctx.send(embed = embed)
    con.close()

@bot.command()
async def 지원금(ctx) :
    id = ctx.author.id
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    check = gmser_check(id)
    if check == 0 :
        embed = discord.Embed(title = ':gift: 지원금', description = 'RG Stock 게임 서비스에 가입되어 있지 않습니다.', color = 0xff0000)
        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif check == 1 :
        check = acc_check(id)
        total = bring_acc(id)
        money = total[2]
        if check == 0 :
            embed = discord.Embed(title = ':gift: 지원금', description = '계좌가 개설되지 않았습니다.', color = 0xff0000)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        elif check == 1 and money == 0 :
            ex = random.randint(10000, 50000)
            cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (ex, id,))
            embed = discord.Embed(title = ':gift: 지원금', description = '지원금 `{}`원을 받았습니다.'.format(ex), color = 0xffc0cb)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        elif check == 1 and money != 0 :
            embed = discord.Embed(title = ':gift: 지원금', description = '계좌잔고가 0원일 때 이용 가능합니다.', color = 0xff0000)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
    con.close()

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def 일(ctx) :
    id = ctx.author.id
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    check = gmser_check(id)
    if check == 0 :
        embed = discord.Embed(title = ':gift: 지원금', description = 'RG Stock 게임 서비스에 가입되어 있지 않습니다.', color = 0xff0000)
        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif check == 1 :
        check = acc_check(id)
        if check == 0 :
            embed = discord.Embed(title = ':gift: 지원금', description = '계좌가 개설되지 않았습니다.', color = 0xff0000)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        elif check == 1 :
            total = bring_acc(id)
            money = total[2]
            ex = random.randint(1, 1000)
            cal = money + ex
            cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (cal, id,))
            embed = discord.Embed(title = ':hourglass: 일', description = '일을 하여 `{}`원을 받았습니다.'.format(ex), color = 0xffc0cb)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
    con.close()

@bot.command()
async def 도박(ctx) :
    id = ctx.author.id
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cmd = ctx.message.content[4:]
    check = gmser_check(id)
    if check == 0 :
        embed = discord.Embed(title = ':money_with_wings: 도박', description = 'RG Stock 게임 서비스에 가입되어 있지 않습니다.', color = 0xff0000)
        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif check == 1 :
        check = acc_check(id)
        if check == 0 :
            embed = discord.Embed(title = ':money_with_wings: 도박', description = '계좌가 개설되지 않았습니다.', color = 0xff0000)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        elif check == 1 :
            total = bring_acc(id)
            money = total[2]
            if cmd == '올인' :
                if money == 0 :
                    embed = discord.Embed(title = ':money_with_wings: 도박', description = '돈이 부족합니다.', color = 0xff0000)
                    embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                    await ctx.send(embed = embed)
                else :
                    prob = random.choices(range(1, 3), weights = [50, 50])
                    if prob[0] == 1 :
                        ex = money
                        cal = money + ex
                        cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (cal, id,))
                        embed = discord.Embed(title = ':money_with_wings: 도박', description = '도박을 하여 {}원을 벌었습니다!'.format(ex), color = 0xffc0cb)
                        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                        await ctx.send(embed = embed)
                    elif prob[0] == 2 :
                        ex = money
                        cal = money - ex
                        cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (cal, id,))
                        embed = discord.Embed(title = ':money_with_wings: 도박', description = '도박을 하여 {}원을 잃었습니다..'.format(ex), color = 0xffc0cb)
                        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                        await ctx.send(embed = embed)
            elif cmd != '올인' and type(int(cmd)) == int and int(cmd) != 0 :
                cmd = int(cmd)
                if money < cmd :
                    embed = discord.Embed(title = ':money_with_wings: 도박', description = '돈이 부족합니다.', color = 0xff0000)
                    embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                    await ctx.send(embed = embed)
                else :
                    prob = random.choices(range(1, 3), weights = [50, 50])
                    if prob[0] == 1 :
                        ex = cmd
                        ex = int(ex)
                        cal = money + ex
                        cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (cal, id,))
                        embed = discord.Embed(title = ':money_with_wings: 도박', description = '도박을 하여 {}원을 벌었습니다!'.format(ex), color = 0xffc0cb)
                        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                        await ctx.send(embed = embed)
                    elif prob[0] == 2 :
                        ex = cmd
                        ex = int(ex)
                        cal = money - ex
                        cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (cal, id,))
                        embed = discord.Embed(title = ':money_with_wings: 도박', description = '도박을 하여 {}원을 잃었습니다..'.format(ex), color = 0xffc0cb)
                        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                        await ctx.send(embed = embed)
            elif int(cmd) == 0 :
                embed = discord.Embed(title = ':money_with_wings: 도박', description = '도박에 걸 돈은 자연수여야 합니다.', color = 0xff0000)
                embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                await ctx.send(embed = embed)
    con.close()

@bot.command()
async def 송금(ctx) :
    ex = 0
    id = ctx.author.id
    alr_exist = []
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT id FROM UserInfo WHERE UserInfo.id")
    rows = cur.fetchall()
    for i in range(len(rows)) :
        ex = rows[i]
        alr_exist.append(ex[0])
        ex = 0
    if id not in alr_exist :
        embed = discord.Embed(title = ':envelope_with_arrow: 송금', description = 'RG Stock 게임 서비스에 가입되어 있지 않습니다.', color = 0xff0000)
        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    elif id in alr_exist :
        cur.execute("SELECT * FROM UserInfo WHERE id = ?", (id,))
        rows = cur.fetchall()
        alr_exist2 = list(rows[0])
        bank = alr_exist2[1]
        acc_num = alr_exist2[2]
        money = alr_exist2[3]
        if bank == 'NULL' and acc_num == 'NULL' and money == 'NULL' :
            embed = discord.Embed(title = ':envelope_with_arrow: 송금', description = '계좌가 개설되지 않았습니다.', color = 0xff0000)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        else :
            req_bank = ctx.message.content[4:8]
            req_acc_num = ctx.message.content[9:24]
            req_money = ctx.message.content[25:]
            cur.execute("SELECT * FROM UserInfo WHERE account = ?", (req_acc_num,))
            rows = cur.fetchall()
            alr_exist3 = list(rows[0])
            check_id = alr_exist3[0]
            check_bank = alr_exist3[1]
            check_acc_num = alr_exist3[2]
            check_money = alr_exist3[3]
            if req_bank == check_bank and req_acc_num == check_acc_num :
                fee = (int(req_money) // 10)
                cal = int(req_money)
                check_money = check_money + cal
                money = money - (cal + fee)
                if money >= 0 :
                    if int(req_money) > 0:
                        cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (money, id,))
                        cur.execute("UPDATE UserInfo SET money = ? WHERE id = ?", (check_money, check_id))
                        embed = discord.Embed(title = ':envelope_with_arrow: 송금 완료', description = '거래일 : `{}`\n\n출금계좌 : `{} {}`\n\n입금계좌 : `{} {}`\n\n이체금액 : `{}원`\n\n수수료 : `{}원`'.format(nowDatetime, bank, acc_num, req_bank, req_acc_num, req_money, fee), color = 0xffc0cb)
                        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                        await ctx.send(embed = embed)
                    else :
                        embed = discord.Embed(title = ':envelope_with_arrow: 송금 실패', description = '보내실 금액을 0보다 큰 수로 설정해주세요.', color = 0xff0000)
                        embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                        await ctx.send(embed = embed)
                elif money < 0 :
                    embed = discord.Embed(title = ':envelope_with_arrow: 송금 실패', description = '잔액이 부족합니다.', color = 0xff0000)
                    embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                    await ctx.send(embed = embed)
            else :
                embed = discord.Embed(title = ':envelope_with_arrow: 송금 실패', description = '은행 또는 계좌번호가 틀렸습니다.\n`은행 또는 계좌번호를 다시 확인해주세요.`', color = 0xff0000)
                embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
                await ctx.send(embed = embed)
    con.close()

@bot.command()
async def 주식(ctx) :
    req = ctx.message.content[4:]
    id = ctx.author.id
    if req == "차트" :
        now_price = now_stock_price()
        price_updown_pic = stock_updown_pic()
        price_updown_giho = stock_updown_giho()
        price_updown = updown_price()
        check = gmser_check(id)
        if check == 1 :
            embed = discord.Embed(title = ':chart_with_upwards_trend: | RG 주식 차트 | :chart_with_downwards_trend:', description = '{} 기준\n```{} 삼산테크    {}    ({}  {})\n{} 따브류엠    {}    ({}  {})\n{} 루이조선    {}    ({}  {})\n{} 테수울라    {}    ({}  {})\n{} 비뜨코인    {}    ({}  {})```'.format(now_price[5], price_updown_pic[0], now_price[0], price_updown_giho[0], price_updown[0], price_updown_pic[1], now_price[1], price_updown_giho[1], price_updown[1], price_updown_pic[2], now_price[2], price_updown_giho[2], price_updown[2], price_updown_pic[3], now_price[3], price_updown_giho[3], price_updown[3], price_updown_pic[4], now_price[4], price_updown_giho[4], price_updown[4]), color = 0xffc0cb)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        elif check == 0 :
            embed = discord.Embed(title = ':chart_with_upwards_trend: | RG 주식 차트 | :chart_with_downwards_trend:', description = 'RG Stock 게임 서비스에 가입되어 있지 않습니다.', color = 0xff0000)
            embed.set_footer(text = f"{ctx.message.author.name} | RG Stock#1639", icon_url = ctx.message.author.avatar_url)
            await ctx.send(embed = embed)

bot.run(token)
