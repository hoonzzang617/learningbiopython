s = input("s : ")
h = input("h : ")

cnt = 0
cnt1 = 0

n = 0

for i in s:
    if i != h[n]:
        cnt += 1
    n += 1

print(cnt)
# for i in s:
#     for x in h:
#         pass
#     if i != x:
#         cnt += 1
#     elif i == x:
#         cnt1 += 1
# print(cnt)
# print(cnt1)

