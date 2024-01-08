
def getfrand():
    s = 0
    with open("rand","r") as randfile:
        s = int(randfile.readline())
    randfile.close()
    return s

s = getfrand()
def newrand():
    global s

    a = 4567890153
    c = 9871456645654
    m = 2**32

    s = (a*s + c)%m

    with open("rand","w") as randfile:
        randfile.write(f"{s}")

    randfile.close()
    return s

for i in range(7):
    print(newrand())
