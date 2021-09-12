lang0 = ["Python", "Java"]
lang1 = ["C", "C++", "VB"]
# lang1.append("hi")
# print(lang1)

# lang0.extend(lang1)
# totalLang = lang0
# print(totalLang)
# totalLang = lang0.extend(lang1) 이렇게 하면 안되나?

# for i in lang1:
#     lang0.append(i)

# i = 0
# while i < len(lang1):

#     lang0.append(lang1[i])
#     i += 1

len_lang1 = len(lang1)
i = 0
while i < len_lang1:

    lang0.append(lang1.pop())
    i += 1


print(lang0)


# x = "stupid!"
# x.replace("!", "?")
# print(x)

