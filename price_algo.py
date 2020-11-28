import sqlite3
import datetime
import random
import time

beforeDatetime = "2020-11-28 19:01:55"

while True :
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    con = sqlite3.connect(r'C:\Users\ykjrc\OneDrive\바탕 화면\코딩 작업파일\주식 게임\stock game data.db', isolation_level = None)
    cur = con.cursor()
    cur.execute("SELECT * FROM Stock_Price WHERE Change_time = ?", (beforeDatetime,))
    rows = cur.fetchall()
    nowprice = list(rows[0])
    up_down = [] # 주가의 상승 또는 하락을 저장하는 리스트
    up_down_plma = []
    up_down_pic = []
    updown_price = [] # up_down의 결과에 따라 상승하거나 하락하게 될 가격을 저장하는 리스트
    ex = 0 #임시로 저장할 값이 있을 때 저장하는 변수

    for i in range(len(nowprice) - 1) : # 랜덤으로 주가의 상승과 하락을 결정하는 반복문
        ex = random.randint(1, 20)
        if ex == 1 or ex == 2 or ex == 3 or ex == 4 or ex == 5 or ex == 6 or ex == 7 or ex == 8 :
            ex = 'up'
        elif ex == 9 or ex == 10 or ex == 11 or ex == 12 or ex == 13 or ex == 14 or ex == 15 or ex == 16 :
            ex = 'down'
        elif ex == 17 or ex == 18 or ex == 19 or ex == 20 :
            ex = 'now'
        up_down.append(ex)
        ex = 0

    for i in up_down : # 주가의 상승과 하락을 플러스와 마이너스 기호로 나타내는 반복문
        if i == 'up' :
            up_down_plma.append('+')
        elif i == 'down' :
            up_down_plma.append('-')
        elif i == 'now' :
            up_down_plma.append('=')

    up_down_plma.append(nowDatetime)
    cur.execute("UPDATE updown SET samsan_tech = ? WHERE date = ?", (up_down_plma[0], beforeDatetime,))
    cur.execute("UPDATE updown SET wm_enter = ? WHERE date = ?", (up_down_plma[1], beforeDatetime,))
    cur.execute("UPDATE updown SET rui_ship = ? WHERE date = ?", (up_down_plma[2], beforeDatetime,))
    cur.execute("UPDATE updown SET tesla = ? WHERE date = ?", (up_down_plma[3], beforeDatetime,))
    cur.execute("UPDATE updown SET bitcoin = ? WHERE date = ?", (up_down_plma[4], beforeDatetime,))
    cur.execute("UPDATE updown SET date = ? WHERE date = ?", (up_down_plma[5], beforeDatetime,))

    for i in up_down : # 주가의 상승과 하락을 상승모양과 하락모양으로 나타내는 반복문
        if i == 'up' :
            up_down_pic.append('▲')
        elif i == 'down' :
            up_down_pic.append('▼')
        elif i == 'now' :
            up_down_pic.append('─')
    
    up_down_pic.append(nowDatetime)
    cur.execute("UPDATE updown_pic SET samsan_tech = ? WHERE date = ?", (up_down_pic[0], beforeDatetime,))
    cur.execute("UPDATE updown_pic SET wm_enter = ? WHERE date = ?", (up_down_pic[1], beforeDatetime,))
    cur.execute("UPDATE updown_pic SET rui_ship = ? WHERE date = ?", (up_down_pic[2], beforeDatetime,))
    cur.execute("UPDATE updown_pic SET tesla = ? WHERE date = ?", (up_down_pic[3], beforeDatetime,))
    cur.execute("UPDATE updown_pic SET bitcoin = ? WHERE date = ?", (up_down_pic[4], beforeDatetime,))
    cur.execute("UPDATE updown_pic SET date = ? WHERE date = ?", (up_down_pic[5], beforeDatetime,))

    for i in range(len(nowprice) - 2) : # 주가의 상승하거나 하락할 가격을 정하는 반복문
        ex = random.randint(100, 3000)
        updown_price.append(ex)
        ex = 0

    for i in range(1) : # 비트코인의 상승하거나 하락할 가격을 정하는 반복문
        ex = random.randint(1, 300000)
        updown_price.append(ex)
        ex = 0

    updown_price.append(nowDatetime)
    if up_down[0] != 'now' :
        cur.execute("UPDATE updown_price SET samsan_tech = ? WHERE date = ?", (updown_price[0], beforeDatetime,))
    elif up_down[0] == 'now' :
        cur.execute("UPDATE updown_price SET samsan_tech = ? WHERE date = ?", (0, beforeDatetime,))
    if up_down[1] != 'now' :
        cur.execute("UPDATE updown_price SET wm_enter = ? WHERE date = ?", (updown_price[1], beforeDatetime,))
    elif up_down[1] == 'now' :
        cur.execute("UPDATE updown_price SET wm_enter = ? WHERE date = ?", (0, beforeDatetime,))
    if up_down[2] != 'now' :
        cur.execute("UPDATE updown_price SET rui_ship = ? WHERE date = ?", (updown_price[2], beforeDatetime,))
    elif up_down[2] == 'now' :
        cur.execute("UPDATE updown_price SET rui_ship = ? WHERE date = ?", (0, beforeDatetime,))
    if up_down[3] != 'now' :
        cur.execute("UPDATE updown_price SET tesla = ? WHERE date = ?", (updown_price[3], beforeDatetime,))
    elif up_down[3] == 'now' :
        cur.execute("UPDATE updown_price SET tesla = ? WHERE date = ?", (0, beforeDatetime,))
    if up_down[4] != 'now' :
        cur.execute("UPDATE updown_price SET bitcoin = ? WHERE date = ?", (updown_price[4], beforeDatetime,))
    elif up_down[4] == 'now' :
        cur.execute("UPDATE updown_price SET bitcoin = ? WHERE date = ?", (0, beforeDatetime,))
    cur.execute("UPDATE updown_price SET date = ? WHERE date = ?", (updown_price[5], beforeDatetime,))

    for i in range(len(nowprice) - 1) : # 상승과 하락, 가격을 적용하는 반복문
        if up_down[i] == 'up' :
            nowprice[i] = nowprice[i] + updown_price[i]
        elif up_down[i] == 'down' :
            nowprice[i] = nowprice[i] - updown_price[i]
            if nowprice[i] < 0 :
                nowprice[i] = 1
        elif up_down[i] == 'now' :
            continue

    nowprice[5] = nowDatetime
    cur.execute("UPDATE Stock_Price SET samsan_tech = ? WHERE Change_time = ?", (nowprice[0], beforeDatetime,))
    cur.execute("UPDATE Stock_Price SET wm_enter = ? WHERE Change_time = ?", (nowprice[1], beforeDatetime,))
    cur.execute("UPDATE Stock_Price SET rui_ship = ? WHERE Change_time = ?", (nowprice[2], beforeDatetime,))
    cur.execute("UPDATE Stock_Price SET tesla = ? WHERE Change_time = ?", (nowprice[3], beforeDatetime,))
    cur.execute("UPDATE Stock_Price SET bitcoin = ? WHERE Change_time = ?", (nowprice[4], beforeDatetime,))
    cur.execute("UPDATE Stock_Price SET Change_time = ? WHERE Change_time = ?", (nowprice[5], beforeDatetime,))
    beforeDatetime = nowprice[5]
    con.close()

    print("주가 변동 !")
    print("삼산테크 : {}\n따브류엠 : {}\n루이조선 : {}\n테수울라 : {}\n비뜨코인 : {}".format(nowprice[0], nowprice[1], nowprice[2], nowprice[3], nowprice[4]))

    time.sleep(30)