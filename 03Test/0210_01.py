"""반반 """

from sys import stdin as s
input = open("/Users/e_o_n_l_a_/Desktop/패캠)TIL&MATERIAL/03Test/input.txt","rt").readline

for i in range(1, int(input())+1):
    inptLi = list(input().strip())
    # print(inptLi)
    inptSt = list(set(inptLi))
    # print(inptSt)
    try:
        if inptLi.count(inptSt[0]) == inptLi.count(inptSt[1]) == 2:
            print(f"#{i} Yes")
        else:
            print(f"#{i} No")
    except:
        print(f"#{i} No")