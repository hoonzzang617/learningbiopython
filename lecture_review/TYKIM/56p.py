regNum0 = input("1st person's birth date : ")
regNum1 = input("2nd person's birth date : ")
regNum2 = input("3rd person's birth date : ")

d_month = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "Mar",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}

print("regNum0:", d_month[regNum0[2:4]] + "-" + regNum0[4:6])
print("regNum1:", d_month[regNum1[2:4]] + "-" + regNum1[4:6])
print("regNum2:", d_month[regNum2[2:4]] + "-" + regNum2[4:6])
