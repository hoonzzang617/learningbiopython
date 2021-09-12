score = input("score: ")

int_score = int(score)

if 90 <= int_score <= 100:
    print("A")
elif 80 <= int_score < 90:
    print("B")
elif 70 <= int_score < 80:
    print("C")
elif 60 <= int_score < 70:
    print("D")
else:
    print("F")
