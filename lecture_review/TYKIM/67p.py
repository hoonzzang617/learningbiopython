money = input("USD, EUR, JPY, CNY :")

each_money = money.split(",")

USD = 1203.82
EUR = 1365.73
JPY = 11.22
CNY = 172.04

d = {}
for i in each_money:
    list_money = i.strip().split()
    d[list_money[1]] = list_money[0]

print(list_money)

print(d)

usd = round(int(d["USD"]) * USD, 2)
eur = round(int(d["EUR"]) * EUR, 2)
jpy = round(int(d["JPY"]) * JPY, 2)
cny = round(int(d["CNY"]) * CNY, 2)

print(f"{usd} KRW, {eur} KRW, {jpy} KRW, {cny} KRW")

