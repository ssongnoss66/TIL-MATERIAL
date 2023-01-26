"""문자열의 거울상"""

for i in range(1, (int(input())+1)):
    srtdStr =  input().strip()
    prntStr = str()
    for j in srtdStr[::-1]:
        if j == "b":
            prntStr += "d"
        elif j == "d":
            prntStr += "b"
        elif j == "p":
            prntStr += "q"
        else:
            prntStr += "p"
    print(f"#{i} {prntStr}")