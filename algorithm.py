import random
import sqlite3

private_money = 0 # 개인 돈 저장 변수
company_name = ['삼산테크', '따브류엠', '루이조선', '테수울라', '비뜨코인'] # 주식 회사 명
now_stock_price = [33000, 28000, 78000, 40000, 150000] # 현재 기업별 주가
up_down = [] # 주가의 상승 또는 하락을 저장하는 리스트
updown_price = [] # up_down의 결과에 따라 상승하거나 하락하게 될 가격을 저장하는 리스트
ex = 0 #임시로 저장할 값이 있을 때 저장하는 변수

# 랜덤으로 주가의 상승과 하락을 결정하는 반복문
for i in range(len(company_name)) :
    ex = random.randint(1, 20)
    if ex == 1 or ex == 2 or ex == 3 or ex == 4 or ex == 5 or ex == 6 or ex == 7 or ex == 8 :
        ex = 'up'
    elif ex == 9 or ex == 10 or ex == 11 or ex == 12 or ex == 13 or ex == 14 or ex == 15 or ex == 16 :
        ex = 'down'
    elif ex == 17 or ex == 18 or ex == 19 or ex == 20 :
        ex = 'now'
    up_down.append(ex)
    ex = 0

# 주가의 상승하거나 하락할 가격을 정하는 반복문
for i in range(len(company_name)) :
    ex = random.randint(100, 500)
    updown_price.append(ex)
    ex = 0

# 상승과 하락, 가격을 적용하는 반복문
for i in range(len(company_name)) :
    if up_down[i] == 'up' :
        now_stock_price[i] = now_stock_price[i] + updown_price[i]
    elif up_down[i] == 'down' :
        now_stock_price[i] = now_stock_price[i] - updown_price[i]
    elif up_down[i] == 'now' :
        now_stock_price[i] = now_stock_price[i]

print(up_down)
print(updown_price)
print(now_stock_price)