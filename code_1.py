import operator_1
cap_j1, cap_j2 = input("Enter cap of j1 and j2: ").split(" ")
j1, j2 = input("Enter initial values of j1 and j2:  ").split(" ")
goal1, goal2 = input("enter final values in j1 and j2:  ").split(" ")
while int(j1) != int(goal1) or int(j2) != int(goal2):
    r = int(input("Rule 1 : fill the jug \nRule 2 : Empty the jug\nRule 3: pour some from either of them\n"))
    if r == 1:
        jug = input("which jug j1 or j2 :")
        if jug == "j1":
            j1 = operator_1.rule1(int(j1), int(cap_j1))
            print("The values of j1 and j2 are : ", j1, j2)
        elif jug == "j2":
            j2 = operator_1.rule1(int(j2), int(cap_j2))
            print("The values of j1 and j2 are : ", j1, j2)
    if r == 2:
        jug = input("which jug j1 or j2 :")
        if jug == "j1":
            j1 = operator_1.rule2(int(j1))
            print("The values of j1 and j2 are : ", j1, j2)
        elif jug == "j2":
            j2 = operator_1.rule2(int(j2))
            print("The values of j1 and j2 are : ", j1, j2)
    if r == 3:
        jug = input("j1 to j2 or j2 to j1 ")
        if jug == "j2 to j1":
            j1, j2 = operator_1.rule3(int(j1), int(j2), int(cap_j1), int(cap_j2))
            print("The values of j1 and j2 are : ", j1, j2)
        elif jug == "j1 to j2":
            j2, j1 = operator_1.rule3(int(j2), int(j1), int(cap_j2), int(cap_j1))
            print("The values of j1 and j2 are : ", j1, j2)
print("Goal State Reached ! the values of j1 and j2: ", j1, j2)
