import sys

# # x = sys.argv[1]
# # y = sys.argv[2]
# fil1 = ""
# fi1 = open(sys.argv[1], "r")
# for i in fi1:
#     fil1 += i.strip() + f"\t{sys.argv[1]}\n"
#     # fil1 += f"\t{x}\n"
# fi1.close()

# fil2 = ""
# fi2 = open(sys.argv[2], "r")
# for i in fi2:
#     fil2 += i.strip() + f"\t{sys.argv[1]}\n"
#     # fil2 += f"\t{y}\n"
# fi2.close()

# fi3 = open("Test3.txt", "w")
# fi3.write("Group\tdata1\tdata2\tSample\n")
# fi3.write(fil1)
# fi3.write(fil2)
# fi3.close


def combine(fi_name):
    fil = ""
    fi = open(fi_name, "r")
    for i in fi:
        fil += i.strip() + f"\t{fi_name}\n"
    fi.close()
    return fil


fil1 = combine(sys.argv[1])
fil2 = combine(sys.argv[2])
fi3 = open("Test4.txt", "w")
fi3.write("Group\tdata1\tdata2\tSample\n")
fi3.write(fil1)
fi3.write(fil2)
fi3.close()
