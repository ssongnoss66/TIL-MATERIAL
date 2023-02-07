"""괄호 짝짓기 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AV14eWb6AAkCFAYD&probBoxId=AYYQ-fnKCuYDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+2%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

appndLi = []

for i in range(1, 11):
    rng = int(input())
    inptLi = list(input().strip())
    cnt = 0
    if inptLi.count("(") == inptLi.count(")") and inptLi.count("[") == inptLi.count("]") and inptLi.count("{") == inptLi.count("}") and inptLi.count("<")==inptLi.count(">"):
        # print(f"appndLi {appndLi}")
        for j in inptLi:
            if j in ["(", "[", "{", "<"]:
                appndLi.append(j)
                cnt += 1
                # print(f"appndLi {appndLi}")
            else:
                if (j == ")" and not appndLi[-1] == "(") or (j == "]" and not appndLi[-1] == "[") or (j == "}" and not appndLi[-1] == "{") or (j == ">" and not appndLi[-1] == "<"):
                    print(f"#{i} 0")
                    break
                elif (j == ")" and appndLi[-1] == "(") or (j == "]" and appndLi[-1] == "[") or (j == "}" and appndLi[-1] == "{") or (j == ">" and appndLi[-1] == "<"):
                    appndLi.pop()
                    cnt += 1
                    # print(cnt)
                    if cnt == rng:
                        print(f"#{i} 1")
    else:       
        print(f"#{i} 0")