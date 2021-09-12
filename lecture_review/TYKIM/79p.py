# print(end=" ")
# print("abc", end=" ")
# print("def", "ghi", sep=" /")

num0 = input("num0 : ")
num1 = input("num1 : ")
op = input("op : ")


def calc(num0, num1, op):
    if op == "+":
        result = num0 + num1
    elif op == "-":
        result = num0 - num1
    elif op == "*":
        result = num0 * num1
    elif op == "/":
        result = num0 / num1
    return result


result = calc(int(num0), int(num1), op)
print(f"{num0} {op} {num1} =", result)

